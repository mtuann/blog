---
title: Generalization in the Overparameterized Era
date: 2026-04-24
updated: 2026-04-24
tags:
  - machine learning
  - theory
  - generalization
  - double descent
status: evergreen
series: ml-theory
summary: A theory note on why interpolation does not automatically imply bad test error, and how double descent and benign overfitting changed the way we think about generalization.
---

# Generalization in the Overparameterized Era

Modern machine learning forced a revision of one of the cleanest stories in classical statistics. The old intuition said that as model complexity grows, test error should eventually rise because the model starts fitting noise. That intuition is still useful, but it is no longer the whole picture.

Large neural networks often fit the training data almost perfectly and still generalize well. This note explains why that observation was so surprising, what double descent changed, and why benign overfitting is a more careful idea than the phrase first suggests.

## The Classical Story

Let the test risk of a predictor $f$ be

$$
R(f) = \mathbb{E}_{(x, y)}\left[\ell(f(x), y)\right].
$$

In the classical view, increasing model complexity reduces bias at first but eventually increases variance. Under squared loss, this is often summarized as:

$$
\mathbb{E}\left[(\hat{f}(x) - f^\*(x))^2\right]
=
\text{Bias}[\hat{f}(x)]^2 + \text{Var}[\hat{f}(x)] + \sigma^2.
$$

That picture suggests a familiar U-shaped curve:

- too simple: underfit, high bias
- moderately complex: best tradeoff
- too complex: overfit, high variance

For many years, that was the default mental model for model selection.

## Why Deep Learning Broke The Mood

Deep networks made the classical story feel incomplete. In practice:

- very large models could drive training error to nearly zero
- the same models could still achieve strong test performance
- explicit regularization was not always the decisive explanation

That tension was made especially vivid by [Zhang et al. (2016), Understanding Deep Learning Requires Rethinking Generalization](https://arxiv.org/abs/1611.03530), which showed that large networks can even fit random labels. The point was not that generalization vanished, but that naive capacity arguments were no longer enough.

## Double Descent

The next important update was the realization that test error does not always stop at the classical U-shape. Around the **interpolation threshold**, test error can rise sharply and then fall again as models become even more overparameterized.

This produces the now-famous **double descent** curve:

1. a classical descent-then-rise phase
2. a peak near interpolation
3. a second descent in the highly overparameterized regime

The modern ML picture is not "overfitting disappeared." It is that the relationship between capacity and generalization is more structured than the old one-curve story suggested.

Two useful references here are:

- [Reconciling modern machine-learning practice and the classical bias-variance trade-off](https://www.cs.columbia.edu/~djhsu/papers/biasvariance-pnas.pdf)
- [Nakkiran et al. (2019), Deep Double Descent: Where Bigger Models and More Data Hurt](https://arxiv.org/abs/1912.02292)

## A Helpful Mental Model

One way to think about the interpolation regime is this:

- small models cannot represent the signal well
- near interpolation, the model has just enough flexibility to fit both signal and noise awkwardly
- very large models may have enough freedom to fit the training set while still choosing a solution with an unexpectedly favorable inductive bias

That last clause is the key. In modern ML, not all interpolating solutions are equal. Optimization, architecture, normalization, data geometry, and implicit bias all matter.

## Benign Overfitting

The phrase **benign overfitting** sounds contradictory, but the idea is narrower than the slogan. In some overparameterized settings, a model can interpolate noisy training data and still achieve near-optimal prediction risk.

This does **not** mean that fitting noise is always safe. It means there are structured regimes where interpolation is compatible with good generalization.

The most useful clean result is:

- [Bartlett et al. (2019), Benign Overfitting in Linear Regression](https://arxiv.org/abs/1906.11300)

That paper matters because it gives a precise statement in a simple setting. It shows that overparameterization alone is not enough; the covariance structure and effective rank matter too.

## Why This Matters For Practice

These ideas change how we interpret training behavior:

- zero training error is not by itself an indictment
- larger models can be easier to optimize and sometimes easier to generalize with
- the interpolation threshold is often a dangerous regime
- architecture and optimizer bias are part of the statistical story, not just engineering details

This is also why modern model scaling cannot be understood only through VC-dimension-style intuition. The effective solution found by training is often more important than the raw size of the function class.

## What I Think Is Stable

Several lessons feel durable even as the frontier moves:

- Classical bias-variance intuition is still useful locally, but not globally.
- Interpolation is a regime to analyze, not a pathology to dismiss automatically.
- Generalization in deep learning depends on data geometry and optimization bias as much as nominal parameter count.
- Theory is most valuable when it explains which kinds of overparameterization are harmless and which are fragile.

## Where To Go Next

If you want to keep going after this note, the next steps I recommend are:

1. Read the classical bias-variance reconciliation paper for the curve-level intuition.
2. Read the deep double descent paper for the empirical deep-learning version.
3. Read the benign overfitting paper to see a sharp theoretical case.
4. Then revisit scaling laws and implicit regularization with a better mental model.

## Related Notes

- [Machine Learning Overview](index.md)
- [Machine Learning Theory](theory.md)
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
