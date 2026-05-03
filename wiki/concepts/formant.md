---
title: Formant
type: concept
course: [[eee-404]]
tags: [eee-404, dsp, speech, vocal-tract, fft, spectral-envelope]
sources: [[lab-eee-404-project-2-fft-applications]]
created: 2026-05-02
updated: 2026-05-02
---

# Formant

## In one line
A **formant** is a resonance peak of the vocal tract — the spectral peaks that make a vowel sound like a vowel.

## Example first
Take the FFT magnitude of you saying "a" (as in *father*) for 1 second at $f_s = 8000$ Hz. The spectrum is **not** a flat line of harmonics — it has bumps. Two big bumps:

| Vowel | $F_1$ (Hz) — first formant | $F_2$ (Hz) — second formant |
|---|---|---|
| "a" (*father*)  | $\sim 750$ | $\sim 1100$ |
| "i" (*see*)     | $\sim 280$ | $\sim 2400$ |
| "u" (*boot*)    | $\sim 320$ | $\sim 800$  |

(Numbers vary 20–40% by speaker — gender, accent, mouth shape. The UCLA chart at <https://linguistics.ucla.edu/people/hayes/103/Charts/VChart/> is a good reference.)

If you read $F_1$ and $F_2$ off your own FFT plot in MATLAB and compare against the table, you can identify which vowel was spoken. That's exactly what the MATLAB scope (or a spectrogram cursor) lets you do in Project 2.

## The idea
Speech is produced by two cascaded systems:

```
glottis (source)  →  vocal tract (filter)  →  lips (radiation)
   |                       |
   pitch f₀                formants F₁, F₂, F₃
   (sets the harmonics)    (shape the envelope)
```

- The **glottal source** vibrates at a fundamental frequency $f_0$ (the pitch — see [[autocorrelation-pitch-detection]]) and produces a harmonic series at $f_0, 2f_0, 3f_0, \dots$
- The **vocal tract** (throat, mouth, tongue, lips) is an acoustic tube whose resonant modes amplify certain frequencies. Those resonant peaks in the magnitude response are the **formants**.

The harmonics from the glottis are filtered by the vocal tract. The peaks you see in the FFT spectrum are not the harmonics themselves; they're harmonics that happen to land near a formant frequency, plus the formant envelope shaping the whole comb.

## Formal definition
If $S(\omega)$ is the glottal source spectrum and $H(\omega)$ is the vocal-tract transfer function, the speech spectrum is

$$X(\omega) = H(\omega)\,S(\omega).$$

The **formants** are the local maxima of $|H(\omega)|$. They are the poles (or near-poles) of an all-pole model of the vocal tract:

$$H(z) = \frac{G}{1 - \sum_{k=1}^{p} a_k\,z^{-k}}.$$

This is the basis of **Linear Predictive Coding (LPC)** — solving for the $a_k$ from a speech window and reading off the formants as the angles of the poles.

## Why it matters / when you use it
- **Vowel identification** — the first 2–3 formants uniquely identify a vowel.
- **Speech synthesis** — formant-based synthesis (Klatt, MITalk) sets formant frequencies directly to produce intelligible speech.
- **Speech coding** — vocoders code the formants (the slowly-varying envelope) separately from the pitch (the fast excitation).
- **Voice biometrics, accent analysis, language ID** — all depend on formant tracks over time.
- **Project 2 (vowel analysis task)** — Jayden reads $F_1$, $F_2$ off the FFT plot for two vowels and fills the deliverable table.

## Common mistakes
- **Confusing formants with harmonics.** Harmonics are spaced at integer multiples of $f_0$ — many narrow spikes. Formants are broader peaks of the **envelope** that shape those harmonics. Looking at a spectrum: the comb teeth are harmonics, the bumps in the envelope are formants.
- **Confusing formants with pitch.** Pitch is one number; formants are several. Two people saying "a" at very different pitches still have nearly the same formants (because their vocal-tract shapes are similar).
- **Formant numbering.** $F_1, F_2, F_3, \dots$ are ordered by frequency — $F_1$ is the lowest formant, regardless of which is loudest in the FFT.
- **Reading the wrong axis.** In a `spectrogram(s, N, ..., fs, 'yaxis')` plot, frequency is on the y-axis (cause of the `'yaxis'` flag); without it, MATLAB puts frequency on the x-axis and time on the y-axis. Project 2's MATLAB script uses `'yaxis'`.

## Related
- [[autocorrelation-pitch-detection]] — pitch is the *other* feature of a vowel.
- [[fft]], [[stft]] — the analysis tools.
- [[window-function]] — windowing widens formant peaks (mainlobe broadening); too wide a window blurs adjacent formants together.

## Practice
- *(could be added — e.g., given a speech FFT, identify which vowel it is from the formant peaks.)*
