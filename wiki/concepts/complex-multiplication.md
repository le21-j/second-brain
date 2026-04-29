---
title: Complex Multiplication (4 MULTs, 2 ADDs)
type: concept
course: [[eee-404]]
tags: [complex, arithmetic]
sources: [[slides-fft-implementation]]
created: 2026-04-21
updated: 2026-04-26
---

# Complex Multiplication

## In one line
$(a + jb)(c + jd) = (ac - bd) + j(ad + bc)$ — **4 real MULTs, 2 real ADDs**.

## Derivation
$(a + jb)(c + jd) = ac + j\cdot ad + j\cdot bc + j^2\cdot bd = ac + j\cdot ad + j\cdot bc - bd$
$= $ **$(ac - bd) + j(ad + bc)$**

## In code
```c
temp.re = U.re * X[k].re - U.im * X[k].im;   // real part
temp.im = U.re * X[k].im + U.im * X[k].re;   // imaginary part
```

## Why "4 MULTs, 2 ADDs" matters for FFT counting
Complexity analysis in the slides says "$1$ CMULT $= 4$ MULTs $+ 2$ ADDs" — that's this formula. When a question asks "how many real multiplications does an $N$-point FFT need?", the answer is $4 \times $ (number of complex multiplies).

- $N$-point FFT: $(N/2)\cdot\log_2 N$ complex MULTs $\to$ **$2N\cdot\log_2 N$ real MULTs**.
- Example: $N = 64 \to 2\cdot 64\cdot 6 = $ **$768$** real MULTs.

## Known trick (not used in this course)
**Karatsuba-style** complex multiply: 3 MULTs + 5 ADDs. Compute $k_1 = c\cdot(a+b)$, $k_2 = a\cdot(d-c)$, $k_3 = b\cdot(c+d)$, then $\mathrm{Re} = k_1 - k_3$, $\mathrm{Im} = k_1 + k_2$. Sometimes used on hardware where MULTs cost more than ADDs. **Lab 7 uses the standard 4-MULT form** — stick with it.

## Related
- [[butterfly]] — uses complex multiply
- [[twiddle-factor]]
