---
title: Scaling Laws and Compute-Optimal Training
date: 2026-04-24
updated: 2026-04-24
tags:
  - machine learning
  - theory
  - scaling laws
status: evergreen
series: ml-theory
summary: A note on how scaling laws became useful, how Chinchilla revised the earlier compute-optimal picture, and what lessons still hold.
---

# Scaling Laws and Compute-Optimal Training

Scaling laws changed the tone of modern machine learning because they suggested that improvement was not just a matter of isolated tricks. Across wide ranges of model size, data size, and compute, loss often followed smooth empirical trends. That meant researchers could reason about tradeoffs before training the very largest model in a family.

The important word is **empirical**. These are not laws in the physics sense. They are stable regularities observed over meaningful operating ranges, and they are only useful when we remember what they do and do not promise.

## The Core Idea

Suppose a model family is parameterized by model size $N$ and trained on $D$ tokens. A simplified scaling-law view says that the loss often behaves like

$$
L(N, D) \approx E + \frac{A}{N^\alpha} + \frac{B}{D^\beta},
$$

for constants $A, B, E, \alpha, \beta$ fitted from experiments.

This equation is powerful for two reasons:

1. It turns "train bigger and hope" into a measurable planning problem.
2. It exposes when a training run is limited more by model size or by data.

The famous early reference is [Kaplan et al. (2020), Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), which showed smooth power-law trends over model size, dataset size, and training compute.

## Why This Was So Useful

Before scaling-law thinking, it was easy to discuss model size and dataset size as separate knobs. Scaling laws forced a more disciplined question:

**Given a fixed compute budget, where should the next dollar go?**

That is the real value. Scaling laws are most useful as budgeting tools for:

- model size
- training tokens
- compute allocation
- expected returns from the next scale jump

## The Kaplan-Era Intuition

The early scaling-law story implied that very large models were especially sample-efficient. Under a fixed compute budget, the picture favored training larger models and stopping before convergence rather than trying to train a smaller model to exhaustion.

This was a big conceptual shift:

- bigger models were not just more expressive
- bigger models could also be a better use of compute

That result shaped a lot of early large-model strategy.

## Chinchilla Revised The Rule

The next major update came from [Hoffmann et al. (2022), Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556). The Chinchilla result argued that many large language models had been **undertrained** relative to their parameter count.

The key practical lesson was:

- model size and training tokens should scale together more aggressively than many teams had assumed

At a very rough level, if training compute scales like

$$
C \propto N \cdot D,
$$

then compute-optimal training is not just about buying more parameters. It is about choosing a better balance between parameters and data.

This changed the conversation from:

- "How large can the model be?"

to:

- "Is this model-data pairing actually efficient for the budget?"

## What I Think Is Stable

Several lessons from the scaling-law era still feel durable:

### 1. Smooth trends are strategically useful

Even imperfect scaling curves are valuable because they support planning, forecasting, and sanity checks.

### 2. Compute-optimal is a training concept, not the whole product story

A model that is compute-optimal to train is not automatically optimal to serve. Inference cost, latency, memory footprint, and post-training behavior matter too.

### 3. Data is not a side constraint

Once model families become large enough, data quality and data quantity stop being afterthoughts. They are part of the optimization problem itself.

### 4. Aggregate scaling can hide task-level variation

Validation loss can scale smoothly while individual downstream tasks scale unevenly. That means scaling laws are best used as global guides, not as guarantees for any single benchmark or product capability.

## What This Means For Practice

If I were planning a model family from scratch, I would use scaling-law thinking in this order:

1. Fit small and medium runs carefully.
2. Estimate where the next scale regime is likely to saturate.
3. Ask whether the budget is parameter-limited or data-limited.
4. Compare training efficiency against serving constraints before declaring a configuration optimal.

That last step matters more now than ever. In a product setting, a slightly smaller but better-trained model can be more valuable than a giant model with worse inference economics.

## Common Mistakes

- Treating fitted scaling curves as universal laws rather than local empirical summaries.
- Confusing lower training loss with better downstream behavior on every task.
- Ignoring deployment costs when discussing what is "optimal."
- Using scaling laws as a substitute for evaluation instead of as a complement to it.

## Related Notes

- [Machine Learning Overview](index.md)
- [Machine Learning Theory](theory.md)
- [Generalization in the Overparameterized Era](generalization-overparameterization.md)
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
