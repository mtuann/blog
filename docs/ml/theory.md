---
title: Machine Learning Theory
summary: Mathematical foundations for optimization, generalization, and deep learning dynamics.
status: evergreen
updated: 2026-04-24
tags:
  - machine learning
  - theory
  - optimization
---

# Machine Learning Theory

This section tracks the mathematical ideas that remain useful even as the tooling changes. The goal is to understand why models learn, where the abstractions break, and which theoretical ideas help interpret modern AI behavior.

## Core Objective

At the heart of most ML systems is empirical risk minimization:

$$
\theta^\* = \arg\min_{\theta} \frac{1}{N}\sum_{i=1}^{N} \mathcal{L}(f_{\theta}(x_i), y_i)
$$

The interesting work begins after writing that equation down: optimization dynamics, inductive bias, data scale, and model architecture all shape what this objective actually produces in practice.

## Foundations To Build

### 1. Optimization

- Gradient descent and its stochastic variants.
- Loss landscapes, sharpness, curvature, and optimizer-state dynamics.
- Training instabilities such as edge-of-stability behavior and delayed generalization.

### 2. Representation Learning

- Why learned features are useful abstractions rather than mere compression.
- The role of normalization, residual pathways, and depth in signal propagation.
- How architectural choices influence expressivity and trainability.

### 3. Generalization

- Double descent and the limits of classical bias-variance narratives.
- Benign overfitting and interpolation in over-parameterized models.
- How data quality, scale, and augmentation change what generalization means.

## Frontier Topics Worth Tracking

- **Scaling laws** and compute-optimal training.
- **NTK and infinite-width perspectives** as a limit case, not a full explanation.
- **Mechanistic views of training dynamics** such as grokking and phase transitions.
- **Data-centric theory** for curation, filtering, and synthetic data generation.

## What I Want To Publish Here

- Derivations that make research papers easier to read.
- Notes that connect theoretical claims to empirical behavior.
- Small experiments that test intuitions before accepting a narrative.

## Latest Notes

- [Generalization in the Overparameterized Era](generalization-overparameterization.md)
- [Scaling Laws and Compute-Optimal Training](scaling-laws-compute-optimal-training.md)

## Key Resources

- **Book**: [Deep Learning](https://www.deeplearningbook.org/) by Goodfellow, Bengio, and Courville.
- **Course**: [Practical Deep Learning for Coders](https://course.fast.ai/) for intuition that complements formal theory.
- **Visuals**: [Distill](https://distill.pub/) for clear interactive explanations.

<!-- ## The Attention Mechanism

The core of the Transformer architecture is the Scaled Dot-Product Attention.

The attention function implies mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

### Mathematical Formulation

Given queries $Q$, keys $K$, and values $V$, the attention matrix is calculated as:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Where:

*   $Q \in \mathbb{R}^{n \times d_k}$
*   $K \in \mathbb{R}^{m \times d_k}$
*   $V \in \mathbb{R}^{m \times d_v}$
*   $d_k$ is the dimension of the keys (and queries).

!!! note "Why Scale by $\sqrt{d_k}$?"
    We divide by $\sqrt{d_k}$ to prevent the dot products from growing too large in magnitude. If the dot products are large, the gradient of the softmax function becomes extremely small ("vanishing gradients"), leading to hard training.

### Multi-Head Attention

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions.

$$
\begin{aligned}
\text{MultiHead}(Q, K, V) &= \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O \\
\text{where } \text{head}_i &= \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)
\end{aligned}
$$ -->
