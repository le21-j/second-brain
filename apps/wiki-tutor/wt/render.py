"""Output rendering: LaTeX → Unicode, wiki-links → OSC 8 hyperlinks.

Transforms raw LLM output (LaTeX, wiki-links, Obsidian callouts) into a string
ready for Textual's Markdown widget.
"""

from __future__ import annotations

import os
import re
import urllib.parse
from collections.abc import Callable
from pathlib import Path

from .constants import DEFAULT_VAULT_NAME, SUPPORTED_TERM_PROGRAMS

GREEK_LOWER = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "iota": "ι", "kappa": "κ",
    "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "omicron": "ο",
    "pi": "π", "rho": "ρ", "sigma": "σ", "tau": "τ", "upsilon": "υ",
    "phi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
}
GREEK_UPPER = {
    "Alpha": "Α", "Beta": "Β", "Gamma": "Γ", "Delta": "Δ", "Epsilon": "Ε",
    "Zeta": "Ζ", "Eta": "Η", "Theta": "Θ", "Iota": "Ι", "Kappa": "Κ",
    "Lambda": "Λ", "Mu": "Μ", "Nu": "Ν", "Xi": "Ξ", "Omicron": "Ο",
    "Pi": "Π", "Rho": "Ρ", "Sigma": "Σ", "Tau": "Τ", "Upsilon": "Υ",
    "Phi": "Φ", "Chi": "Χ", "Psi": "Ψ", "Omega": "Ω",
}
OPS = {
    "leq": "≤", "geq": "≥", "neq": "≠", "approx": "≈", "propto": "∝",
    "pm": "±", "infty": "∞", "to": "→", "mapsto": "↦", "in": "∈",
    "subset": "⊂", "subseteq": "⊆", "cup": "∪", "cap": "∩",
    "cdot": "·", "times": "×", "div": "÷", "circ": "∘", "otimes": "⊗",
    "sum": "Σ", "int": "∫", "partial": "∂", "nabla": "∇", "forall": "∀",
    "exists": "∃", "emptyset": "∅", "Re": "ℜ", "Im": "ℑ",
    "ldots": "…", "cdots": "⋯", "rightarrow": "→", "leftarrow": "←",
    "Rightarrow": "⇒", "Leftarrow": "⇐", "iff": "⇔",
    "top": "ᵀ", "bot": "⊥", "perp": "⊥", "parallel": "∥",
    "log": "log", "ln": "ln", "sin": "sin", "cos": "cos", "tan": "tan",
    "exp": "exp", "min": "min", "max": "max", "argmax": "argmax",
    "argmin": "argmin", "left": "", "right": "",
    "bigl": "", "bigr": "", "Bigl": "", "Bigr": "",
    "quad": "   ", "qquad": "      ",
}
LATEX_STRIP_BRACES_CMDS = (
    "text", "textit", "textbf", "textsf", "texttt",
    "mathbf", "mathbb", "mathcal", "mathfrak", "mathit", "mathrm", "mathsf",
    "boldsymbol", "operatorname", "bm",
)
ACCENT_COMBINING = {
    "vec": "⃗",
    "hat": "̂",
    "widehat": "̂",
    "bar": "̄",
    "overline": "̄",
    "tilde": "̃",
    "widetilde": "̃",
    "dot": "̇",
    "ddot": "̈",
    "check": "̌",
    "breve": "̆",
    "grave": "̀",
    "acute": "́",
    "underline": "̲",
    "overrightarrow": "⃗",
    "overleftarrow": "⃖",
}
SUPER_DIGIT = str.maketrans(
    "0123456789+-=()abcdefghijklmnoprstuvwxyz",
    "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ",
)
SUB_DIGIT = str.maketrans(
    "0123456789+-=()aehijklmnoprstuvx",
    "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ",
)

LATEX_CMD_RE = re.compile(r"\\([A-Za-z]+)")
DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
INLINE_MATH_RE = re.compile(r"\$([^\$\n]+?)\$")
FRAC_RE = re.compile(r"\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}")
SQRT_RE = re.compile(r"\\sqrt\s*\{([^{}]+)\}")
SUP_BRACE_RE = re.compile(r"\^\{([^{}]+)\}")
SUB_BRACE_RE = re.compile(r"_\{([^{}]+)\}")
SUP_SINGLE_RE = re.compile(r"\^([A-Za-z0-9])")
SUB_SINGLE_RE = re.compile(r"_([A-Za-z0-9])")
WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\]|\n]+)(?:\|([^\]\n]+))?\]\]")
EMBED_RE = re.compile(r"!\[\[([^\]|\n]+)(?:\|([^\]\n]+))?\]\]")
HIGHLIGHT_RE = re.compile(r"==([^=\n]+)==")
BLOCK_REF_RE = re.compile(r"\s\^[a-zA-Z0-9-]+\b")
CODE_FENCE_RE = re.compile(r"(```.*?```|`[^`\n]+`)", re.DOTALL)
CONTROL_BYTE_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
STRIP_BRACES_RE = re.compile(
    r"\\(?:" + "|".join(LATEX_STRIP_BRACES_CMDS) + r")\s*\{([^{}]+)\}"
)
ACCENT_RE = re.compile(
    r"\\(" + "|".join(ACCENT_COMBINING) + r")\s*\{([^{}]+)\}"
)
CALLOUT_RE = re.compile(r"^>[ \t]*\[!(\w+)\]([+-]?)[ \t]*(.*)$", re.MULTILINE)
CALLOUT_ICONS = {
    "note": "📝", "info": "ℹ️", "tip": "💡", "hint": "💡",
    "important": "❗", "warning": "⚠️", "caution": "⚠️", "danger": "🔥",
    "example": "🔬", "question": "❓", "todo": "✅", "done": "✔️",
    "abstract": "📑", "summary": "📑", "tldr": "📑", "quote": "💬",
    "success": "✔️", "failure": "❌", "bug": "🐛",
}


def _replace_cmd(match: re.Match[str]) -> str:
    name = match.group(1)
    if name in GREEK_LOWER:
        return GREEK_LOWER[name]
    if name in GREEK_UPPER:
        return GREEK_UPPER[name]
    if name in OPS:
        return OPS[name]
    return match.group(0)


def _accent_replace(match: re.Match[str]) -> str:
    cmd = match.group(1)
    arg = match.group(2).strip()
    combining = ACCENT_COMBINING[cmd]
    if len(arg) == 1:
        return arg + combining
    return arg[0] + combining + arg[1:] if cmd in ("vec", "overrightarrow", "overleftarrow") else arg + combining


def _math_pass(expr: str) -> str:
    expr = STRIP_BRACES_RE.sub(lambda m: m.group(1), expr)
    expr = ACCENT_RE.sub(_accent_replace, expr)
    expr = SUB_BRACE_RE.sub(lambda m: m.group(1).translate(SUB_DIGIT), expr)
    expr = SUP_BRACE_RE.sub(lambda m: m.group(1).translate(SUPER_DIGIT), expr)
    expr = SUB_SINGLE_RE.sub(lambda m: m.group(1).translate(SUB_DIGIT), expr)
    expr = SUP_SINGLE_RE.sub(lambda m: m.group(1).translate(SUPER_DIGIT), expr)
    expr = FRAC_RE.sub(lambda m: f"({m.group(1)})/({m.group(2)})", expr)
    expr = SQRT_RE.sub(lambda m: f"√({m.group(1)})", expr)
    expr = LATEX_CMD_RE.sub(_replace_cmd, expr)
    expr = expr.replace("\\\\", "\n    ")
    expr = expr.replace("\\,", " ").replace("\\!", "").replace("\\;", " ")
    expr = expr.replace("\\{", "{").replace("\\}", "}")
    return expr.strip()


FRAC_INLINE_RE = re.compile(
    r"\(((?:[^()\n]|\([^()\n]*\))+)\)/\(((?:[^()\n]|\([^()\n]*\))+)\)"
)


def _visible_len(s: str) -> int:
    # Count visible chars: skip Unicode combining marks (U+0300..U+036F, U+20D0..U+20FF).
    out = 0
    for ch in s:
        cp = ord(ch)
        if 0x0300 <= cp <= 0x036F or 0x20D0 <= cp <= 0x20FF:
            continue
        out += 1
    return out


def _pad(s: str, width: int) -> str:
    return s + " " * max(0, width - _visible_len(s))


def _center(s: str, width: int) -> str:
    pad = max(0, width - _visible_len(s))
    left = pad // 2
    right = pad - left
    return " " * left + s + " " * right


def _stack_fractions_in_line(line: str) -> str:
    matches = list(FRAC_INLINE_RE.finditer(line))
    if not matches:
        return line
    top: list[str] = []
    mid: list[str] = []
    bot: list[str] = []
    pos = 0
    for m in matches:
        if m.start() > pos:
            chunk = line[pos:m.start()]
            w = _visible_len(chunk)
            top.append(" " * w)
            mid.append(chunk)
            bot.append(" " * w)
        num, den = m.group(1), m.group(2)
        w = max(_visible_len(num), _visible_len(den))
        top.append(_center(num, w))
        mid.append("─" * w)
        bot.append(_center(den, w))
        pos = m.end()
    if pos < len(line):
        chunk = line[pos:]
        w = _visible_len(chunk)
        top.append(" " * w)
        mid.append(chunk)
        bot.append(" " * w)
    return "\n".join([
        "".join(top).rstrip(),
        "".join(mid).rstrip(),
        "".join(bot).rstrip(),
    ])


def _format_display_math(content: str) -> str:
    if not content:
        return ""
    rendered = _math_pass(content)
    formatted = "\n".join(_stack_fractions_in_line(line) for line in rendered.split("\n"))
    indented = "\n".join("    " + line if line else "" for line in formatted.split("\n"))
    return f"\n\n{indented}\n"


def _math_only(text: str) -> str:
    text = DISPLAY_MATH_RE.sub(lambda m: _format_display_math(m.group(1).strip()), text)
    text = INLINE_MATH_RE.sub(
        lambda m: _math_pass(m.group(1)) if m.group(1).strip() else "",
        text,
    )
    return text


def latex_to_unicode(text: str) -> str:
    parts = CODE_FENCE_RE.split(text)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)
            continue
        out.append(_math_only(part))
    return "".join(out)


def strip_control_bytes(text: str) -> str:
    return CONTROL_BYTE_RE.sub("", text)


def _callout_replace(match: re.Match[str]) -> str:
    kind = match.group(1).lower()
    title = match.group(3).strip()
    icon = CALLOUT_ICONS.get(kind, "📌")
    label = kind.upper()
    if title:
        return f"> **{icon} {label}** — {title}"
    return f"> **{icon} {label}**"


def normalize_obsidian(text: str) -> str:
    text = CALLOUT_RE.sub(_callout_replace, text)
    text = HIGHLIGHT_RE.sub(lambda m: f"**{m.group(1)}**", text)
    text = EMBED_RE.sub(
        lambda m: f"📄 **[[{m.group(1).strip()}]]**", text
    )
    text = BLOCK_REF_RE.sub("", text)
    return text


def obsidian_url(stem: str, vault: str = DEFAULT_VAULT_NAME) -> str:
    return (
        f"obsidian://open?"
        f"vault={urllib.parse.quote(vault, safe='')}"
        f"&file={urllib.parse.quote(stem, safe='')}"
    )


def osc8_supported() -> bool:
    if os.environ.get("WT_FORCE_OSC8") == "1":
        return True
    return os.environ.get("TERM_PROGRAM") in SUPPORTED_TERM_PROGRAMS


def resolve_wikilinks(
    text: str,
    resolver: Callable[[str], Path | None],
    vault: str = DEFAULT_VAULT_NAME,
) -> str:
    use_osc8 = osc8_supported()

    def replace(match: re.Match[str]) -> str:
        stem = match.group(1).strip()
        label = (match.group(2) or stem).strip()
        target = resolver(stem)
        if target is None:
            return f"[[{label}]]"
        if not use_osc8:
            return f"[[{label}]]"
        url = obsidian_url(stem, vault=vault)
        return f"\x1b]8;;{url}\x1b\\[[{label}]]\x1b]8;;\x1b\\"

    return WIKILINK_RE.sub(replace, text)


def render(
    text: str,
    resolver: Callable[[str], Path | None],
    vault: str = DEFAULT_VAULT_NAME,
) -> str:
    text = strip_control_bytes(text)
    text = normalize_obsidian(text)
    text = latex_to_unicode(text)
    text = resolve_wikilinks(text, resolver, vault=vault)
    return text
