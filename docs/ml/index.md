---
title: Machine Learning
summary: Live research directions in machine learning foundations, scaling, data, and optimization.
status: evergreen
updated: 2026-04-24
tags:
  - machine learning
  - foundations
  - theory
---

This page is a living map of machine learning research directions that still matter once hype is stripped away. The emphasis here is on scaling, data, optimization, and generalization, with enough structure to decide what to read next and enough current signals to avoid freezing the page in a 2024 worldview.

## Topic Map

- **Scaling laws and resource allocation**
  This is the bridge from classical sample complexity intuition to foundation-model-era training decisions. It now includes not only model size and token count, but also data quality, task mix, and subgroup behavior. Start with [Scaling Laws and Compute-Optimal Training](scaling-laws-compute-optimal-training.md).
- **Data curation and data value**
  The center of gravity has shifted from “collect more data” to “understand which data changes the frontier.” This includes filtering, deduplication, example selection, mixture design, and data valuation.
- **Synthetic data as a training resource**
  Synthetic data is no longer just augmentation. The active question is when synthetic corpora create new scaling regimes, when they merely smooth over scarcity, and when they introduce collapse or tail-risk artifacts.
- **Generalization and implicit bias**
  Overparameterization is still the core puzzle, but the newer angle is how optimization, data quality, and shortcut features interact. The current anchors are [Generalization in the Overparameterized Era](generalization-overparameterization.md) and [ML Theory](theory.md).
- **Training numerics and recipe stability**
  Low-precision training now matters not just for cost, but for whether scaling experiments remain scientifically interpretable. FP8 and MXFP4 recipes sit at the boundary between ML theory and systems reality.

## Research Questions Right Now

- When does better data beat more data, and how can we tell before paying the full pretraining cost?
- Which scaling laws remain predictive once data quality, multilingual transfer, or task-specific metrics matter more than aggregate validation loss?
- How much of modern generalization comes from optimizer bias versus architecture versus data curriculum?
- Which synthetic-data regimes improve base-model quality, and which ones only inflate apparent progress on narrow evaluations?
- Which low-precision recipes preserve the optimization trajectory, not just the final benchmark score?

## Research Radar

Updated April 24, 2026.

This radar prefers 2025-2026 work. Older entries stay only when they still serve as the cleanest impact reference for a direction that is actively evolving.

### Active Directions

- Scaling laws are moving beyond aggregate validation loss toward task-aware, subgroup-aware, and data-quality-aware views.
- Data curation is becoming a first-class optimization variable rather than a preprocessing afterthought.
- Synthetic data is being studied as a pretraining resource with its own scaling behavior, not just as augmentation.
- Low-precision training is shifting from isolated kernel tricks to end-to-end recipes that can survive large-scale runs.
- Generalization remains anchored on interpolation and implicit regularization, but the newer frontier is understanding how these effects change across architectures, data mixtures, and evaluation slices.

### Keywords To Track

`task-aware scaling`, `relative scaling laws`, `data-quality scaling`, `synthetic data scaling`, `data valuation`, `data curation`, `predictive data selection`, `FP8 training`, `MXFP4`, `implicit regularization`

### Recent Papers And Research Signals By Direction

#### Scaling Laws And Data Quality

- [Hu et al. (2026), Neural Neural Scaling Laws](https://arxiv.org/abs/2601.19831)
- [Held et al. (2025), Relative Scaling Laws for LLMs](https://arxiv.org/abs/2510.24626)
- [Subramanyam et al. (2026), Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining](https://openreview.net/forum?id=x54wwB6QvL) (ICLR 2026 poster)

#### Data Quality, Curation, And Data Value

- [Wang et al. (2025), Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures](https://arxiv.org/abs/2511.13640)
- [Shum et al. (2025), Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://arxiv.org/abs/2503.00808)
- [Li et al. (2025), MASS: Mathematical Data Selection via Skill Graphs for Pretraining Large Language Models](https://arxiv.org/abs/2503.14917)
- [Dohmatob et al. (2026), Why Less is More (Sometimes): A Theory of Data Curation](https://openreview.net/forum?id=8KcjEygedc) (ICLR 2026 poster)
- [Evans et al. (2024), Data curation via joint example selection further accelerates multimodal learning](https://arxiv.org/abs/2406.17711) (kept as an impact curation paper)
- [Penedo et al. (2024), The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) (kept as an impact dataset paper)
- [Soldaini et al. (2024), Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research](https://arxiv.org/abs/2402.00159) (kept as an impact open-data reference)

#### Synthetic Data As A Scaling Resource

- [Qin et al. (2025), Scaling Laws of Synthetic Data for Language Models](https://arxiv.org/abs/2503.19551)
- [Wang et al. (2025), Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures](https://arxiv.org/abs/2511.13640)
- [Kothapalli et al. (2026), PluRel: Synthetic Data unlocks Scaling Laws for Relational Foundation Models](https://openreview.net/forum?id=iti7t2oI85) (ICLR 2026 DATA-FM workshop)

#### Generalization, Implicit Bias, And Robustness

- [Wenger et al. (2026), Variational Deep Learning via Implicit Regularization](https://openreview.net/forum?id=WsN88Ns0i6) (ICLR 2026 poster)
- [Mirzaie et al. (2026), Implicit Regularization of SGD Reduces Shortcut Learning](https://openreview.net/forum?id=CPdAB7H8mU) (ICLR 2026 poster)

#### Low-Precision Training Recipes

- [Hernández-Cano et al. (2025), Towards Fully FP8 GEMM LLM Training at Scale](https://arxiv.org/abs/2505.20524)
- [Zhang et al. (2026), MOSS: Efficient and Accurate FP8 LLM Training with Microscaling and Automatic Scaling](https://openreview.net/forum?id=uvgJM9RQ6T) (ICLR 2026 poster)
- [Wang et al. (2025), FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error](https://arxiv.org/abs/2511.02302)
- [Tseng et al. (2025), Training LLMs with MXFP4](https://arxiv.org/abs/2502.20586)

## Site Coverage

- [Scaling Laws and Compute-Optimal Training](scaling-laws-compute-optimal-training.md)
  The evergreen note for compute-optimal thinking, classic scaling laws, and where newer quality-aware laws depart from the Chinchilla-era mental model.
- [Generalization in the Overparameterized Era](generalization-overparameterization.md)
  The best current internal anchor for interpolation, double descent, and benign overfitting.
- [ML Theory](theory.md)
  The landing point for optimization and theory-heavy notes that explain why these research directions matter.
- [Practical ML](practice.md)
  The engineering layer for experiments, reproducibility, and training-loop discipline.

## Sources To Follow

- [OpenReview](https://openreview.net/)
- [Proceedings of Machine Learning Research](https://proceedings.mlr.press/pmlr.html)
- [Journal of Machine Learning Research](https://jmlr.org/)
- [Google DeepMind Research](https://deepmind.google/en/research/)
- [Ai2 Open Data](https://allenai.org/open-data)
- [Hugging Face FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)

## Open Backlog

- A deeper note on data curation beyond deduplication: selection, mixture design, and when pruning beats scaling.
- A focused reading map on synthetic data scaling, model collapse, and how to evaluate real-synthetic mixtures.
- A theory note on implicit regularization after 2025: shortcut learning, flatness, and optimizer-dependent bias.
- A practical research note on FP8 and MXFP4 training recipes, including what counts as a scientifically honest comparison.
- A future subpage on multilingual and cross-lingual data scaling once the current crop of 2026 work stabilizes.
