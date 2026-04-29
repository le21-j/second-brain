# Papers shelf — Physical-Layer ML canonical reading list

Reference index of every paper cited in the [[python-ml-wireless]]. Papers are not mirrored here — the canonical form is arXiv. When Jayden reads one and it becomes a reproduction project, drop the PDF into this folder and ingest it.

Grouped by technical subtopic. Each entry: `authors, year — title (arxiv | venue)`.

## Tutorials and surveys (start here)

- **O'Shea & Hoydis 2017** — An Introduction to Deep Learning for the Physical Layer (arxiv:1702.00832; IEEE TCCN 2017). The seminal paper. See [[autoencoder-phy]].
- **Simeone 2018** — A Brief Introduction to Machine Learning for Engineers (arxiv:1802.05374).
- **Wang, Di Renzo, Stanczak, Larsson 2020** — AI-Enabled Wireless Networking for 5G and Beyond (IEEE Wireless Comm).
- **Arulkumaran et al. 2017** — Deep Reinforcement Learning: A Brief Survey (IEEE SPM).
- **Ozpoyraz et al. 2022** — Deep Learning-Aided 6G Wireless Networks (arxiv:2201.03866).
- **Wang & Li 2024** — Machine Learning in Communications (arxiv:2407.11595).
- **2025 surveys** — arxiv:2505.01234 (Robust DL PHY), arxiv:2501.17184 (DL Wireless Receivers).

## Channel estimation with DL

- **He, Wen, Jin, Li 2018** — DL-Based Channel Estimation for Beamspace mmWave Massive MIMO (arxiv:1802.01290).
- **Neumann, Wiese, Utschick 2018** — Learning the MMSE Channel Estimator (IEEE TSP).
- **Hu, Gao, Zhang, Jin, Li 2021** — DL for Channel Estimation (arxiv:1911.01918).

## Autoencoder / end-to-end learning

- **Dörner, Cammerer, Hoydis, ten Brink 2018** — DL-Based Communication over the Air (arxiv:1707.03384). First fully-NN SDR.
- **Ye, Li, Juang, Sivanesan 2020** — Channel Agnostic E2E Learning with Conditional GANs (IEEE TWC).
- **Aït Aoudia & Hoydis 2019** — Model-Free Training of End-to-End Communication Systems (arxiv:1812.05929; IEEE JSAC).
- **Cammerer et al. 2020** — Trainable Communication Systems: Concepts and Prototype (arxiv:1911.13055).
- **Aït Aoudia & Hoydis 2020** — End-to-end Learning for OFDM (arxiv:2009.05261).

## CSI feedback compression

- **Wen, Shih, Jin 2018** — DL for Massive MIMO CSI Feedback (CsiNet, arxiv:1712.08919). See [[csi-feedback]].
- **CsiNet-LSTM 2018** (arxiv:1807.11673).
- **CsiNet+ 2019** (arxiv:1906.06007).
- **DeepCMC 2019** (arxiv:1907.02942).
- **Guo, Wen, Jin, Li 2022 overview** (arxiv:2206.14383).
- **Luo, Jiang, Khosravirad, Alkhateeb 2025** — Digital Twin Aided Massive MIMO CSI Feedback (arxiv:2509.25793).

## Neural receivers / signal detection

- **Ye, Li, Juang 2018** — Power of DL for Channel Estimation & Signal Detection in OFDM (IEEE WCL).
- **Samuel, Diskin, Wiesel 2017** — Deep MIMO Detection (arxiv:1706.01151).
- **Farsad & Goldsmith 2018** — Sliding Bidirectional RNN for sequence demodulation (arxiv:1802.02046).
- **Shlezinger et al. 2019** — ViterbiNet (arxiv:1905.10750). Model-based DL — read carefully.
- **Cammerer, Aït Aoudia, Hoydis et al. 2023** — A Neural Receiver for 5G NR Multi-user MIMO (arxiv:2312.02601). See [[neural-receiver]].
- **Wiesmayr, Cammerer, Aït Aoudia, Hoydis et al. 2024** — Design of a Standard-Compliant Real-Time Neural Receiver for 5G NR (arxiv:2409.02912, ICMLCN 2025). Code: https://github.com/NVlabs/neural_rx.

## Neural decoders

- **Gruber, Cammerer, Hoydis, ten Brink 2017** — On DL-based Channel Decoding (CISS).
- **Nachmani et al. 2018** — DL Methods for Improved Decoding of Linear Codes (IEEE JSTSP).
- **Buchberger et al. 2020** — Pruning and Quantizing Neural Belief Propagation Decoders (arxiv:2001.07464).

## DL for beamforming / MIMO / resource allocation

- **Sun, Chen, Shi, Hong, Fu, Sidiropoulos 2017** — Learning to Optimize (arxiv:1705.09412).
- **Eisen, Zhang, Chamon, Lee, Ribeiro 2018** — Learning Optimal Resource Allocations (arxiv:1807.08088).
- **Cui, Shen, Yu 2018** — Spatial DL for Wireless Scheduling (arxiv:1808.01486).
- **Wang, Narasimha, Heath 2018** — MmWave Beam Prediction with Situational Awareness (SPAWC).

## RL for wireless

- **Challita, Dong, Saad 2018** — Proactive Resource Management for LTE-U (IEEE TWC).
- **Ye, Li, Juang 2018** — Deep RL Based Resource Allocation for V2V (arxiv:1805.07222).
- **Nasir & Guo 2018** — Multi-Agent DRL for Dynamic Power Allocation (arxiv:1808.00490).

## Modulation classification, channel charting

- **O'Shea, Roy, Clancy 2018** — Over-the-Air DL Based Radio Signal Classification (arxiv:1712.04578). RadioML 2018.01A basis paper.
- **Studer, Medjkouh, Gönültaş, Goldstein, Tirkkonen 2018** — Channel Charting (arxiv:1807.05247). See [[channel-charting]].

## Sionna / NVIDIA Research

- **Hoydis, Cammerer, Aït Aoudia et al. 2022** — Sionna (arxiv:2203.11854). See [[sionna]].
- **Hoydis et al. 2023** — Sionna RT: Differentiable Ray Tracing (arxiv:2303.11103).
- **Hoydis et al. 2025** — Sionna RT technical report (arxiv:2504.21719).
- **Hoydis et al. 2024** — Learning Radio Environments by Differentiable Ray Tracing (IEEE TMLCN). Code: https://github.com/NVlabs/diff-rt-calibration. See [[differentiable-ray-tracing]].
- **Cammerer et al. 2025** — Sionna Research Kit (arxiv:2505.15848).
- **Wiesmayr et al. 2025** — SALAD: Self-Adaptive Link Adaptation (arxiv:2510.05784).

## DeepMIMO / DeepSense / Alkhateeb Wi-Lab

- **Alkhateeb 2019** — DeepMIMO dataset (arxiv:1902.06435). See [[deepmimo]].
- **Alkhateeb et al. 2023** — DeepSense 6G (arxiv:2211.09769; IEEE ComMag). See [[deepsense-6g]].
- **Charan et al. 2022** — Multi-Modal Beam Prediction Challenge (arxiv:2209.07519).
- **Alkhateeb, Jiang, Charan 2023** — Real-Time Digital Twins for 6G (arxiv:2301.11283). See [[wireless-digital-twin]].
- **Jiang & Alkhateeb 2023** — Digital Twin Based Beam Prediction (arxiv:2301.07682).
- **Jiang et al. 2024** — Learnable Wireless Digital Twins (arxiv:2409.02564).
- **Morais, Charan, Srinivas, Alkhateeb 2024** — DeepSense-V2V (arxiv:2406.17908).
- **Demirhan & Alkhateeb 2026** — Radar-Aided Beam Prediction and Tracking (IEEE TCOM).
- **Jiang & Alkhateeb 2022** — Vision Aided Beam Tracking (GLOBECOM).
- **Alikhani, Charan, Alkhateeb 2024** — Large Wireless Model (arxiv:2411.08872). See [[large-wireless-model]].
- **LWM-Spectro 2026** (arxiv:2601.08780).
- **LWM-Temporal 2026** (arxiv:2603.10024).
- **Osman, Shekhawat, Roy, Trichopoulos, Alkhateeb 2025** — RIS-Aided mmWave O-RAN (arxiv:2510.20088). MILCOM 2025 Best Demo.
- **Jiang & Alkhateeb 2024** — Digital Twin Assisted Beamforming for ISAC (arxiv:2412.07180).
- **Morais et al. 2026** — Wireless Dataset Similarity (arxiv:2601.01023).
- **Morais et al. 2025** — Comparing Stochastic and Ray-tracing Datasets (arxiv:2512.12449).
- **Khosravirad, Alkhateeb, Van de Voorde 2026** — Generative Decompression (arxiv:2602.03505).
- **Luo & Alkhateeb 2026** — Digital Twin Aided mmWave MIMO Beam Codebook Learning (arxiv:2512.01902).

## Foundational deep-learning papers (read in order)

- **LeNet-5** (LeCun 1998) — the first CNN.
- **AlexNet** (Krizhevsky 2012).
- **VGG** (Simonyan 2014).
- **ResNet** (He 2015, arxiv:1512.03385).
- **DenseNet**, **MobileNetV2**, **EfficientNet**, **ConvNeXt**.
- **Attention Is All You Need** (Vaswani 2017, arxiv:1706.03762). See [[transformer]].
- **BERT** (Devlin 2018).
- **GPT** (Radford 2018, 2019, 2020).
- **VAE** (Kingma & Welling 2013, arxiv:1312.6114). See [[variational-autoencoder]].
- **GAN** (Goodfellow 2014, arxiv:1406.2661).
- **DCGAN**, **WGAN-GP**.
- **DDPM** (Ho 2020). See [[diffusion-model]].

## Related wiki pages
- [[python-ml-wireless]]
- [[sionna]]
- [[deepmimo]]
- [[deepsense-6g]]
- [[large-wireless-model]]
