---
title: FFT Scaling (Overflow Prevention)
type: concept
course: [[eee-404]]
tags: [fft, fixed-point, overflow]
sources: [[slides-fft-implementation]], [[lab-7-fft]]
created: 2026-04-21
updated: 2026-04-26
---

# FFT Scaling (Overflow Prevention)

## In one line
At every FFT stage, divide the butterfly outputs by 2 to keep values from growing out of range. Multiply the final output by $N$ to get the correct DFT.

## Example first
Say you're running an 8-point fixed-point FFT with Q15 samples in $[-1, 1)$. Input: a pure sinusoid that peaks at $1.0$. After stage 1, the butterfly outputs are sums like $X_e + W\cdot X_o$. A sum of two Q15 numbers can be up to $2.0$ — **overflow**.

Fix: scale each butterfly output by $0.5$. Now after stage 1, max is still $1.0$. Repeat for every stage. After $\log_2 N$ stages, you've accumulated a scale of $(1/2)^{\log_2 N} = $ **$1/N$**. Multiply the final output by $N$ and you've recovered the true DFT.

For $N = 1024$, final multiplier is **$1024$**.

## The idea
The DFT equation $X[k] = \sum x[n]\cdot W^{kn}$ is basically a sum of $N$ values each of magnitude $\leq \max|x[n]|$. So in the worst case $|X[k]|$ can be as large as $N\cdot\max|x[n]|$. Fixed-point arithmetic can't hold values that big without special care.

Per-stage scaling pre-distributes that "growth of $N$" across the $\log_2 N$ stages — instead of one big multiply by $N$ at the end (which would overflow first), you shrink by $1/2$ every stage, then grow by $N$ once at the end after the intermediate sums have collapsed.

## The butterfly with scaling

```c
float scale = (scale_or_not) ? 0.5 : 1.0;
...
P.re = (X[i].re + temp.re) * scale;
P.im = (X[i].im + temp.im) * scale;
Q.re = (X[i].re - temp.re) * scale;
Q.im = (X[i].im - temp.im) * scale;
```

At the end:

```c
if (scale_or_not) {
    X[i].re = X[i].re * SIZE_FFT;
    X[i].im = X[i].im * SIZE_FFT;
}
```

In **fixed-point**, scaling by $0.5$ is just `>> 1` (right shift by 1).

## Why 0.5 exactly?
Because each butterfly is a sum/difference of two values each bounded by $M$. Worst case: $|X[i] + \text{temp}| = 2M$. Dividing by 2 restores the bound to $M$. With scaling, the magnitude never grows across stages.

## Common mistakes
- Forgetting to multiply by $N$ at the end $\to$ your spectrum is off by $1/N$.
- Scaling by $0.5$ in float but also shifting by $1$ in fixed-point (double scaling).
- Turning scaling OFF on large $N$ (like $128$) with real inputs $\to$ overflow, garbage output. The Lab 7 Task 4 question asks you to observe and explain this.

## Why not just use more bits?
You could. But fixed-point multiplies produce double-width results (32-bit $\times$ 32-bit $\to$ 64-bit); juggling 64-bit intermediate values is slower and uses more memory. Per-stage scaling keeps everything in 32-bit and is what DSP code does in practice.

## Related
- [[butterfly]]
- [[fixed-point-arithmetic]]
- [[lab-7-fft]]

## Practice
- [[fft-fundamentals-set-01]] — includes the $1024$-pt scale-recovery question
