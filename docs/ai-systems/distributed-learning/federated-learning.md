---
title: Federated Learning
summary: Live research directions in cross-device and cross-silo learning, personalization, private foundation-model adaptation, and federated unlearning.
status: evergreen
updated: 2026-04-24
tags:
  - federated learning
  - distributed learning
  - privacy
  - foundation models
---

This page is a living map of federated-learning research. It focuses on cross-device and cross-silo collaboration, non-IID personalization, privacy-preserving foundation-model adaptation, and federated unlearning; datacenter-scale parallel training stays under Distributed Learning, while serving and kernel questions stay under AI Systems and GPU Systems & CUDA.

## Topic Map

- **Cross-device and cross-silo federations**
  The original mobile-device setting is still important, but newer work increasingly targets hospitals, labs, enterprises, and scientific facilities that cannot centralize raw data.
- **Personalization under non-IID data**
  The core challenge is no longer only how to aggregate, but how to preserve client-specific structure without collapsing into a weak global compromise.
- **Foundation-model and PEFT-based federated fine-tuning**
  LoRA, adapters, prompt tuning, and related PEFT objects are turning federated learning into a realistic adaptation mechanism for large pretrained models.
- **Privacy, secure aggregation, and leakage**
  Federated learning is not automatically private; the research frontier now includes stronger privacy accounting, attack auditing, and leakage analysis for PEFT-based updates.
- **Federated unlearning and governance**
  If federated systems are going to be used in regulated domains, they must support deletion requests, auditable forgetting, and realistic verification.
- **Asynchrony and systems constraints**
  Real federations have partial participation, slow clients, unstable links, and heterogeneous devices, so protocol design matters as much as model design.

## Research Questions Right Now

- What is the right aggregation object for federated foundation-model adaptation: adapter weights, low-rank subspaces, Gram matrices, task vectors, or routed experts?
- Which personalization abstractions scale from classic federated learning to LLM and multimodal adaptation without exploding client-side cost?
- How should federated learning be evaluated once client churn, system heterogeneity, and partial participation matter as much as headline accuracy?
- Which privacy guarantees survive practical attacks on adapter-based or PEFT-based federated fine-tuning?
- Which workloads are the strongest long-term fit for federated foundation models: on-device adaptation, regulated-domain collaboration, scientific cross-facility training, or multimodal personalization?

## Research Radar

Updated April 24, 2026.

This radar prefers 2025-2026 work. Older references stay only when they remain the clearest foundation for a still-active direction.

### Active Directions

- Federated fine-tuning is shifting toward parameter-efficient objects such as LoRA and adapters rather than full-model synchronization.
- Personalization is moving from simple local heads toward task-vector, graph-based, or expert-routed aggregation schemes.
- Federated unlearning is becoming a first-class problem because privacy regulation requires removal, not only training.
- Cross-silo and scientific federations are expanding beyond mobile roots, especially where data cannot leave facilities or jurisdictions.
- Privacy auditing is catching up with PEFT-based FL as newer work shows adapter-only updates can still leak training data.

### Keywords To Track

`cross-device FL`, `cross-silo FL`, `FedLLM`, `federated PEFT`, `LoRA aggregation`, `personalization`, `secure aggregation`, `differential privacy`, `federated unlearning`, `client churn`

### Recent Papers And Research Signals By Direction

#### Foundation-Model And Adapter-Based Federated Fine-Tuning

- [A Survey on Federated Fine-tuning of Large Language Models](https://arxiv.org/abs/2503.12016) (2025, useful as the current survey anchor for the FedLLM space)
- [Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA](https://arxiv.org/abs/2502.01755) (2025)
- [FLoRG: Federated Fine-tuning with Low-rank Gram Matrices and Procrustes Alignment](https://openreview.net/forum?id=kntrZOm2AQ) (ICLR 2026 Poster)
- [Rethinking LoRA Aggregation for Federated Fine-tuning of Foundation Models](https://openreview.net/forum?id=k5SgTEKdA2) (ICLR 2026 submission)
- [Developmental Federated Tuning: A Cognitive-Inspired Paradigm for Efficient LLM Adaptation](https://openreview.net/forum?id=htbzmulSaG) (ICLR 2026 Poster)

#### Personalization Under Heterogeneity

- [Bi-level Personalization for Federated Foundation Models: A Task-vector Aggregation Approach](https://arxiv.org/abs/2509.12697) (2025)
- [TAP: Two-Stage Adaptive Personalization of Multi-task and Multi-Modal Foundation Models in Federated Learning](https://openreview.net/forum?id=bXTDrSo0ya) (ICLR 2026 submission)
- [Representation-Aligned Multi-Scale Personalization for Federated Learning](https://openreview.net/forum?id=LGomq5co14) (ICLR 2026 submission)
- [FLEx: Personalized Federated Learning for Mixture-of-Experts LLMs via Expert Grafting](https://openreview.net/forum?id=T4dvY146Tk) (ICLR 2026 withdrawn submission, still useful as a signal that MoE-style personalization is emerging)

#### Privacy, Leakage, And Unlearning

- [Reconstructing Training Data from Adapter-based Federated Large Language Models](https://arxiv.org/abs/2601.17533) (2026)
- [Understanding Federated Unlearning through the Lens of Memorization](https://openreview.net/forum?id=jUGWx29UHK) (ICLR 2026 submission)
- [Exact Federated Continual Unlearning for Ridge Heads on Frozen Foundation Models](https://arxiv.org/abs/2603.12977) (2026)
- [FedQUIT: On-Device Federated Unlearning via a Quasi-Competent Virtual Teacher](https://openreview.net/forum?id=BLYR9Fm7PI) (ICLR 2026 submission)

#### Cross-Silo, Multimodal, And Scientific Federations

- [Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers](https://arxiv.org/abs/2603.19544) (2026)
- [FeDaL: Federated Dataset Learning for General Time Series Foundation Models](https://openreview.net/forum?id=HK6t5x5gJq) (ICLR 2026 Poster)
- [FedMosaic: Federated Retrieval-Augmented Generation via Parametric Adapters](https://arxiv.org/abs/2602.05235) (2026)
- [Federated Foundation Models in Harsh Wireless Environments: Prospects, Challenges, and Future Directions](https://arxiv.org/abs/2509.01957) (2025, kept as a good systems-framing reference for hostile deployment settings)

### Related Notes

- [FedLLM Aggregation Objects](./fedllm-aggregation-objects.md)
- [Distributed Learning](./index.md)
- [Distributed Training Playbook](../distributed-training-playbook.md)
- [AI Systems](../index.md)

## Site Coverage

- [Distributed Learning](./index.md)
  The parent map for datacenter-scale parallel training, communication efficiency, and resilience questions that sit next to federated learning.
- [Distributed Training Playbook](../distributed-training-playbook.md)
  The current internal note for the main distributed-training abstractions that often interact with cross-silo system design.
- [FedLLM Aggregation Objects](./fedllm-aggregation-objects.md)
  A focused comparison of what the server should actually aggregate: LoRA factors, subspaces, Gram matrices, task vectors, or routed experts.

## Sources To Follow

- [Flower Framework Documentation](https://flower.ai/docs/framework/index.html)
- [TensorFlow Federated](https://www.tensorflow.org/federated/federated_learning)
- [Using TFF for Federated Learning Research](https://www.tensorflow.org/federated/tff_for_research)
- [FedML Octopus User Guide](https://fedml-ai.github.io/FedML-Doc/cross-silo/user_guide.html)

## Open Backlog

- A deeper page on personalization for federated foundation models, especially how group-wise aggregation differs from per-client adaptation.
- A focused note on federated unlearning and verification, separating legal deletion claims from measurable forgetting.
- A systems note on cross-silo federations for healthcare, enterprise, and scientific settings where communication and trust assumptions differ sharply from mobile FL.
- A future comparison page for Flower, TensorFlow Federated, and FedML from the perspective of what research questions each framework makes easiest to test.
