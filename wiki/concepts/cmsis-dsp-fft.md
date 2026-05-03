---
title: CMSIS-DSP FFT API (arm_rfft_fast_f32)
type: concept
course: [[eee-404]]
tags: [eee-404, cmsis, fft, real-valued-fft, stm32, embedded, arm]
sources: [[lab-eee-404-project-2-fft-applications]]
created: 2026-05-02
updated: 2026-05-02
---

# CMSIS-DSP FFT API (`arm_rfft_fast_f32`)

## In one line
ARM's CMSIS-DSP library ships an optimized $N$-point real-FFT for Cortex-M; you initialize a struct with a power-of-two length, then call one function for forward or inverse — but the **output is packed in a non-obvious format** that always trips up first-time users.

## Example first
Take a 512-point real signal `X[]` and compute its forward FFT into `Y[]`:

```c
#define ARM_MATH_CM4
#include "arm_math.h"

#define SIZE_FFT 512
arm_rfft_fast_instance_f32 fft_handler;
float32_t X[SIZE_FFT], Y[SIZE_FFT];

// once, near startup:
arm_rfft_fast_init_f32(&fft_handler, SIZE_FFT);

// each time you have a new buffer:
arm_rfft_fast_f32(&fft_handler, X, Y, 0);   // 0 = forward
arm_rfft_fast_f32(&fft_handler, Y, Z, 1);   // 1 = inverse
```

`Y[]` is the same length as `X[]` — but it's not "real part in indices 0..N-1, imaginary part somewhere else." It's packed:

| `Y[i]` index | Value |
|---|---|
| `Y[0]` | $\text{Re}\{Y[0]\}$ — DC |
| `Y[1]` | $\text{Re}\{Y[N/2]\}$ — Nyquist (also real) |
| `Y[2]` | $\text{Re}\{Y[1]\}$ |
| `Y[3]` | $\text{Im}\{Y[1]\}$ |
| `Y[4]` | $\text{Re}\{Y[2]\}$ |
| `Y[5]` | $\text{Im}\{Y[2]\}$ |
| ⋮ | ⋮ |
| `Y[N-2]` | $\text{Re}\{Y[N/2-1]\}$ |
| `Y[N-1]` | $\text{Im}\{Y[N/2-1]\}$ |

So computing $|Y[k]|^2$ for $k \geq 1$ uses pairs:

```c
for (i = 2; i < N; i += 2)
    spectrum[i/2] = Y[i]*Y[i] + Y[i+1]*Y[i+1];   // |Y[i/2]|^2
spectrum[0]   = Y[0]*Y[0];                       // DC
spectrum[N/2] = Y[1]*Y[1];                       // Nyquist
```

That's exactly what the FILL_IN_BLANK on `waverecorder.c:168` is asking for.

## The idea
For a **real-valued** input of length $N$, the FFT has Hermitian symmetry: $Y[N-k] = Y[k]^*$. So bins $N/2+1, \dots, N-1$ are redundant (just conjugates of bins $1, \dots, N/2-1$). That gives you $N$ real-valued storage slots and $N/2 + 1$ complex bins to store. The "+1" matters: bins 0 and $N/2$ are real-only (because $Y[0] = Y[0]^*$ and $Y[N/2] = Y[N/2]^*$), so they fit in two slots, and the remaining $N/2 - 1$ complex bins fit in the other $N - 2$ slots as `(re, im)` pairs. That's the packing.

CMSIS chose this packing so the output buffer is the **same size** as the input — half the memory of a generic complex FFT and a $\sim 2\times$ speedup.

## Formal definition
The forward-FFT call:

```c
arm_status arm_rfft_fast_init_f32(arm_rfft_fast_instance_f32 *S, uint16_t fftLen);
void       arm_rfft_fast_f32(arm_rfft_fast_instance_f32 *S,
                             float32_t *p,    // input  (length fftLen)
                             float32_t *pOut, // output (length fftLen, packed)
                             uint8_t ifftFlag);  // 0 = forward, 1 = inverse
```

`fftLen` must be a power of 2: $\{32, 64, 128, 256, 512, 1024, 2048, 4096\}$.

For the **inverse** transform with `ifftFlag = 1`, the input must be in the same packed format (so you can feed back `Y[]` from a forward transform, or fill it manually as the project does for the autocorrelation step).

CMSIS reference: <https://arm-software.github.io/CMSIS_5/DSP/html/group__RealFFT.html>.

## Why it matters / when you use it
- **STM32F407 + Cortex-M4F** has hardware single-precision floating point (`fpv4-sp-d16`). The CMSIS FFT exploits it and runs $\sim 4 \times$ faster than a generic float FFT compiled from textbook code.
- **Real-time spectrum analyzer** — you need every microsecond. CMSIS gives you the budget for windowing + FFT + magnitude squared + dB conversion + UART transmit inside one audio frame.
- **Project 2** uses `arm_rfft_fast_f32` for both the vowel-analysis task (offline 512-pt) and the spectrum analyzer (real-time 1024-pt).

## Common mistakes
- **Forgetting to call `arm_rfft_fast_init_f32`.** Calling the transform on an uninitialized handler segfaults or returns garbage. The init *must* run once before any forward/inverse transform — that is exactly the FILL_IN_BLANK on `audio_spectrum_analyzer/main.c:109`.
- **Initializing inside the audio interrupt.** The init allocates / sets up tables. Run it once, in `main()`, **before** enabling the audio DMA/interrupts. Otherwise the handler might fire mid-init.
- **Forgetting the packed format and indexing `Y[k]` as if it were a normal complex array.** It isn't. `Y[1]` is *not* `Re{Y[1]}` — it's `Re{Y[N/2]}`. Mis-indexing here is the most common project-2 bug.
- **Treating the inverse as scaled.** CMSIS's inverse already includes the $1/N$ factor — don't divide again. (For forward transforms, **no** scaling is applied; magnitudes grow with $N$.) See [[fft-scaling]].
- **Wrong precision.** There's also `arm_rfft_q15`, `arm_rfft_q31` for fixed-point. Project 2 uses **f32** (float32). Don't mix.

## Related
- [[real-valued-fft]] — the math the packing exploits.
- [[fft]], [[fft-scaling]], [[bit-reversed-order]] — FFT basics.
- [[stft]] — the sliding-window pipeline that consumes this API.
- [[lab-7-fft]] — Lab 7 builds an FFT from scratch; Project 2 uses CMSIS to skip that.

## Practice
- *(could add — call `arm_rfft_fast_f32` on a synthetic single-sinusoid input, predict which packed slot the peak lands in, verify.)*
