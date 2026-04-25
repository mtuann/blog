---
title: Machine Learning
summary: Foundational ideas, practical workflows, and the bridge from core ML to modern generative models.
status: evergreen
updated: 2026-04-24
tags:
  - machine learning
  - foundations
  - theory
---

<div class="hero-shell section-hero ml-hero">
<p class="hero-eyebrow">Foundations</p>

<h1>Machine Learning</h1>

<p class="hero-lead">This section is the base layer for the rest of the site: optimization, generalization, scaling, practical experimentation, and the bridge from classical ML intuition to modern deep learning behavior.</p>

<div class="chip-row">
<span class="chip">Optimization</span>
<span class="chip">Generalization</span>
<span class="chip">Scaling laws</span>
<span class="chip">Practical ML</span>
</div>

<div class="hero-actions">
<a class="md-button md-button--primary" href="theory/">Read ML Theory</a>
<a class="md-button" href="scaling-laws-compute-optimal-training/">Read Scaling Laws</a>
</div>
</div>

<div class="hub-grid">
<div class="hub-panel">
<h3>Start Here</h3>
<ul class="link-stack">
  <li><a href="theory/">Theory</a><p>Optimization, scaling laws, and mathematical foundations.</p></li>
  <li><a href="generalization-overparameterization/">Generalization in the Overparameterized Era</a><p>The modern view of interpolation and test error.</p></li>
  <li><a href="practice/">Practical ML</a><p>Experimentation, training loops, and reproducibility.</p></li>
  <li><a href="../genai/transformer-attention/">Transformer Foundations</a><p>The bridge into foundation models.</p></li>
</ul>
</div>

<div class="hub-panel">
<h3>Flagship Notes</h3>
<ul class="link-stack">
  <li><a href="generalization-overparameterization/">Generalization in the Overparameterized Era</a></li>
  <li><a href="scaling-laws-compute-optimal-training/">Scaling Laws and Compute-Optimal Training</a></li>
  <li><p>More derivation-driven notes will land here next.</p></li>
</ul>
</div>

<div class="hub-panel">
<h3>Open Questions</h3>
<ul>
  <li>Which scaling insights are truly stable across architectures and data regimes?</li>
  <li>What practical signals best predict whether a training run is improving or drifting?</li>
  <li>Which old ML ideas are worth revisiting in the era of foundation models?</li>
</ul>
</div>
</div>

## Research Radar

Updated April 24, 2026.

This radar prefers 2025-2026 work. Anything older is kept only if it still serves as the cleanest foundation or an impact reference for the direction.

### Active Directions

- Scaling laws are moving beyond aggregate validation loss toward task-aware, subgroup-aware, and data-quality-aware views.
- Data curation is becoming a first-class optimization variable rather than a preprocessing afterthought.
- Synthetic data is being studied as a pretraining resource with its own scaling behavior, not just as augmentation.
- Low-precision training is shifting from isolated kernel tricks to end-to-end recipes that can survive large-scale runs.
- Generalization remains anchored on interpolation and implicit regularization, but the newer frontier is understanding how these effects change across architectures, data mixtures, and evaluation slices.

### Keywords To Track

`task-aware scaling`, `relative scaling laws`, `data-quality scaling`, `synthetic data scaling`, `data valuation`, `data curation`, `predictive data selection`, `FP8 training`, `MXFP4`, `implicit regularization`

### Recent Papers By Direction

#### Scaling Beyond A Single Loss Curve

- [Neural Neural Scaling Laws](https://arxiv.org/abs/2601.19831) (2026)
- [Relative Scaling Laws for LLMs](https://arxiv.org/abs/2510.24626) (2025)
- [Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining](https://arxiv.org/abs/2510.03313) (2025)

#### Data Quality, Curation, And Data Value

- [Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures](https://arxiv.org/abs/2511.13640) (2025)
- [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://arxiv.org/abs/2503.00808) (2025)
- [MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models](https://arxiv.org/abs/2503.14917) (2025)
- [Data curation via joint example selection further accelerates multimodal learning](https://arxiv.org/abs/2406.17711) (2024, kept because it strongly shaped the current curation conversation)
- [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) (2024, kept as an impact dataset paper)
- [Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research](https://arxiv.org/abs/2402.00159) (2024, kept as an impact open-data reference)

#### Synthetic Data As A Scaling Resource

- [Scaling Laws of Synthetic Data for Language Models](https://arxiv.org/abs/2503.19551) (2025)
- [Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures](https://arxiv.org/abs/2511.13640) (2025)

#### Low-Precision Training Recipes

- [Towards Fully FP8 GEMM LLM Training at Scale](https://arxiv.org/abs/2505.20524) (2025)
- [InfiR2: A Comprehensive FP8 Training Recipe for Reasoning-Enhanced Language Models](https://arxiv.org/abs/2509.22536) (2025)
- [FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error](https://arxiv.org/abs/2511.02302) (2025)
- [Training LLMs with MXFP4](https://arxiv.org/abs/2502.20586) (2025)

### Sources To Follow

- [OpenReview](https://openreview.net/) for current ICLR-style discussion and freshly posted papers.
- [Proceedings of Machine Learning Research](https://proceedings.mlr.press/pmlr.html) for ICML, AISTATS, COLT, and workshop proceedings.
- [Google DeepMind Research](https://deepmind.google/en/research/) for data curation, scaling, and optimization work.
- [Ai2 Open Data](https://allenai.org/open-data) and the [Dolma project page](https://allenai.org/blog/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64) for open-corpus and data-pipeline signals.
- [Hugging Face FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) for open pretraining-data releases.
- [PyTorch Blog](https://pytorch.org/blog/) for practical training-system updates that often land before polished survey coverage.

### Canonical References Worth Keeping

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
- [Deep Double Descent: Where Bigger Models and More Data Hurt](https://arxiv.org/abs/1912.02292)
- [Benign Overfitting in Linear Regression](https://arxiv.org/abs/1906.11300)
