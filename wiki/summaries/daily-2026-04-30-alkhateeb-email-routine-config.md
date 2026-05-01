---
title: "Deferred routine config — Wi-Lab cold email to Alkhateeb"
type: summary
source_type: other
source_path: ""
source_date: 2026-04-30
course:
  - "[[python-ml-wireless]]"
tags:
  - schedule
  - routine
  - wi-lab
  - alkhateeb
  - cold-email
  - deferred
created: 2026-04-30
---

# Deferred routine config — draft cold email to Alkhateeb

Saved on **2026-04-30** from a phy-ml-coach session. Jayden offered to schedule a remote agent for ~mid-April 2027 to draft the Wi-Lab cold email after the portfolio is shipped. Jayden chose to **defer the schedule** — the agent isn't created yet. When ready, paste the body below into `/schedule` (or run `RemoteTrigger create` directly) with a `run_once_at` of choice.

## Trigger reasoning

- **Why this routine exists:** [[alkhateeb]] guidance says do not cold-email until at least one LWM/DeepMIMO/Sionna repo is live. The [[python-ml-wireless]] roadmap puts the Wi-Lab cold-email window at **late May → early Sep 2027** (for Fall 2028 PhD admission). Mid-April 2027 is the right pre-window slot for portfolio audit + draft + iteration.
- **Why deferred locally:** Jayden wants flexibility on the exact firing date — he'll set it once Phase 3 (M7 — Sionna neural receiver reproduction) is on track in early 2027.
- **Decision rule for setting the date later:** fire it ~6 weeks before send. If portfolio is solid by Mar 2027, set fire date to early-Apr 2027. If the roadmap is slipping, push fire date to late-May 2027 and shrink the iteration window.

## Decisions locked in

| Field | Value |
|---|---|
| Name | `Draft Wi-Lab cold email to Alkhateeb` |
| Model | `claude-opus-4-7` |
| Repo | `https://github.com/le21-j/second-brain` |
| Tools | `Bash, Read, Write, Edit, Glob, Grep, WebFetch` |
| MCP | Gmail connector attached (creates draft directly in inbox) |
| Environment | Default (`env_01W3dTHH3VBYbiDy4oVXCaHj`, anthropic_cloud) |
| Schedule type | One-time (`run_once_at`) |
| Fire date | **TBD** — set when Jayden gives the green light |
| Default proposal | Wed, Apr 14, 2027 @ 9:00 AM Phoenix = `2027-04-14T16:00:00Z` UTC |

## When ready — drop into `RemoteTrigger create`

Replace `RUN_ONCE_AT_PLACEHOLDER` with an RFC3339 UTC timestamp. Generate a fresh lowercase v4 UUID for `events[].data.uuid`.

```json
{
  "name": "Draft Wi-Lab cold email to Alkhateeb",
  "run_once_at": "RUN_ONCE_AT_PLACEHOLDER",
  "enabled": true,
  "job_config": {
    "ccr": {
      "environment_id": "env_01W3dTHH3VBYbiDy4oVXCaHj",
      "session_context": {
        "model": "claude-opus-4-7",
        "sources": [
          {"git_repository": {"url": "https://github.com/le21-j/second-brain"}}
        ],
        "allowed_tools": ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebFetch"]
      },
      "events": [
        {"data": {
          "uuid": "GENERATE_FRESH_UUID_V4",
          "session_id": "",
          "type": "user",
          "parent_tool_use_id": null,
          "message": {
            "content": "PROMPT_BELOW",
            "role": "user"
          }
        }}
      ]
    }
  },
  "mcp_connections": [
    {
      "connector_uuid": "856ce64a-293a-4302-ba92-d13cf5031eda",
      "name": "Gmail",
      "url": "https://gmailmcp.googleapis.com/mcp/v1"
    }
  ]
}
```

## The prompt to embed (verbatim)

Paste this string into `events[0].data.message.content`, replacing `PROMPT_BELOW` above. It is fully self-contained — the remote agent has no memory of this conversation.

```
You are a one-shot scheduled agent. This routine was queued on 2026-04-30 from a phy-ml-coach
session for Jayden Le, an EE/DSP undergrad at ASU working through the [[python-ml-wireless]]
14-month roadmap (committed April 2026). Today's task: audit shipped portfolio artifacts and
draft a cold email to Professor Ahmed Alkhateeb (Wireless Intelligence Lab, ASU).

Goal:
1. Re-check [[python-ml-wireless]] for current Phase status and shipped artifacts as of today
   (~April 2027). The original roadmap targeted these artifacts by now:
     - M4: O'Shea-Hoydis 2017 autoencoder reproduction
     - M5-M6: RadioML modulation classifier
     - M7: CsiNet / CRNet / CLNet CSI feedback variant
     - M7-M8: Sionna neural receiver reproduction
     - M9-M11: DeepMIMO channel-estimation OR DeepSense beam-prediction experiment
   Audit which actually shipped to GitHub with W&B run links. Be honest — if the portfolio
   isn't ready, that's the report, NOT an email. The [[alkhateeb]] page rule is explicit:
   do NOT send until at least one LWM / DeepMIMO / Sionna repo is live.

2. If portfolio is ready, draft the cold email:
   - Recipient: Professor Ahmed Alkhateeb, Wireless Intelligence Lab, ASU
   - Primary ask: Fall 2028 PhD admission interest
   - Sub-ask (if appropriate): summer 2027 engagement
   - Anchor in actually-shipped repos (not planned). One concrete artifact = one paragraph.
   - Cite a specific recent (2026-2027) Alkhateeb-group paper. Pull current publications via
     WebFetch on https://www.wi-lab.net/publications/ and https://arxiv.org/a/alkhateeb_a_1.html.
     Pick ONE paper that connects to a shipped portfolio artifact — do not generic-cite the
     whole lab.
   - Length: under 200 words. Subject line specific (not 'Research opportunity'). Three
     paragraphs: who+why-this-lab, what-I-bring (anchored in shipped artifacts with links),
     the ask (PhD + optional summer + dates + offer to send CV).
   - Tone: senior-PI calibrated. No filler ('I am passionate about...'). No mentorship-in-
     lieu-of-position. No 4-page CV attachment — link a one-page PDF or LinkedIn instead.

3. Output channel:
   - Use the Gmail MCP connector (connector_uuid 856ce64a-293a-4302-ba92-d13cf5031eda) to
     create a Gmail DRAFT (not sent) addressed to Alkhateeb. Use the
     mcp__claude_ai_Gmail__create_draft tool. Look up his current ASU email via WebFetch on
     https://search.asu.edu/profile/2356896 if not already in [[alkhateeb]].
   - ALSO file a markdown copy of the draft to wiki/summaries/daily-YYYY-MM-DD-alkhateeb-
     email-draft.md so Jayden has it in the wiki, with a short rationale section explaining
     paper-cite choice and which shipped artifacts anchored each paragraph.
   - Append to log.md a one-line entry: '## [YYYY-MM-DD] query | Wi-Lab cold email draft —
     Alkhateeb (auto-fired routine)'.

4. If portfolio audit fails (no LWM/DeepMIMO/Sionna repo shipped):
   - Do NOT draft an email. Do NOT create a Gmail draft.
   - Instead, write a one-page status report to wiki/summaries/daily-YYYY-MM-DD-alkhateeb-
     email-DEFERRED.md with: which milestones slipped, which 1-2 milestones to ship in the
     next 4-6 weeks to unblock the email, a concrete one-week ship plan, and a re-fire date
     (4-8 weeks out). Append to log.md.

Reproducibility / sim-to-real / baseline rules from the persona apply. Wiki-first: read
[[python-ml-wireless]], [[alkhateeb]], [[deepmimo]], [[deepsense-6g]], [[large-wireless-model]],
[[sionna]] before drafting.

Format the email per the global response style (LaTeX for any math, bold for the headline
ask sentence, no em-dash filler). Show the email at the end of the response so Jayden can
review the Gmail draft against the wiki copy.
```

## Re-fire checklist (when Jayden says "ship it")

- [ ] Confirm fire date and convert to UTC (Phoenix is UTC-7 year-round, no DST).
- [ ] Generate a fresh lowercase v4 UUID for `events[].data.uuid`.
- [ ] Verify Gmail connector is still connected at https://claude.ai/customize/connectors. If disconnected, reconnect first or strip the `mcp_connections` block (the agent will fall back to the markdown-only file in `wiki/summaries/`).
- [ ] Confirm `https://github.com/le21-j/second-brain` is still the right repo (it is unless Jayden migrates the wiki).
- [ ] Paste body into `RemoteTrigger create`.
- [ ] Save the returned `trigger_id` here for traceability.

## TL;DR

Locked: name + model (Opus 4.7) + repo + tools + Gmail connector + the full prompt. Pending: only the `run_once_at` timestamp. Drop in the fire date when ready and the routine spins up in seconds.

## Related

- [[alkhateeb]] — recipient page; "no email before live LWM/DeepMIMO/Sionna repo" rule
- [[python-ml-wireless]] — the 14-month roadmap; current Phase governs whether the email is sendable
- [[wireless-intelligence-lab]] — the lab itself
- [[deepmimo]], [[deepsense-6g]], [[large-wireless-model]], [[sionna]] — the infrastructure the email must anchor in
- [[hoydis]], [[morais]] — NVIDIA-side context for the dual-target framing if relevant
