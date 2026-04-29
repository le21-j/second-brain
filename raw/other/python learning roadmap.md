# The physical-layer ML roadmap: 14 months to NVIDIA and Wi-Lab

**Your path is clearer than you think.** The two targets you named — NVIDIA's Sionna team and Prof. Ahmed Alkhateeb's Wi-Lab at ASU — are the two most tightly coupled research programs in physical-layer ML today: **DeepMIMO integrates directly with NVIDIA Sionna RT and the Aerial Omniverse Digital Twin**, and João Morais (Alkhateeb PhD 2025) is now a Wireless Software Engineer at NVIDIA. This means every hour spent on Sionna-plus-DeepMIMO pays double. With a junior's DSP/wireless foundation and 20+ hours/week, the realistic outcome over 14 months is: **6 polished GitHub repos, 1–2 arXiv preprints, a Sionna contribution merged, a DeepSense 6G Challenge submission, and a warm introduction to Alkhateeb before your PhD application opens.** The rest of this document is the concrete execution plan, organized for direct action.

A candid note on the NVIDIA internship: **NVIDIA Research internships target PhD students**; a junior applying for Summer 2027 should target the **regular BS-level ML/SWE internships** (portal opens Aug–Oct 2026) and use Sionna contributions + a direct email to Hoydis/Cammerer/Aït Aoudia as the lever to be considered for a research-adjacent project. This is achievable but requires the portfolio to be real by September 2026.

---

## 1. How to read this roadmap

The 14-month plan is structured in five phases running from May 2026 through June 2027. Each phase has specific deliverables, a primary study track, and a portfolio artifact. At any given time you should be doing three things in parallel: **(1) structured coursework**, **(2) a shipping project**, and **(3) paper reading** (one paper per week minimum, logged in a notes repo). Never let any one of these stall the other two.

Throughout, use this canonical toolchain: **Python 3.11+, VS Code or Cursor, JupyterLab, uv or conda for envs, Git + GitHub, PyTorch + Lightning as primary, TensorFlow/Keras as working knowledge for legacy Sionna code, Weights & Biases for experiment tracking, Hydra for configs, ruff + black + pre-commit, and Google Colab or Kaggle Kernels for GPU**. All experiments logged in W&B; all code in reproducible repos with Hydra configs and a results table in the README.

---

## 2. Python learning path (scientific computing and ML)

### Fundamentals (weeks 1–2)

**Primary course: CS50P — Harvard's Introduction to Programming with Python** (https://cs50.harvard.edu/python/). Ten weekly problem sets, in-browser grading, strong emphasis on testing and debugging from day one. Compressible to 3–4 weeks at your pace. Supplement with **Corey Schafer's Python tutorials on YouTube** (https://www.youtube.com/c/Coreyms) for decorators, generators, context managers, virtual environments, and OOP — these are the intermediate topics CS50P touches lightly.

For a book companion, **"Python Crash Course" (3rd ed.) by Eric Matthes** is the fastest on-ramp; **"Automate the Boring Stuff with Python" by Al Sweigart** is free at https://automatetheboringstuff.com/ and excellent for building early momentum. Once you're past basics, **"Fluent Python" (2nd ed.) by Luciano Ramalho** is the definitive intermediate/advanced text — return to it in Month 2. Practice daily with **Exercism's Python track** (https://exercism.org/tracks/python), which offers mentored code review.

### Scientific Python stack (weeks 3–4)

**NumPy is the single most important library** for your research. Start with the official NumPy Absolute Beginners tutorial, then **Nicolas Rougier's "From Python to NumPy"** (https://www.labri.fr/perso/nrougier/from-python-to-numpy/) — the best free resource focused on vectorization, which is exactly the skill you need for DSP and ML prototyping. Drill with **Rougier's 100 NumPy Exercises** (https://github.com/rougier/numpy-100); aim for all one-star and two-thirds of two-star exercises. Stanford CS231n's Python/NumPy tutorial (https://cs231n.github.io/python-numpy-tutorial/) covers 80% of what you'll use in one dense hour.

For SciPy, work through the **scipy.signal and scipy.fft tutorials** at https://docs.scipy.org/doc/scipy/tutorial/signal.html — essential for your DSP background. Master the functions `firwin`, `iirfilter`, `butter`, `lfilter`, `filtfilt`, `freqz`, `sosfilt`, `welch`, `resample_poly`, `hilbert`, `chirp`, `correlate`, `convolve`. The absolute highest-value domain resource is **PySDR by Marc Lichtman** (https://pysdr.org/) — a free online textbook covering sampling, FFT, filtering, modulation, OFDM, pulse shaping, synchronization, and a dedicated ML-for-RF chapter. This is the single most wireless-relevant free resource anywhere.

For plotting, **"Scientific Visualization: Python + Matplotlib" by Nicolas Rougier** (https://github.com/rougier/scientific-visualization-book) is the open-access gold standard — you will need publication-quality figures for your papers. For pandas, the official 10-minutes-to-pandas plus Wes McKinney's free book (https://wesmckinney.com/book/) are sufficient.

### PyTorch (weeks 5–8)

PyTorch is your primary framework. Start with the **official 60 Minute Blitz** (https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html), then the **"Learn PyTorch for Deep Learning" free online book by Daniel Bourke** (https://www.learnpytorch.io/). For depth, **"Deep Learning with PyTorch" by Stevens, Antiga, and Viehmann** is available as a free PDF from Manning via form — chapters 1–8 explain PyTorch internals (tensors, storage, strides, autograd) better than any other source. **Sebastian Raschka's "PyTorch in One Hour"** (https://sebastianraschka.com/teaching/pytorch-1h/) is an excellent dense refresher, and his book **"Machine Learning with PyTorch and Scikit-Learn"** (code free at https://github.com/rasbt/machine-learning-book) bridges sklearn fluency to PyTorch.

For architecture-specific tutorials: **Andrej Karpathy's "Neural Networks: Zero to Hero" playlist** (https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) and his **"Let's build GPT from scratch"** video are the highest-ROI deep-learning content anywhere — do the entire playlist. Add **"The Annotated Transformer"** (http://nlp.seas.harvard.edu/annotated-transformer/) and **nanoGPT** (https://github.com/karpathy/nanoGPT). For autoencoders, reference **PyTorch-VAE** (https://github.com/AntixK/PyTorch-VAE). Adopt **PyTorch Lightning** (https://lightning.ai/docs/pytorch/) once you're writing real training loops.

### TensorFlow (working knowledge — week 10)

Sionna 2.x has migrated to PyTorch, but Sionna 1.x and a large body of existing research code remain TensorFlow-based, so you need working competence, not deep expertise. Focus on: `tf.keras.layers.Layer` subclassing (this is how every Sionna block is written), `@tf.function` and AutoGraph, `tf.GradientTape` for custom training loops, and basic `tf.data.Dataset` pipelines. The official TensorFlow beginner quickstart and the Keras guide **"Making new layers and models via subclassing"** are the critical reads. Budget ~25–35 hours total. If you have money to spend, **Chollet's "Deep Learning with Python" (2nd ed.)** is the authoritative source — chapters 3, 7, and 9 cover exactly what you need for Sionna.

### Software engineering best practices (ongoing from week 1)

**Git and GitHub**: read chapters 1–3 and 6 of **"Pro Git"** (free at https://git-scm.com/book/en/v2); reinforce with **"Learn Git Branching"** (https://learngitbranching.js.org/) and **Oh My Git!** (https://ohmygit.org/). For environments, use **uv** (https://docs.astral.sh/uv/) as your default — it's 10–100× faster than pip — and **conda/Miniconda** when you need CUDA/GPU toolchain bundling. Testing: **pytest** plus **Hypothesis** for property-based tests (try "IFFT(FFT(x)) ≈ x" as your first property). Code quality: **ruff** as primary linter/formatter, **pre-commit** hooks, optional **mypy** for type checking. Reproducibility stack: **Weights & Biases** (free for academic use; https://wandb.ai/), **Hydra** (https://hydra.cc/) for configs, **DVC** (https://dvc.org/) for dataset versioning. Use the **Lightning-Hydra-Template** (https://github.com/ashleve/lightning-hydra-template) as a starting point for every serious project.

### Wireless/DSP-specific Python libraries

Beyond scipy.signal, master these: **CommPy** (https://github.com/veeresht/CommPy) for classical coding/modulation in pure NumPy, **Komm** (https://komm.dev/) as a cleaner modern alternative, **TorchSig** (https://torchsig.com/) for PyTorch-native RF signals with pretrained models, **julius** and **TorchFX** for GPU-accelerated differentiable DSP, and **GNU Radio** Python bindings (https://wiki.gnuradio.org/) when you graduate to SDR hardware. **Sionna itself** is the centerpiece — see Section 5.

---

## 3. Machine learning and deep learning foundations

Your DSP background is a major asset: Karhunen-Loève is PCA, Kalman filtering is a linear-Gaussian state-space model (Bishop PRML Ch 13), belief propagation is sum-product on factor graphs, and regularized least squares is ridge regression. Lean into this connection — it will let you skip some introductory material that CS students need.

### Classical ML (Month 1 of Phase 1)

**Primary course: Andrew Ng's Machine Learning Specialization** (https://www.coursera.org/specializations/machine-learning-introduction), the 2022 DeepLearning.AI rebuild in Python. Three courses covering supervised learning, advanced learning algorithms (NNs, trees, XGBoost), and unsupervised learning plus RL intro. Follow with **Stanford CS229 (2018 Autumn)** on YouTube (https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) for rigor — for you, lectures 2–10, 14–15, and 17–20 are priority. Use **StatQuest with Josh Starmer** (https://www.youtube.com/@statquest) as just-in-time intuition.

Primary textbook: **ISLP — "An Introduction to Statistical Learning with Applications in Python"** (free PDF at https://hastie.su.domains/ISLP/ISLP_website.pdf). Read chapters 2–10 and 12. For deeper probabilistic grounding, **Bishop's "Pattern Recognition and Machine Learning"** is your most valuable reference: prioritize chapters 1–4 (decision theory, Gaussians, Bayesian linear regression = MMSE estimator), 6 (kernel methods and Gaussian processes), 8 (graphical models — directly used in iterative decoding), 9–11 (EM, variational inference, MCMC), and especially **chapter 13 (sequential data, HMMs, Kalman filters)**. **Kevin Murphy's "Probabilistic Machine Learning: An Introduction"** (free at https://probml.github.io/pml-book/) is the modern encyclopedic replacement — use it as reference, not a linear read.

### Deep learning (Month 2–3 of Phase 1 and into Phase 2)

**Andrew Ng's Deep Learning Specialization** (https://www.coursera.org/specializations/deep-learning) — 5 courses, do in order. Course 3 (Structuring ML Projects) is underrated and teaches you how to do research well. Supplement with **Stanford CS231n** (https://cs231n.stanford.edu/) — CNNs for Visual Recognition is directly relevant to wireless because CSI matrices, spectrograms, and constellation diagrams are all 2D "images." **Do assignment 2 fully** (BatchNorm, Dropout, ConvNets in NumPy+PyTorch); it's the single best exercise for your research goal. **MIT 6.S191** (http://introtodeeplearning.com/) offers a fast up-to-date overview, and **NYU Deep Learning (DS-GA 1008) by LeCun and Canziani** (https://atcold.github.io/NYU-DLSP20/) covers energy-based and self-supervised models useful for unsupervised channel representation learning.

Primary textbook: **Simon Prince, "Understanding Deep Learning"** (free at https://udlbook.github.io/udlbook/) — the modern successor to Goodfellow et al., with the best pedagogical figures available. This is your main DL book. **"Dive into Deep Learning"** (https://d2l.ai/) is the best code-first companion — read the concept in Prince, run the code in d2l. **Goodfellow/Bengio/Courville** (https://www.deeplearningbook.org/) remains valuable as theoretical reference, especially chapters 5–10, 14–15.

### Key architectures, in priority order

For **CNNs**, CS231n is definitive. Read the foundational papers in arXiv chronological order: LeNet-5, AlexNet, VGG, ResNet (arxiv:1512.03385), DenseNet, MobileNetV2, EfficientNet, ConvNeXt. For **transformers**, do Karpathy's "Let's build GPT" (https://www.youtube.com/watch?v=kCc8FmEb1nY), read Jay Alammar's **"Illustrated Transformer"** (https://jalammar.github.io/illustrated-transformer/), then the original paper. For **VAEs**, read Kingma & Welling "Auto-Encoding Variational Bayes" (arxiv:1312.6114) and Lilian Weng's blog post (https://lilianweng.github.io/posts/2018-08-12-vae/). For **GANs**, read Goodfellow 2014 and skim DCGAN/WGAN-GP. For **diffusion models**, Lilian Weng's post (https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) plus Hugging Face's Diffusion Course (https://huggingface.co/learn/diffusion-course). For **GNNs** — highly relevant for wireless networks as graphs — take **Stanford CS224W** (https://web.stanford.edu/class/cs224w/).

### Reinforcement learning (Phase 2)

RL is essential for beam management, power control, and link adaptation. **Primary textbook: Sutton & Barto "Reinforcement Learning: An Introduction" (2nd ed.)** — free at http://incompleteideas.net/book/the-book-2nd.html. Read chapters 1–8 (tabular), 9–11 (approximate), 13 (policy gradient). Pair with **David Silver's DeepMind/UCL RL course** on YouTube. For hands-on, **Hugging Face Deep RL Course** (https://huggingface.co/learn/deep-rl-course/) and **OpenAI Spinning Up** (https://spinningup.openai.com/) plus **CleanRL** (https://github.com/vwxyzjn/cleanrl) for reproducible single-file reference implementations. Master in order: tabular Q-learning, DQN, REINFORCE, PPO, SAC.

### Math refreshers

Your DSP background covers most of what you need. Fill ML-specific gaps with: **Parr & Howard "The Matrix Calculus You Need For Deep Learning"** (https://explained.ai/matrix-calculus/) in one sitting; **3Blue1Brown's Neural Networks playlist** including the new attention/transformer chapters; **MacKay's "Information Theory, Inference, and Learning Algorithms"** (free at https://www.inference.org.uk/mackay/itila/book.html) — chapters 47–50 on LDPC/turbo/fountain codes are especially valuable; and **Boyd & Vandenberghe "Convex Optimization"** (free at https://stanford.edu/~boyd/cvxbook/) for chapters 1–5.

### Hands-on platforms

**Kaggle** for micro-courses at https://www.kaggle.com/learn and free GPU kernels. **Hugging Face** for the LLM, Deep RL, Diffusion, Audio, and Computer Vision courses. **Papers with Code** (https://paperswithcode.com/) for paper implementations. **Google Colab** free T4 GPUs to start. **Weights & Biases** for all experiment tracking.

---

## 4. The wireless+ML specialization — your core differentiator

This is the section that separates serious applicants from generic ML students. You need to know both the canonical ComSoc Best Readings and the active research fronts at your two target labs.

### ComSoc Best Readings — organized by subtopic

The IEEE ComSoc Best Readings page (https://www.comsoc.org/publications/best-readings/machine-learning-communications) is organized into eight sections: Signal Detection, Channel Encoding/Decoding, Channel Estimation/Prediction/Compression, End-to-End/Semantic Communications, Resource Allocation, Distributed/Federated Learning, Standardization, and Selected Topics.

**Foundational tutorials and surveys** start with **O'Shea & Hoydis, "An Introduction to Deep Learning for the Physical Layer,"** IEEE TCCN 2017 (arxiv:1702.00832) — the seminal autoencoder-based PHY paper and the starting point for everything downstream. Add **Arulkumaran et al. "Deep Reinforcement Learning: A Brief Survey,"** IEEE SPM 2017; **Wang, Di Renzo, Stanczak, Wang, Larsson, "AI-Enabled Wireless Networking for 5G and Beyond,"** IEEE WC 2020; and **Simeone, "A Brief Introduction to Machine Learning for Engineers,"** Foundations and Trends 2018 (arxiv:1802.05374).

**Deep learning for channel estimation** includes the canonical works: **He, Wen, Jin, Li, "Deep Learning-Based Channel Estimation for Beamspace mmWave Massive MIMO"** (arxiv:1802.01290); **Neumann, Wiese, Utschick, "Learning the MMSE Channel Estimator,"** IEEE TSP 2018; and **Hu, Gao, Zhang, Jin, Li, "Deep Learning for Channel Estimation: Interpretation, Performance, and Comparison,"** IEEE TWC 2021 (arxiv:1911.01918).

**Autoencoder / end-to-end learning** — the O'Shea/Hoydis thread: **Dörner, Cammerer, Hoydis, ten Brink, "Deep Learning-Based Communication over the Air,"** IEEE JSTSP 2018 (arxiv:1707.03384) — first fully-NN SDR implementation; **Ye, Li, Juang, Sivanesan, "Channel Agnostic End-to-End Learning with Conditional GANs,"** IEEE TWC 2020; **Aït Aoudia & Hoydis, "Model-Free Training of End-to-End Communication Systems,"** IEEE JSAC 2019 (arxiv:1812.05929); and **Cammerer et al. "Trainable Communication Systems: Concepts and Prototype,"** IEEE TCOM 2020 (arxiv:1911.13055).

**CSI feedback compression** starts with the seminal **Wen, Shih, Jin, "Deep Learning for Massive MIMO CSI Feedback" (CsiNet),** IEEE WCL 2018 (arxiv:1712.08919). Follow with the derivatives — CsiNet-LSTM (arxiv:1807.11673), CsiNet+ (arxiv:1906.06007), DeepCMC (arxiv:1907.02942), and the 2022 overview by Guo, Wen, Jin, Li (arxiv:2206.14383).

**Neural receivers / signal detection** covers **Ye, Li, Juang, "Power of Deep Learning for Channel Estimation and Signal Detection in OFDM"** (IEEE WCL 2018), **Samuel, Diskin, Wiesel "Deep MIMO Detection"** (arxiv:1706.01151), **Farsad & Goldsmith's SBRNN** (arxiv:1802.02046), and **Shlezinger et al., "ViterbiNet"** (arxiv:1905.10750) — a model-based DL paper in the mold you should aspire to. On the decoding side: **Gruber, Cammerer, Hoydis, ten Brink "On Deep Learning-based Channel Decoding"** (CISS 2017); **Nachmani et al. "Deep Learning Methods for Improved Decoding of Linear Codes"** (IEEE JSTSP 2018); and **Buchberger et al. "Pruning and Quantizing Neural Belief Propagation Decoders"** (arxiv:2001.07464).

**Deep learning for beamforming / MIMO** — **Sun, Chen, Shi, Hong, Fu, Sidiropoulos, "Learning to Optimize: Training DNNs for Interference Management"** (arxiv:1705.09412); **Eisen, Zhang, Chamon, Lee, Ribeiro, "Learning Optimal Resource Allocations in Wireless Systems"** (arxiv:1807.08088); and **Cui, Shen, Yu, "Spatial Deep Learning for Wireless Scheduling"** (arxiv:1808.01486). Plus **Wang, Narasimha, Heath, "MmWave Beam Prediction with Situational Awareness"** (SPAWC 2018) as the situational-awareness bridge to Alkhateeb's work.

**Reinforcement learning for wireless** — **Challita, Dong, Saad "Proactive Resource Management for LTE in Unlicensed Spectrum"** (IEEE TWC 2018); **Ye, Li, Juang, "Deep RL Based Resource Allocation for V2V Communications"** (arxiv:1805.07222); **Nasir & Guo, "Multi-Agent Deep RL for Dynamic Power Allocation"** (arxiv:1808.00490).

**Modulation classification and channel charting** — **O'Shea, Roy, Clancy, "Over-the-Air Deep Learning Based Radio Signal Classification"** (IEEE JSTSP 2018, arxiv:1712.04578) is the RadioML 2018.01A basis paper; **Studer, Medjkouh, Gönültaş, Goldstein, Tirkkonen, "Channel Charting"** (arxiv:1807.05247) is the canonical self-supervised CSI-to-UE positioning paper.

**Recent surveys (2022–2026) to complement the list** — **Ozpoyraz et al., "Deep Learning-Aided 6G Wireless Networks"** (arxiv:2201.03866); **Wang & Li, "Machine Learning in Communications: A Road to Intelligent Transmission and Processing"** (arxiv:2407.11595); and the 2025 **"Robust Deep Learning-Based Physical Layer Communications"** (arxiv:2505.01234) and **"Deep Learning in Wireless Communication Receiver: A Survey"** (arxiv:2501.17184). For books, the **Eldar, Goldsmith, Gündüz, Poor edited volume "Machine Learning and Wireless Communications" (Cambridge 2022)** is the current academic reference, and **Simeone's monograph** remains the best engineer-oriented ML primer.

### Alkhateeb's Wi-Lab — what you must know before cold-emailing

Prof. Alkhateeb (PhD UT Austin 2016 under Robert Heath Jr.; Associate Professor ASU ECEE; ~25,600+ Google Scholar citations; NSF CAREER 2021) directs the Wireless Intelligence Lab. His lab explicitly states "**We are always looking for highly-motivated Ph.D. students**" — cold email is invited. Contact: alkhateeb@asu.edu. Homepages: https://www.aalkhateeb.net/ and https://www.wi-lab.net/.

**The five hottest active directions (2024–2026):**

1. **Foundation models for wireless** — the **Large Wireless Model (LWM)** family. The flagship paper is **Alikhani, Charan, Alkhateeb "Large Wireless Model: A Foundation Model for Wireless Channels"** (arxiv:2411.08872, ICMLCN 2025). It uses a bidirectional transformer with Masked Channel Modeling pretrained on 1M+ DeepMIMO channels across 15 scenarios. Follow-ups are **LWM-Spectro** (arxiv:2601.08780, for I/Q spectrograms with protocol-specialized mixture-of-experts) and **LWM-Temporal** (arxiv:2603.10024, with Sparse Spatio-Temporal Attention). All checkpoints are on Hugging Face at https://huggingface.co/wi-lab (models `wi-lab/lwm`, `wi-lab/lwm-v1.1`, `wi-lab/lwm-spectro`), with an interactive Space demo. **Reproducing or extending LWM is your single highest-leverage project for a Wi-Lab application.**

2. **Digital twins and site-specific ML** — the vision paper is **Alkhateeb, Jiang, Charan "Real-Time Digital Twins: Vision and Research Directions for 6G and Beyond"** (IEEE ComMag 2023, arxiv:2301.11283). Build-out papers include **Jiang & Alkhateeb "Digital Twin Based Beam Prediction"** (arxiv:2301.07682); **Jiang et al. "Learnable Wireless Digital Twins" with Meta Reality Labs** (arxiv:2409.02564); **Luo, Jiang, Khosravirad, Alkhateeb "Digital Twin Aided Massive MIMO CSI Feedback"** (arxiv:2509.25793); and **Luo & Alkhateeb "Digital Twin Aided mmWave MIMO: Site-Specific Beam Codebook Learning"** (arxiv:2512.01902, ICC 2026).

3. **Multi-modal sensing-aided beamforming and DeepSense** — **Alkhateeb et al. "DeepSense 6G: A Large-Scale Real-World Multi-Modal Sensing and Communication Dataset"** (IEEE ComMag 2023); **Morais, Charan, Srinivas, Alkhateeb "DeepSense-V2V"** (IEEE TVT 2025, arxiv:2406.17908); **Demirhan & Alkhateeb "Radar-Aided Beam Prediction and Tracking"** (IEEE TCOM 2026); and **Jiang & Alkhateeb "Computer Vision Aided Beam Tracking in a Real-World mmWave Deployment"** (GLOBECOM Workshops 2022).

4. **Real-world ISAC and RIS-O-RAN** — **Osman, Shekhawat, Roy, Trichopoulos, Alkhateeb "RIS-Aided mmWave O-RAN"** (arxiv:2510.20088) demonstrated a 1,024-element 28 GHz RIS with 9–20 dB SNR gains and won **Best Demo Paper at IEEE MILCOM 2025**. Plus **Jiang & Alkhateeb "Digital Twin Assisted Beamforming for ISAC"** (arxiv:2412.07180).

5. **Generative AI for wireless and dataset analysis** — **Morais et al. "Wireless Dataset Similarity"** (arxiv:2601.01023); **Morais et al. "Comparing Stochastic and Ray-tracing Datasets"** (arxiv:2512.12449, Asilomar 2025); **Khosravirad, Alkhateeb, Van de Voorde "Generative Decompression"** (arxiv:2602.03505).

**DeepMIMO dataset** (https://www.deepmimo.net/, `pip install --pre deepmimo` for v4) is the core tool. v4 is a unified Python toolchain with `dm.download()`, `dm.load()`, `dataset.compute_channels()`, and critically **`dm.convert()`** which accepts Sionna RT, Wireless InSite, or NVIDIA AODT outputs — making DeepMIMO the integration glue between your Sionna work and Wi-Lab's ecosystem. Major scenarios: O1 (outdoor grid at 3.5/28/60 GHz and THz), I1/I3 (indoor), Boston5G_3p5 and Boston5G_28, asu_campus_3p5, plus 12 city scenarios used for LWM pretraining.

**DeepSense 6G** (https://www.deepsense6g.net/) is the multi-modal real-world companion — 1M+ synchronized samples across 40+ scenarios with mmWave (60 GHz phased array), RGB/360° cameras, 32-channel LiDAR, 77 GHz FMCW radar, RTK GPS, and sub-6 channels. Past challenges: Multi-Modal Beam Prediction 2022, LiDAR-Aided 2023, Multi-Modal V2V 2023. The synthetic digital twin is **DeepVerse 6G** (https://deepverse6g.net/). Official baselines live at https://github.com/DeepSense6G.

**Current lab members to know**: Tawfik Osman (RIS/O-RAN/ISAC, MILCOM 2025 Best Demo), Hao Luo (digital twin CSI feedback, 2023 Qualcomm Innovation Fellowship), Sadjad Alikhani (LWM lead), Preston Garrett (DT spatial beam prediction), Namhyun Kim (LWM-Spectro lead), Kengmin Lin. **Recent PhD placements**: Shuaifeng Jiang → Bosch, **João Morais → NVIDIA Wireless SWE**, Gouranga Charan and Umut Demirhan (DeepMIMO maintainer) also graduated in 2024–2025. Sponsors include NSF, Qualcomm, Meta/Facebook Reality Labs, Nokia Bell Labs, InterDigital, Remcom, NVIDIA. The Wi-Lab is an AI-RAN Alliance member.

### NVIDIA's wireless ML ecosystem

**Sionna** (https://nvlabs.github.io/sionna/, https://github.com/NVlabs/sionna) is the centerpiece. Current state as of April 2026: **Sionna 2.0.x** has PHY and SYS migrated to PyTorch (Python 3.11+, PyTorch 2.9+), while **Sionna 1.2.x** remains on TensorFlow. Both coexist — verify which backend any given tutorial targets. Three modules: **Sionna PHY** (link-level — 5G LDPC and polar codes, modulation/demapping, MIMO, OFDM, channel estimation, 5G NR PUSCH, 3GPP 38.901 channels), **Sionna SYS** (system-level PHY abstraction, link adaptation, scheduling, power control), and **Sionna RT** (differentiable ray tracing on Mitsuba 3 + Dr.Jit, framework-agnostic across TF/PyTorch/JAX/NumPy). Sionna RT supports specular/diffuse reflection, refraction, diffraction (since v1.2), RIS (since v0.18), and mobility.

**Core Sionna tutorials to complete** (https://nvlabs.github.io/sionna/phy/tutorials.html): Part 1 (Getting Started), Part 2, Part 3, and especially **Part 4 (Advanced Neural Receiver — training and benchmarking)**. Plus 5G_NR_PUSCH, OFDM_MIMO_Detection, Autoencoder (end-to-end learning), Realistic Multiuser MIMO, Iterative Detection and Decoding, Pulse Shaping, and on the RT side, Introduction to Sionna RT, Mobility, Radio Maps, and RIS tutorials. All source at https://github.com/NVlabs/sionna/tree/main/examples.

**NVIDIA AI Aerial / ACAR / cuPHY** — the full AI-native RAN stack. **Aerial CUDA-Accelerated RAN was open-sourced in December 2025** (Apache 2.0) at https://github.com/NVIDIA/aerial-cuda-accelerated-ran. Components: **cuBB** (CUDA Baseband SDK), **cuPHY** (GPU-accelerated 5G PHY with LDPC/polar/QAM/MIMO/channel estimation), **cuMAC** (L2 scheduler acceleration), **pyAerial** (Python bindings for AI/ML integration with PyTorch/TF/Sionna), and a MATLAB-based 5GModel for test vectors. **Aerial Omniverse Digital Twin (AODT)** (https://developer.nvidia.com/aerial-omniverse-digital-twin) launched at GTC 2024 and open-sourced March 2026 — simulates city-scale 6G systems with 3GPP-compliant software-defined RAN, physically-accurate EM solver, SUMO-based mobility. AODT 1.4 (2026) uses gRPC for embedding into any C++/Python/MATLAB chain.

**NVIDIA 6G Research Cloud** (https://developer.nvidia.com/6g-research), announced March 2024, combines AODT + ACAR + Sionna. Founding ecosystem: Ansys, Arm, ETH Zurich, Fujitsu, Keysight, Nokia, Northeastern, Rohde & Schwarz, Samsung, SoftBank, Viavi. Access via the **NVIDIA 6G Developer Program**. In October 2025, NVIDIA invested $1B in Nokia and announced the **Arc Aerial RAN Computer** (6G-ready) with T-Mobile and Dell; trials begin 2026. The **AI-RAN Alliance** (https://ai-ran.org/) — founded at MWC 2024 by NVIDIA, Arm, AWS, DeepSig, Ericsson, Microsoft, Nokia, Northeastern, Samsung, SoftBank, T-Mobile — had 75 members across 17 countries by MWC 2025.

**Key NVIDIA Research papers** you should know: **Hoydis, Cammerer, Aït Aoudia et al. "Sionna"** (arxiv:2203.11854); **Hoydis et al. "Sionna RT: Differentiable Ray Tracing"** (arxiv:2303.11103) and the 2025 technical report (arxiv:2504.21719); **Cammerer, Aït Aoudia, Hoydis et al. "A Neural Receiver for 5G NR Multi-user MIMO"** (GC Wkshps 2023, arxiv:2312.02601); **Wiesmayr, Cammerer, Aït Aoudia, Hoydis et al. "Design of a Standard-Compliant Real-Time Neural Receiver for 5G NR"** (arxiv:2409.02912, ICMLCN 2025, code at https://github.com/NVlabs/neural_rx); **Hoydis et al. "Learning Radio Environments by Differentiable Ray Tracing"** (IEEE TMLCN 2024, code at https://github.com/NVlabs/diff-rt-calibration); **Cammerer et al. "Sionna Research Kit: A GPU-Accelerated Research Platform for AI-RAN"** (arxiv:2505.15848); **Wiesmayr et al. "SALAD: Self-Adaptive Link Adaptation"** (arxiv:2510.05784); and the older pilotless-OFDM work **Aït Aoudia & Hoydis, "End-to-end Learning for OFDM"** (arxiv:2009.05261). NVIDIA Research people to know: **Jakob Hoydis** (Distinguished Research Scientist, wireless ML lead), **Fayçal Aït Aoudia** and **Sebastian Cammerer** (Sionna co-maintainers), **Alexander Keller** (Senior Director of Research leading the group), plus Reinhard Wiesmayr, Lorenzo Maggi, Guillermo Marcus, Merlin Nimier-David, Tobias Zirr, and — directly relevant to you — **João Morais**, formerly Alkhateeb's PhD student, now at NVIDIA. Research profiles live at https://research.nvidia.com/person/jakob-hoydis, /faycal-ait-aoudia, /sebastian-cammerer.

---

## 5. Projects: the portfolio ladder

Every project ends with a GitHub repo containing a README with a results table and headline figure, Hydra configs, a W&B report link, and reproducibility instructions. This structural consistency is itself a signal to reviewers.

### Level 1 — Beginner (months 1–2)

**OFDM-from-scratch toolbox in NumPy**: single notebook implementing bits → QAM mapping → IFFT → CP → AWGN → FFT → equalization → demapping → BER vs. Eb/N0 validated against Q-function theory. One week. Then **extend to multipath and frequency-selective channels** with a 3-tap Rayleigh multipath, pilot-based LS/MMSE channel estimation, and ZF/MMSE equalization, sweeping perfect CSI vs. LS vs. MMSE. Follow with a **classical ML tabular project** on an RF fingerprinting or UCI signal-modulation dataset using logistic regression, random forest, and XGBoost with proper cross-validation, and a **CIFAR-10 ResNet-18 training exercise with mixed precision** (FP32 vs. `torch.cuda.amp`) logged to W&B — a direct signal of GPU literacy to NVIDIA. Optional but enormously differentiating: an **SDR listening exercise** with a $30 RTL-SDR, recording FM audio and an LTE/Wi-Fi beacon via GNU Radio and demodulating in Python.

### Level 2 — Intermediate (months 3–5)

**Reproduce O'Shea & Hoydis 2017** (arxiv:1702.00832): train an (n,k) autoencoder over AWGN, recover the learned constellations, compare BLER against Hamming codes. **Automatic modulation classification on RadioML 2016.10a and 2018.01A**: CNN, ResNet, and a small Transformer with per-SNR accuracy curves and CFO robustness testing (datasets at https://www.deepsig.ai/datasets/). **Reproduce CsiNet** (Wen-Shih-Jin 2018) on the pre-processed COST2100 dataset across compression ratios 1/4, 1/16, 1/32, 1/64 for indoor + outdoor, then swap in CRNet and CLNet — reference implementations at https://github.com/sydney222/Python_CsiNet, https://github.com/Kylin9511/CRNet, https://github.com/SIJIEJI/CLNet. Complete **Sionna Tutorials Parts 1–4 end-to-end on a GPU**, culminating in the neural receiver on the 3GPP UMi channel, then modify the architecture (swap CNN for a small Transformer block) and compare BLER. Finish with a **Sionna LDPC/polar decoder experiment** training a simple GNN-based decoder on short block lengths vs. classical belief propagation.

### Level 3 — Advanced (months 6–9)

**Beam prediction on DeepSense 6G** — pick scenario 31 (held-out test scenario for 2022 Challenge) or 32–34. Build an LSTM+MLP position baseline, add an RGB branch with a pretrained ResNet, fuse features, and compete on top-k accuracy and DBA-Score. Reference: **Charan et al. arxiv:2209.07519** and the LiDAR baseline arxiv:2203.05548. Write this up as a short workshop paper. **Channel estimation with deep learning on DeepMIMOv4** on `asu_campus_3p5` or `O1_60` — compare LS, LMMSE, and a CNN/U-Net estimator for pilot-sparse mmWave OFDM across SNR and pilot density. **Train a full neural receiver in Sionna RT (site-specific)** using the Munich scene or a custom OSM scene: pretrain on 3GPP UMi, fine-tune for a specific BS location, show site-specific BLER gain. Reference: https://github.com/NVlabs/neural_rx and arxiv:2409.02912. **Reinforcement learning for beam management** on DeepMIMO-generated channels using DQN or PPO via Stable-Baselines3 or CleanRL. And the capstone: **site-specific ML with Sionna RT + DeepMIMO interop** — generate a custom scene (upload an OSM building layout to Sionna RT), export to DeepMIMO via `dm.convert()`, train a beam predictor, demonstrate generalization across two scenes. This single project hits the exact intersection of NVIDIA's and Wi-Lab's research programs.

### Level 4 — Research-level (pick one for a 4–6 month push in Phase 4)

**Reproduce and extend the Large Wireless Model**. Download the LWM Hugging Face checkpoint (https://huggingface.co/wi-lab/lwm), fine-tune on a new DeepMIMO scenario for a new downstream task (user localization, RIS phase prediction, Doppler estimation), and compare against a from-scratch ResNet baseline. The **2025 ITU Large Wireless Models Challenge** provides five pre-built downstream tasks for benchmarking. Cite the LWM-Spectro and LWM-Temporal sequels to show you're current. This is your **single strongest play for Wi-Lab** — a good reproduction functions as an admission essay. Alternative research-level plays: a **sensing-aided beam/blockage prediction paper** for the next DeepSense Challenge using modern transformer fusion (Perceiver IO or ViT); a **merged Sionna open-source contribution** — pick a "good first issue" at https://github.com/NVlabs/sionna, add a tutorial notebook for a classical paper not yet in the gallery, or port a new channel model. Even a small merged PR puts your GitHub handle in front of Hoydis, Cammerer, and Aït Aoudia — an almost-direct line to NVIDIA hiring.

### Paper reproduction discipline

For each paper, create a repo `<paper-short-name>-reproduction` with a dataset-download script, `train.py`, `eval.py`, and a README with one results table comparing your numbers to the paper's. The suggested sequence of 10 foundational papers to reproduce: O'Shea-Hoydis 2017 autoencoder, O'Shea-Roy-Clancy 2018 OTA classification, CsiNet (Wen-Shih-Jin 2018), Ye-Li-Juang 2018 OFDM joint estimation/detection, Dörner et al. 2018 SDR E2E, Aït Aoudia-Hoydis 2020 model-free, DeepMIMO (arxiv:1902.06435), DeepSense 6G (arxiv:2211.09769), Cammerer et al. 2023 neural receiver + Wiesmayr et al. 2024 standard-compliant version, and the LWM family.

### Open-source contribution targets

**Sionna** (https://github.com/NVlabs/sionna), **Sionna Research Kit** (https://github.com/NVlabs/sionna-rk), **neural_rx** (https://github.com/NVlabs/neural_rx), **DeepMIMO** (https://github.com/DeepMIMO/DeepMIMO), **CommPy** (https://github.com/veeresht/CommPy), and **Hugging Face wi-lab** (https://huggingface.co/wi-lab) all have open issues and accept tutorial contributions.

### Public competitions

**DeepSense 6G Challenges** (https://www.deepsense6g.net/challenges/) — top-5 finishes appear on the CVs of current Wi-Lab students. **ITU AI/ML in 5G Challenge** (https://aiforgood.itu.int/about-us/aiml-in-5g-challenge/) — Alkhateeb hosts LWM-track problems; provides free GPU compute. **LWM Competition 2025** on Hugging Face. Plus general Kaggle signal/RF competitions.

---

## 6. The 14-month timeline, month by month

### Phase 1 — Foundations (May–July 2026)

**May 2026 (Month 1)**: Python fundamentals — CS50P compressed to 3 weeks, toolchain setup (uv, VS Code, Git, pre-commit, W&B). Start Andrew Ng ML Specialization Course 1. 3Blue1Brown linear algebra and neural networks playlists. Deliverable: Exercism badges, "learning-log" GitHub repo live, first Kaggle Titanic submission.

**June 2026 (Month 2)**: NumPy and SciPy deep-dive — Rougier's "From Python to NumPy" and 100 Exercises, scipy.signal and scipy.fft tutorials, PySDR chapters 1–4. Andrew Ng ML Specialization Courses 2–3. Deliverable: OFDM-from-scratch notebook with BER curves vs. theory; multipath extension with LS/MMSE channel estimation.

**July 2026 (Month 3)**: PyTorch fluency — Bourke's `learnpytorch.io`, Stevens/Antiga "Deep Learning with PyTorch" chapters 1–8, Karpathy's Zero-to-Hero playlist (micrograd → makemore). Start Andrew Ng Deep Learning Specialization Courses 1–2. Deliverable: CIFAR-10 ResNet-18 with AMP logged to W&B; Level 1 classical ML tabular project.

### Phase 2 — Deep learning and first wireless-ML projects (August–October 2026)

**August 2026 (Month 4)**: Andrew Ng DL Specialization Courses 3–4 (CNNs). Start CS231n notes and Assignment 2. Prince "Understanding Deep Learning" chapters 1–9 + 10–11. Goodfellow chapters 5–9. **Read and reproduce O'Shea & Hoydis 2017 autoencoder**. Deliverable: Reproduction repo with BLER curves matching the paper. **This is also when NVIDIA Summer 2027 intern postings begin opening (Aug–Oct 2026) — start monitoring https://www.nvidia.com/en-us/about-nvidia/careers/university-recruiting/ weekly**.

**September 2026 (Month 5)**: Andrew Ng DL Spec Course 5 (Sequence Models) + CS224N Lectures 5–7. **Transformers week**: Jay Alammar's "Illustrated Transformer" → Karpathy's "Let's build GPT" → "Attention Is All You Need" → Prince Ch 12. Read the O'Shea-Roy-Clancy 2018 paper and **reproduce RadioML modulation classification**. Deliverable: RadioML repo with CNN/ResNet/Transformer comparison. **Submit early NVIDIA BS-level intern applications** (Sept–Oct window is the highest-yield).

**October 2026 (Month 6)**: TensorFlow/Keras crash course (25–35 hours). Generative models — Prince Ch 14–15 + Kingma VAE paper + Lilian Weng's post. **Reproduce CsiNet with CRNet/CLNet extensions**. First PyTorch Lightning + Hydra refactor of an existing project. Deliverable: CsiNet repo with results table across compression ratios; public portfolio landing page (GitHub profile README).

### Phase 3 — Physical-layer ML specialization (November 2026–January 2027)

**November 2026 (Month 7)**: **Sionna tutorials Parts 1–4 end-to-end on a GPU**. Read the Sionna white paper and browse "Made with Sionna" to pick a paper whose idea resonates. Start CS224W (GNNs) for wireless-graph applications. Begin Sutton & Barto RL book chapters 1–8 plus David Silver's RL course lectures 1–7. Deliverable: Sionna tutorials repo with your modified neural receiver (Transformer block swap), plus a "lessons learned" blog post.

**December 2026 (Month 8)**: **First Sionna open-source contribution** — file a doc-fix PR or a good-first-issue PR to https://github.com/NVlabs/sionna. Reinforcement learning depth — Hugging Face Deep RL Units 1–4, Spinning Up VPG → PPO implementation. Read Alkhateeb's **DeepMIMO (arxiv:1902.06435) and DeepSense 6G (arxiv:2211.09769) papers in full** and install both toolchains. Deliverable: merged Sionna PR (even tiny); DeepMIMOv4 working locally on asu_campus_3p5 scenario.

**January 2027 (Month 9)**: **Beam prediction on DeepSense 6G** — LSTM+MLP position baseline, add vision branch, fuse. **DeepMIMO channel estimation project** — CNN/U-Net vs. LS/LMMSE. Read the LWM paper (arxiv:2411.08872) and the Alkhateeb digital twin vision paper (arxiv:2301.11283) carefully. Begin drafting a short Asilomar 2027 paper (typical deadline is April). Deliverable: DeepSense scenario-31 predictor with leaderboard-comparable top-k accuracy; DeepMIMO channel-estimation repo.

### Phase 4 — Advanced projects and original research (February–April 2027)

**February 2027 (Month 10)**: **Train a full neural receiver in Sionna RT** using a custom OSM scene — pretrain on 3GPP UMi, fine-tune site-specific, demonstrate BLER gain. Read the Wiesmayr/Cammerer neural receiver paper (arxiv:2409.02912) and the Hoydis differentiable RT calibration paper as you work. Deliverable: site-specific neural receiver repo.

**March 2027 (Month 11)**: **Research-level push** — choose one of: (a) LWM reproduction and extension on a new DeepMIMO scenario with a new downstream task, comparing against a from-scratch ResNet baseline; (b) DeepSense 6G Challenge submission with modern transformer fusion; (c) a more ambitious Sionna contribution (new block, new channel model, new tutorial). Submit a workshop paper to Asilomar 2027 (deadline typically April). Deliverable: research-level repo, paper draft on arXiv.

**April 2027 (Month 12)**: Polish research-level project, push arXiv preprint. **Begin cold-email research to Prof. Alkhateeb** — read at least 5 of his recent papers, identify a specific technical observation for the email. Read 2025–2026 Wi-Lab papers: LWM-Spectro, LWM-Temporal, Morais "Wireless Dataset Similarity," Osman RIS-O-RAN. Deliverable: arXiv preprint submitted; polished CV; draft cold-email ready.

### Phase 5 — Application and polish (May–June 2027)

**May 2027 (Month 13)**: If you landed the NVIDIA internship, execute it flawlessly (see Section 7). If not, continue research-level project as an independent summer push. **Send cold-email to Prof. Alkhateeb** (late May–early June is the best window) with CV and links to 4–6 polished repos. Begin SoP draft for PhD applications. Retake GRE if the quantitative score is below 168.

**June 2027 (Month 14)**: Finalize PhD school list (target ASU ECEE + 4–6 others). Polish GitHub profile — every repo must have README with results table, headline figure, quickstart, and citation. Begin drafting personal statements. Reach out to letter writers (one wireless/DSP professor, one ML professor, one research mentor). Attend IEEE ICC 2027 virtually if possible; engage on LinkedIn with Hoydis, Cammerer, Alkhateeb. Deliverable: complete portfolio ready for application season (Nov 2027 for Fall 2028 PhD start).

---

## 7. Application strategy

### NVIDIA Summer 2027 internship

The realistic timeline: **postings open August–October 2026**, roll through December, and heavy-volume Research team decisions close January–February 2027. Apply early (the September–October window is highest-yield). As a junior, the realistic target is **BS-level ML/SWE intern roles** — NVIDIA Research internships explicitly target PhD students, though direct researcher contact can create exceptions. Limit applications to 3–5 best-fit roles per NVIDIA's own guidance.

What to emphasize on the application: (1) **a completed Sionna project on GitHub** — a trained neural receiver notebook is the single strongest signal; (2) **PyTorch fluency plus basic CUDA/Triton exposure** — work through **NVIDIA's Deep Learning Institute courses** at https://learn.nvidia.com/, specifically "Fundamentals of Accelerated Computing with CUDA Python" and "Building Transformer-Based NLP Applications"; (3) **an arXiv or workshop preprint** even if it's a reproduction; (4) **4–6 polished GitHub repos** each with results tables; (5) **5G/6G domain literacy** — know 3GPP PHY basics (PUSCH, DMRS, LDPC, HARQ, CSI-RS).

Interview preparation: 150+ LeetCode mediums on arrays/hashmaps/graphs/DP starting 8–12 weeks before applications open; ML fundamentals prep on bias/variance, batch-norm vs. layer-norm, transformer forward pass on paper, AdamW vs. SGD, mixed precision, gradient checkpointing; domain prep on OFDM, cyclic prefix, pilot-aided channel estimation, LDPC belief propagation, the autoencoder-as-PHY view, and what differentiable ray tracing is and why it matters. For senior interns, add distributed training (DDP, FSDP) and data pipeline design.

**Directly email NVIDIA researchers** once your portfolio has real content: a concise pitch with a concrete project extension to a 2024–2025 paper of theirs (e.g., "I'd like to work on extensions to SALAD for link adaptation" or "I have a reproduction of the standard-compliant NRX and a proposed site-specific pretraining experiment"). Do not email until you have at least one Sionna-based project on GitHub. NVIDIA Research operates on a sponsor model — a specific researcher must want you on their project.

### Wi-Lab PhD application

Prof. Alkhateeb explicitly invites cold emails. Timing: send **between late May and early September 2027** (the summer before your Fall 2027 PhD application for Fall 2028 entry), or earlier if you have strong results. Keep it 150–200 words plus a one-page CV. Structure: one line identifying yourself (junior at X, GPA, concentration) → one sentence naming a specific recent paper of his with a substantive technical observation (not a generic compliment) → 2–3 bullets with concrete artifacts and GitHub links (LWM reproduction, DeepSense Challenge rank, DeepMIMO contribution) → clear ask: "I'd love to apply for Fall 2028 PhD admission. Would you be accepting students, and would engagement with DeepSense/DeepMIMO this year be useful?" Follow up exactly once, 2–3 weeks later.

**Avoid**: generic passion statements, GPA-only bragging, claiming expertise in everything, attaching papers you haven't actually read, sending without having read at least three of his recent papers. **Contact**: alkhateeb@asu.edu. On Twitter/X the handle `@AhmedAlKhateeb` belongs to a Saudi tourism minister, not the professor — stick to email and LinkedIn. Admin contact: Katarina.Miller@asu.edu.

The Wi-Lab admit profile based on current membership: strong EE/CS background with signal processing + ML coursework; at least one research project with a preprint or publication; **demonstrated use of DeepMIMO, DeepSense, or Sionna is nearly a prerequisite**; 1–2 coauthored workshop/letter papers is common; GPA ≥3.5 in the last 60 hours. Strong letters from at least one recognizable wireless-area faculty. ASU ECEE PhD deadline is typically December 15 for Fall start (verify each year); interview invitations December–February, visit days March, decisions by the April 15 universal reply date. Take the GRE even if nominally optional — 160+ Q is a zero-cost positive signal. International applicants need TOEFL iBT ≥100 as a competitive target.

**Funding path options**: direct PhD (apply Nov–Dec 2027 for Fall 2028 entry, best for funding) is primary target; alternatively a Summer 2027 REU at WINLAB Rutgers, Virginia Tech Hume Center, Notre Dame Wireless Institute, or Colorado Boulder; or ask Alkhateeb directly about informal summer positions if your portfolio is strong. Master's-first is a viable but slower and often self-funded path.

### GitHub portfolio best practices

Use this structure for every repo: README with a results table and headline figure in the top screen, LICENSE (MIT or Apache-2.0), pinned `requirements.txt` or `pyproject.toml`, `configs/` directory with Hydra/YAML configs for every experiment, `src/` with `data/`, `models/`, `train.py`, `eval.py`, `notebooks/` only for exploration, `scripts/` for `download_data.sh` and `run_all.sh`, `tests/` with pytest, `docs/` for figures, `CITATION.cff` so people can cite your repo, `.github/workflows/` for CI with lint + test. Pre-commit with black + ruff + isort. Pin PyTorch and CUDA versions. Embed W&B report links in the README.

README checklist: one-line description with badge row; headline results table in first screen; headline figure (loss curve, BER curve, constellation); a "Quickstart" with 4 shell commands reproducing one result; a "Full reproduction" section with dataset download scripts and exact commands; BibTeX citation block; acknowledgements.

Exemplary portfolios to study: https://github.com/NVlabs/sionna (the gold standard for ML-PHY repos), https://github.com/NVlabs/neural_rx (exemplary code-for-a-paper), https://github.com/DeepMIMO/DeepMIMO (clean library with DB API), https://github.com/emilbjornson (every repo pairs with a textbook chapter), https://github.com/lucidrains (lightweight single-purpose reproductions), https://github.com/karpathy/nanoGPT (exemplary minimal ML repo).

### Conferences to engage

Flagship wireless venues where Alkhateeb's lab publishes: **IEEE ICC** (May/June, ML for Communications workshop co-chaired by O'Shea), **IEEE GLOBECOM** (December, strong ML workshops), **IEEE ICASSP** (May, signal processing flagship), **Asilomar Conference on Signals, Systems, and Computers** (late October/early November, Pacific Grove CA, short deadlines in April — Wi-Lab sends people every year), **IEEE SPAWC** (July, high density of ML-PHY papers), **IEEE WCNC**, **IEEE VTC**, and the new **IEEE ICMLCN** (dedicated ML-for-communication-and-networking venue). ML conferences: **NeurIPS, ICML, ICLR** — watch for their ML4Wireless workshops. Join the **IEEE ComSoc Machine Learning for Communications ETI** (https://mlc.committees.comsoc.org/) and read its research library top-to-bottom. Student travel grants of $500–$1500 are commonly available via IEEE ComSoc, SPS, and conferences directly. Ask — don't self-eliminate on funding.

---

## 8. Community and ongoing learning

**Twitter/X**: **Tim O'Shea at @oshtim** is verified and active. Ahmed Alkhateeb, Jakob Hoydis, Emil Björnson, and most senior wireless researchers post primarily on **LinkedIn**, not X — Hoydis's LinkedIn (https://www.linkedin.com/in/jhoydis/) posts Sionna release notes; follow Cammerer, Alkhateeb, Björnson, and O'Shea there. Use X's Lists feature to track the remaining ML community via retweets. **GitHub follows** for jhoydis, emilbjornson, Alkhateeb collaborators are equally valuable.

**YouTube**: **Wireless Future** (Björnson + Larsson, https://www.youtube.com/c/WirelessFuture) is the best wireless-specific channel on YouTube and essentially required viewing. **NVIDIA Developer** (https://www.youtube.com/@NVIDIADeveloper) hosts Sionna tutorials. Yannic Kilcher and Two Minute Papers for general ML; Stanford Online and MIT OpenCourseWare for course lectures; DeepSig for occasional tech talks.

**Podcasts**: **Wireless Future podcast** (https://wirelessfuture.podbean.com/, same duo as the YouTube channel) — required listening. Machine Learning Street Talk and The Gradient Podcast for ML. No flagship ML-for-wireless podcast exists today, which is itself an opportunity.

**Newsletters**: The Batch (deeplearning.ai) for weekly ML news; Import AI (Jack Clark) for policy; **IEEE ComSoc Technology News** at https://www.comsoc.org/publications/ctn; **NVIDIA Developer Blog** Telecommunications and Sionna tags at https://developer.nvidia.com/blog/category/telecommunications/; Emil Björnson's blog (https://ebjornson.com/blog/); Alkhateeb's lab news page checked quarterly.

**Forums and communities**: **DeepMIMO Forum** at https://deepmimo.net/forum/ — the direct line to Alkhateeb's team and users; **DeepSense Forum** linked from challenge pages; **NVIDIA Developer Forums** have a dedicated Sionna sub-forum at https://forums.developer.nvidia.com/; PyTorch Forums (discuss.pytorch.org); Hugging Face Discord; Fast.ai Forums; GNU Radio Matrix/Slack; **NVIDIA 6G Developer Program** at https://developer.nvidia.com/6g-program (register).

**arXiv auto-tracking**: set email alerts at https://arxiv.org/a/ for **eess.SP** (signal processing, primary), **cs.IT** (information theory, primary for PHY), **cs.LG** (ML), and **cs.NI** (networking). Set Google Scholar alerts for keywords "Sionna," "DeepMIMO," "DeepSense," "neural receiver," "beam prediction," "CSI feedback," "channel estimation deep learning," and author alerts for Alkhateeb, Hoydis, O'Shea, Björnson, Studer, Goldsmith.

**Hugging Face org to watch**: https://huggingface.co/wi-lab for LWM checkpoints and future foundation models.

---

## 9. What this plan is really asking of you

**Execute tight loops, not sprawling plans.** Every month ends with a new artifact on GitHub and a new paper in your notes repo. Every week ends with at least one git commit to your main project and at least one paper summary. The single biggest mistake junior researchers make is over-consuming courses and under-producing artifacts — the ladder above is engineered to prevent that. If you are ever more than 3 weeks without a new public artifact, stop whatever course you're taking and ship something.

**Pick Sionna and DeepMIMO as your first loves.** Everything else is substitutable; these two are not. Your Sionna neural receiver tutorial reproduction in Month 7 and your LWM extension in Month 11 are the two most important items in this entire document. If you do nothing else, do those two well.

**Email early and specifically.** The difference between "another applicant" and "we've been watching your work" is a cold email in June 2027 that names a specific paper and links to a specific repo. Practice this skill by sending two preparatory emails earlier — to João Morais at NVIDIA about his path from Wi-Lab, and to Umut Demirhan (DeepMIMO maintainer) with a dataset-related question after your Phase 3 project. Both are former Wi-Lab students who remember what it was like to be you.

**Treat this as the start of a research career, not a checklist.** The 14 months are not a race to admission — they are the first 14 months of a 5–6 year project. The habits you build now (reproducibility, paper reading, writing up results honestly, talking to researchers) are the research career. Andrew Ng's Course 3 and Sutton's book and Ramalho's "Fluent Python" are not separate from your wireless goals; they are what makes a student become a researcher capable of those goals. The roadmap above will get you to the door of NVIDIA and Wi-Lab. What you do after is up to you.