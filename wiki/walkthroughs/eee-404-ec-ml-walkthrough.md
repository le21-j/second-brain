---
title: EEE 404 Extra-Credit Lab — Neural Network Training (XOR-XOR) — Walkthrough + Report Skeleton
type: example
course: [[eee-404]]
tags: [eee-404, lab, extra-credit, walkthrough, neural-network, mlp, embedded-ml, stm32, training, backpropagation]
sources: [[summary-eee-404-ec-ml-lab]]
created: 2026-04-29
updated: 2026-04-29
---

# EEE 404 Extra-Credit Lab: Neural Network Training — Walkthrough

> [!note] **What this is.** A per-section walkthrough of the **Extra Credit Lab on Machine Learning** (`raw/labs/eee-404/ec-ml-lab_machine_learning.pdf`). It (a) explains the concept being tested, (b) shows the exact code modifications you need to make, (c) tells you what to capture for the report, and (d) ends with a **fill-in-the-blanks report skeleton** in the standard Lab/Project Report Template format.
>
> **Lab is worth 10 extra credit points. Due 2026-05-02 06:59 UTC** (Friday morning).
> **Hardware:** STM32F407G-DISC1 + USB cable.
> **Provided code:** `main.c`, `embeddedML.c`, `embeddedML.h` (in `raw/labs/eee-404/ec-ml-code/code/`).

> [!tip] **The headline modification.** The provided code trains the NN to implement **XOR-AND** (Out1 = X1⊕X2, Out2 = X2·X3). You need to modify it to implement **XOR-XOR** (Out1 = X1⊕X2, Out2 = X2⊕X3). The change is **exactly two functions** in `main.c`: the training-data generator `generate_xorand` and the test-cases block at the end of `main()`. **No changes to `embeddedML.c` or `embeddedML.h`.**

---

## Section I — Network topology (review only, no code change)

> **Topology.** 3 input neurons → 9 hidden neurons (ReLU) → 6 output neurons (ReLU).
> **Parameters.** $3 \times 9 + 9 \times 6 = 27 + 54 = \mathbf{81\ \text{weights}}$ and $9 + 6 = \mathbf{15\ \text{biases}}$.

### The concept

Same MLP forward-pass math as Exam 2 Problem 1 — see [[mlp]] and [[neuron]]:
$$\text{neuron output} = f\!\left(\sum_{j} w_j x_j + b\right), \quad f = \text{ReLU}$$

Now in this lab the network also **trains** itself via backpropagation, which is supplied by the EmbeddedML library:

- `train_ann(net, x, y)` — one forward pass + one backward pass (gradient descent on weights and biases). See [[backpropagation]].
- `run_ann(net, x)` — forward pass only (no weight update). Used to *test* the trained network.
- `init_ann(net)` — set up internal allocation tables.

You don't have to derive backprop here — the library handles it. But understand the loop:

```
for epoch in 0 .. 1999:
    pick a random one of 8 input patterns
    train_ann(net, x, y)             # one gradient step
    if epoch % 200 == 0:
        run all 8 patterns through run_ann, sum MSE → net_error_epoch
```

After ~2000 epochs the `net_error_epoch` should be small (< 0.05 typical), confirming the NN has learned the truth table.

---

## Section II — Understand the existing XOR-AND code (read-only)

Open `main.c`. Find these three regions — they are the only parts you'll modify:

### Region A — `generate_xorand(x, y, i)` (lines 60–144)

Picks a random integer $k \in \{0..7\}$, then outputs the input/output pattern for row $k$ of the truth table. **For XOR-AND** the table is:

| $X_1$ | $X_2$ | $X_3$ | Out1 = $X_1 \oplus X_2$ | Out2 = $X_2 \cdot X_3$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 |

The remaining four output neurons (`y[2]`..`y[5]`) are pinned to 0.0 (we only use 2 of the 6 output neurons).

### Region B — Hyperparameters (lines 248–253 of main.c)

```c
net.eta = 0.05;     // Learning rate
net.beta = 0.01;    // Bias learning rate
net.alpha = 0.25;   // Momentum coefficient
net.output_activation_function = &relu;
net.hidden_activation_function = &relu;
```

For XOR-XOR these defaults work. **Don't change** unless training fails to converge.

### Region C — Test cases at end of `main()` (lines 271–365)

This block runs all 8 input combinations through `run_ann` and accumulates the mean-squared error in `net_error_epoch`. The expected `ground_truth[0], ground_truth[1]` for each `xN` is hard-coded — you'll edit these to match the new XOR-XOR truth table.

---

## Section III — The XOR-XOR modification (THIS IS THE EXERCISE)

> **New target system.** Out1 = $X_1 \oplus X_2$ (same as before), Out2 = $X_2 \oplus X_3$ (CHANGED from $X_2 \cdot X_3$).

### Step 1 — Update the truth table

| $X_1$ | $X_2$ | $X_3$ | Out1 = $X_1 \oplus X_2$ | Out2 = $X_2 \oplus X_3$ | Same as XOR-AND? |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | **0** | ✓ |
| 0 | 0 | 1 | 0 | **1** | (was 0) |
| 0 | 1 | 0 | 1 | **1** | (was 0) |
| 0 | 1 | 1 | 1 | **0** | (was 1) |
| 1 | 0 | 0 | 1 | **0** | ✓ |
| 1 | 0 | 1 | 1 | **1** | (was 0) |
| 1 | 1 | 0 | 0 | **1** | (was 0) |
| 1 | 1 | 1 | 0 | **0** | (was 1) |

> [!tip] **Out1 column is identical** in both tables — only **Out2** changes. So your edits all touch `y[1]` (in `generate_xorand`) or `ground_truth[1]` (in the test cases). `y[0]` and `ground_truth[0]` lines stay exactly the same.

### Step 2 — Modify `generate_xorand` (rename it `generate_xorxor` for clarity)

> [!example] **Diff: lines 60–144 of main.c.**
>
> Only the `y[1]` value changes per case. Below is the full updated function — copy it in.
>
> ```c
> void generate_xorxor(float *x, float *y, int i) {
>     int k = rand() % 8;
>
>     switch (k) {
>     case 0:                    // X1=0, X2=0, X3=0
>         x[0] = 0.0; x[1] = 0.0; x[2] = 0.0;
>         y[0] = 0.0;            // X1 XOR X2 = 0
>         y[1] = 0.0;            // X2 XOR X3 = 0  (unchanged)
>         break;
>     case 1:                    // X1=0, X2=0, X3=1
>         x[0] = 0.0; x[1] = 0.0; x[2] = 1.0;
>         y[0] = 0.0;            // X1 XOR X2 = 0
>         y[1] = 1.0;            // X2 XOR X3 = 1  (was 0 in XOR-AND)
>         break;
>     case 2:                    // X1=0, X2=1, X3=0
>         x[0] = 0.0; x[1] = 1.0; x[2] = 0.0;
>         y[0] = 1.0;            // X1 XOR X2 = 1
>         y[1] = 1.0;            // X2 XOR X3 = 1  (was 0 in XOR-AND)
>         break;
>     case 3:                    // X1=0, X2=1, X3=1
>         x[0] = 0.0; x[1] = 1.0; x[2] = 1.0;
>         y[0] = 1.0;            // X1 XOR X2 = 1
>         y[1] = 0.0;            // X2 XOR X3 = 0  (was 1 in XOR-AND)
>         break;
>     case 4:                    // X1=1, X2=0, X3=0
>         x[0] = 1.0; x[1] = 0.0; x[2] = 0.0;
>         y[0] = 1.0;            // X1 XOR X2 = 1
>         y[1] = 0.0;            // X2 XOR X3 = 0  (unchanged)
>         break;
>     case 5:                    // X1=1, X2=0, X3=1
>         x[0] = 1.0; x[1] = 0.0; x[2] = 1.0;
>         y[0] = 1.0;            // X1 XOR X2 = 1
>         y[1] = 1.0;            // X2 XOR X3 = 1  (was 0 in XOR-AND)
>         break;
>     case 6:                    // X1=1, X2=1, X3=0
>         x[0] = 1.0; x[1] = 1.0; x[2] = 0.0;
>         y[0] = 0.0;            // X1 XOR X2 = 0
>         y[1] = 1.0;            // X2 XOR X3 = 1  (was 0 in XOR-AND)
>         break;
>     case 7:                    // X1=1, X2=1, X3=1
>         x[0] = 1.0; x[1] = 1.0; x[2] = 1.0;
>         y[0] = 0.0;            // X1 XOR X2 = 0
>         y[1] = 0.0;            // X2 XOR X3 = 0  (was 1 in XOR-AND)
>         break;
>     default:
>         x[0] = 0.0; x[1] = 0.0; x[2] = 0.0;
>         y[0] = 0.0;
>         y[1] = 0.0;
>         break;
>     }
>
>     // Remaining 4 output neurons stay zero (we only use 2 of 6 output neurons)
>     y[2] = 0.0; y[3] = 0.0; y[4] = 0.0; y[5] = 0.0;
> }
> ```

### Step 3 — Update the call inside the training loop (line 294)

> [!example] **Single-line change: line 294.**
> ```c
> // BEFORE:
> generate_xorand(x, y, i);
>
> // AFTER:
> generate_xorxor(x, y, i);
> ```

### Step 4 — Update the test cases at end of `main()` (lines 316–362)

The test block runs each of the 8 inputs through `run_ann` and compares against the ground truth. Only `ground_truth[1]` changes (per the truth table above). Diff:

> [!example] **Diff for the 8 test blocks.** Only `ground_truth[1]` lines that change are flagged; `ground_truth[0]` lines stay the same.
>
> ```c
> // x0 → (0,0,0): ground_truth = (0, 0)
> run_ann(&net, x0);
> ground_truth[0] = 0.0;   // unchanged
> ground_truth[1] = 0.0;   // unchanged
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
>
> // x1 → (0,0,1): ground_truth = (0, 1)   ← was (0, 0)
> run_ann(&net, x1);
> ground_truth[0] = 0.0;
> ground_truth[1] = 1.0;   // CHANGED
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
>
> // x2 → (0,1,0): ground_truth = (1, 1)   ← was (1, 0)
> run_ann(&net, x2);
> ground_truth[0] = 1.0;
> ground_truth[1] = 1.0;   // CHANGED
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
>
> // x3 → (0,1,1): ground_truth = (1, 0)   ← was (1, 1)
> run_ann(&net, x3);
> ground_truth[0] = 1.0;
> ground_truth[1] = 0.0;   // CHANGED
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
>
> // x4 → (1,0,0): ground_truth = (1, 0) — unchanged
> run_ann(&net, x4);
> ground_truth[0] = 1.0;
> ground_truth[1] = 0.0;
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
>
> // x5 → (1,0,1): ground_truth = (1, 1)   ← was (1, 0)
> run_ann(&net, x5);
> ground_truth[0] = 1.0;
> ground_truth[1] = 1.0;   // CHANGED
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
>
> // x6 → (1,1,0): ground_truth = (0, 1)   ← was (0, 0)
> run_ann(&net, x6);
> ground_truth[0] = 0.0;
> ground_truth[1] = 1.0;   // CHANGED
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
>
> // x7 → (1,1,1): ground_truth = (0, 0)   ← was (0, 1)
> run_ann(&net, x7);
> ground_truth[0] = 0.0;
> ground_truth[1] = 0.0;   // CHANGED
> Output_Error(2, &net, ground_truth, &error);
> net_error = net_error + error;
> ```

> [!warning] **Don't forget to update the comments.** The original code says `// x1 XOR x2, x2 AND x3` at line 271. Update to `// X1 XOR X2, X2 XOR X3` so the report graders can see at a glance what system you implemented.

---

## Section IV — Build, run, and capture the screenshot

### Step 1 — Open the project in STM32CubeIDE

If you haven't yet imported the project, follow the standard import flow (`File → Import → Existing Projects into Workspace → root directory of your code`).

### Step 2 — Drop in your modified `main.c`

Replace the file with your new version. Save (`Ctrl+S`).

### Step 3 — Build

`Project → Build Project` (or hammer icon). Confirm **0 errors**. Warnings about implicit conversions for the `1.0` ↔ `1.0f` are OK — they don't break behavior.

### Step 4 — Set up the breakpoint and SWV trace

> [!example] **Where to put the breakpoint.**
> Set a breakpoint at the **first line of `while(1)`** (line 374 in original numbering — the infinite loop after the training loop). When training finishes, execution will halt there with `net_error_epoch` holding the final epoch error.

> [!example] **SWV configuration.**
> 1. `Run → Debug Configurations → STM32 → <your project> Debug → Debugger tab → Serial Wire Viewer (SWV) section: enable.`
> 2. `Window → Show View → SWV → SWV Data Trace Timeline Graph.`
> 3. In the timeline graph dialog, add **two trace expressions**: `i` (the epoch counter) and `net_error_epoch` (the per-epoch error).
> 4. Press the red record button in the SWV panel before pressing **Resume** in the debugger.

### Step 5 — Debug + capture

1. Click **Debug** (the bug icon).
2. Click **Resume** (the green ▶).
3. The MCU runs all 2000 epochs, then halts at your breakpoint.
4. The **Variables** window will show `net_error_epoch ≈ 0.005..0.05` (typical converged value).
5. The **SWV Data Trace Timeline Graph** will show the loss curve decreasing from ~$2$ at epoch 0 to ~$0.01$ by epoch 2000.

> [!example] **Take the screenshot.** On Windows: `Ctrl + Alt + PrtScn` captures the active window. Make sure all three regions are visible and legible:
> - **Source view** showing `while(1)` with breakpoint set
> - **Variables / Expressions panel** showing `net_error_epoch` (highlight in yellow if you can)
> - **SWV Data Trace Timeline Graph** showing both `i` and `net_error_epoch` curves

> [!warning] **Convergence troubleshooting.** If `net_error_epoch` stays > 0.5 after 2000 epochs:
> 1. **Increase `N_EPOCH`** to 5000 (line 36).
> 2. **Lower `eta`** to 0.02 (slower but more stable).
> 3. **Re-seed `rand()`** with `srand(42)` at the top of `main()` to get reproducible results.
>
> XOR is harder than AND because it's not linearly separable — the NN may need more epochs to find the right hidden-layer representation. If it converges sometimes but not always, the **initial weights are unlucky** — re-run.

---

## Section V — What goes in the report (deliverables checklist)

Per the lab PDF (Section VI):

1. **Title + name** at the top.
2. **Screenshot (1)** — IDE window showing breakpoint, `net_error_epoch` value, SWV graph.
3. **Code modifications** — explain the changes briefly + paste the modified portions.

Submit as a **single PDF**.

---

# 📄 Report Skeleton (fill in the blanks Friday)

Copy everything below into a new Word doc / Google Doc, fill in the bracketed blanks, take screenshots where indicated, and export as PDF.

---

> **EEE 404/591 Real Time DSP**
> **Extra Credit Lab: Neural Network Training (XOR-XOR Implementation)**
> **Name:** Jayden Le
> **Date:** _[YYYY-MM-DD]_

## 1. Objective

Modify the provided embedded neural-network code to train an MLP (3 inputs, 9 hidden neurons, 6 output neurons) to implement the **3-input, 2-output XOR-XOR system** ($\text{Out}_1 = X_1 \oplus X_2$, $\text{Out}_2 = X_2 \oplus X_3$) on the STM32F407G-DISC1 board.

## 2. Truth Table for the XOR-XOR System

| $X_1$ | $X_2$ | $X_3$ | $\text{Out}_1 = X_1 \oplus X_2$ | $\text{Out}_2 = X_2 \oplus X_3$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 |

## 3. Code Modifications

I made changes in **two regions of `main.c`**: the training-data generator (renamed `generate_xorxor`) and the test cases at the end of `main()`. The library (`embeddedML.c`/`.h`) was unchanged.

### 3.1 Renamed `generate_xorand` → `generate_xorxor` and updated `y[1]` per case

Out1 ($X_1 \oplus X_2$) was identical between XOR-AND and XOR-XOR, so I left every `y[0]` line unchanged. Only `y[1]` (which was previously $X_2 \cdot X_3$) had to be replaced with $X_2 \oplus X_3$ values for each of the 8 cases.

```c
void generate_xorxor(float *x, float *y, int i) {
    int k = rand() % 8;
    switch (k) {
    case 0:  x[0]=0; x[1]=0; x[2]=0;  y[0]=0; y[1]=0;  break;
    case 1:  x[0]=0; x[1]=0; x[2]=1;  y[0]=0; y[1]=1;  break;  // y[1] CHANGED
    case 2:  x[0]=0; x[1]=1; x[2]=0;  y[0]=1; y[1]=1;  break;  // y[1] CHANGED
    case 3:  x[0]=0; x[1]=1; x[2]=1;  y[0]=1; y[1]=0;  break;  // y[1] CHANGED
    case 4:  x[0]=1; x[1]=0; x[2]=0;  y[0]=1; y[1]=0;  break;
    case 5:  x[0]=1; x[1]=0; x[2]=1;  y[0]=1; y[1]=1;  break;  // y[1] CHANGED
    case 6:  x[0]=1; x[1]=1; x[2]=0;  y[0]=0; y[1]=1;  break;  // y[1] CHANGED
    case 7:  x[0]=1; x[1]=1; x[2]=1;  y[0]=0; y[1]=0;  break;  // y[1] CHANGED
    default: x[0]=0; x[1]=0; x[2]=0;  y[0]=0; y[1]=0;  break;
    }
    y[2]=0; y[3]=0; y[4]=0; y[5]=0;
}
```

The function call in the training loop was also updated:

```c
generate_xorxor(x, y, i);   // was generate_xorand(x, y, i);
```

### 3.2 Updated test ground-truth values for the 8 input patterns

```c
// x0 → (0,0,0): truth = (0, 0)   [unchanged]
// x1 → (0,0,1): truth = (0, 1)   [y[1] CHANGED from 0 to 1]
// x2 → (0,1,0): truth = (1, 1)   [y[1] CHANGED from 0 to 1]
// x3 → (0,1,1): truth = (1, 0)   [y[1] CHANGED from 1 to 0]
// x4 → (1,0,0): truth = (1, 0)   [unchanged]
// x5 → (1,0,1): truth = (1, 1)   [y[1] CHANGED from 0 to 1]
// x6 → (1,1,0): truth = (0, 1)   [y[1] CHANGED from 0 to 1]
// x7 → (1,1,1): truth = (0, 0)   [y[1] CHANGED from 1 to 0]

run_ann(&net, x0); ground_truth[0] = 0.0; ground_truth[1] = 0.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
run_ann(&net, x1); ground_truth[0] = 0.0; ground_truth[1] = 1.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
run_ann(&net, x2); ground_truth[0] = 1.0; ground_truth[1] = 1.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
run_ann(&net, x3); ground_truth[0] = 1.0; ground_truth[1] = 0.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
run_ann(&net, x4); ground_truth[0] = 1.0; ground_truth[1] = 0.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
run_ann(&net, x5); ground_truth[0] = 1.0; ground_truth[1] = 1.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
run_ann(&net, x6); ground_truth[0] = 0.0; ground_truth[1] = 1.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
run_ann(&net, x7); ground_truth[0] = 0.0; ground_truth[1] = 0.0; Output_Error(2, &net, ground_truth, &error); net_error += error;
```

### 3.3 Hyperparameters (unchanged from the provided code)

```c
net.eta = 0.05;     // Learning rate
net.beta = 0.01;    // Bias learning rate
net.alpha = 0.25;   // Momentum coefficient
net.output_activation_function = &relu;
net.hidden_activation_function = &relu;
```

## 4. Training Result

After 2000 training epochs, the network converged to a final per-epoch error of **`net_error_epoch = ____`** (insert measured value, expect <0.05).

The **SWV Data Trace Timeline Graph** below shows the evolution of the epoch counter `i` and `net_error_epoch` over training. The loss curve decreases monotonically (with some noise from the random epoch sampling), confirming successful training of the XOR-XOR system.

### 4.1 Screenshot

_[INSERT SCREENSHOT HERE — showing source view with breakpoint, Variables window with `net_error_epoch` value highlighted in yellow, and SWV Data Trace Timeline Graph showing both `i` and `net_error_epoch`.]_

## 5. Conclusion

The MLP successfully learned the 3-input, 2-output XOR-XOR system after _[N]_ training epochs. The same network topology that solved XOR-AND (3-9-6 with ReLU, $\eta = 0.05$) also handles XOR-XOR without re-tuning, demonstrating the general-purpose nature of the embedded ML approach. _[Optional 1-2 sentences on what surprised you or what you'd improve.]_

---

> [!tip] **Time budget for this lab.** ~30 min reading the PDF, ~15 min editing `main.c`, ~30 min in STM32CubeIDE setting up debug + SWV, ~10 min capturing the screenshot, ~30 min writing the report. **Total: ~2 hours.** Worth it for 10 EC.

> [!tip] **Why this exercise matters beyond the EC points.** This is your first hands-on encounter with **on-device training** — the network learns *on the STM32* with no PC in the loop. That's a building block for the [[python-ml-wireless]] roadmap: federated learning, edge ML, AirComp neural-receivers. Save this code; you'll come back to it.

## See also

- [[eee-404]] — course page
- [[mlp]], [[neuron]], [[relu]], [[forward-propagation]], [[backpropagation]] — concepts behind this lab
- [[eee-404-exam-2-walkthrough]] — Exam 2 Problem 1 is the same MLP forward-pass math
- [[lab-7-fft]] — companion lab summary; this EC lab is the smaller cousin
