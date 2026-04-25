---
title: FedLLM Aggregation Objects
date: 2026-04-24
updated: 2026-04-24
tags:
  - federated learning
  - fedllm
  - lora
  - mixture of experts
status: evergreen
series: "distributed-learning"
summary: Which object should a federated foundation-model system aggregate: LoRA weights, low-rank subspaces, Gram matrices, task vectors, or routed experts?
---

Backlog item:
Which aggregation object should a FedLLM system use: direct LoRA weights, low-rank subspaces, Gram matrices, task vectors, or expert routing?

As of April 24, 2026, this is one of the central design choices in federated foundation-model adaptation. The answer changes depending on whether the dominant problem is `adapter noise`, `resource heterogeneity`, `privacy`, `group-wise personalization`, or `MoE-style specialization`.

## Why This Matters

- The aggregation object determines what information the server can preserve, suppress, or personalize.
- Two methods with the same local fine-tuning recipe can behave very differently if one aggregates raw LoRA factors and the other aggregates a subspace, Gram matrix, or expert selection pattern.
- This choice also changes communication cost, privacy behavior, and whether heterogeneous clients can participate without padding everything into a single shared shape.
- In practice, this is now a more useful decision axis than the vague question “which FedLLM method is best?”

## Short Answer

- `Direct LoRA aggregation` is still the default baseline and the right first comparison, but naive averaging of LoRA factors creates aggregation noise and conflict under heterogeneity.
- `Low-rank subspace methods` are strongest when clients have different compute budgets, different feasible ranks, or differential privacy pressure; they try to aggregate the adaptation space more carefully than plain factor averaging.
- `Gram-matrix aggregation` is the cleanest recent formulation when the main concern is factor misalignment and decomposition drift rather than personalization.
- `Task-vector aggregation` is the most promising object for group-wise personalization, but the evidence base is still thinner than for LoRA-centric methods.
- `Expert routing or expert grafting` becomes attractive when the base model is already modular or the data heterogeneity is semantic enough that one shared adapter is clearly the wrong abstraction.

## Aggregation Object Map

| Object | What the server aggregates | Best fit | Main tradeoff | Representative reads |
|---|---|---|---|---|
| Direct LoRA weights | The low-rank factors themselves, or a corrected merge of them | Strong baseline, same adapter shape across clients | Susceptible to conflict, cross-term noise, and heterogeneous-rank pain | [Wang et al. (2024), FLoRA](https://openreview.net/forum?id=TcCorXxNJQ), [Chen et al. (2025), RoLoRA](https://arxiv.org/abs/2502.01755), [Li et al. (2026), HFLoRA](https://openreview.net/forum?id=k5SgTEKdA2) |
| Low-rank subspaces / reparameterized factors | A structured low-rank space, sketch, orthogonal basis, or small latent matrix | Resource heterogeneity, DP, or communication bottlenecks | Better geometry, but more machinery and sometimes weaker simplicity | [Singhal et al. (2026), Fed-SB](https://openreview.net/forum?id=87UyFEhzyP), [Lee et al. (2025), FedSVD](https://openreview.net/forum?id=Qq19n9LZ97), [Fang et al. (2026), FSLoRA](https://openreview.net/forum?id=wy41I8a3Mr) |
| Gram matrices | Inner-product structure of a single low-rank matrix | Clean global aggregation with less decomposition ambiguity | Less directly personalized; strongest when one global object is still sensible | [Meng et al. (2026), FLoRG](https://openreview.net/forum?id=kntrZOm2AQ) |
| Task vectors | Client-specific task deltas or task-vector similarities | Group-wise personalization under non-IID data | Evidence is promising but still relatively narrow | [Yang et al. (2025), Bi-level Personalization for Federated Foundation Models](https://arxiv.org/abs/2509.12697), [Jhunjhunwala et al. (2025), FedRPCA](https://arxiv.org/abs/2506.01194) |
| Expert routing / expert grafting | Expert identities, expert mixtures, or shared vs local expert paths | Strong heterogeneity, MoE backbones, multimodal or domain-specialized personalization | Highest modeling flexibility, but also most architecture-specific | [Wang et al. (2025), FedLEASE](https://openreview.net/forum?id=es4TTVGJ9x), [Liu et al. (2025), FLEx](https://arxiv.org/abs/2506.00965) |

## Core Concepts You Need

| Concept | One-line definition | Why it matters here |
|---|---|---|
| Aggregation noise | Error introduced when server-side merging does not match the true low-rank update geometry | This is the main critique of naive LoRA factor averaging |
| Decomposition drift | Instability caused by repeatedly decomposing an aggregate low-rank update into non-unique factors | This is the core issue Gram-matrix methods try to fix |
| Task vector | A model delta used as a representation of what changed for a client or task | Useful when the server wants similarity-aware personalization rather than one global merge |
| Subspace alignment | Keeping client updates comparable even when rank, orientation, or basis differs | Central for heterogeneous-rank or privacy-aware methods |
| Expert routing | Choosing which experts or expert combinations a client should use | Important when the model is sparse or when personalization should stay modular |

## Paper Map

| Paper | Published | Object family | Main contribution | Read this for |
|---|---|---|---|---|
| [Wang et al. (2024), FLoRA](https://openreview.net/forum?id=TcCorXxNJQ) | NeurIPS 2024 poster, September 25, 2024 | Direct LoRA weights | Shows naive LoRA aggregation is mathematically noisy and proposes stacking-based aggregation for heterogeneous ranks | The canonical baseline critique |
| [Chen et al. (2025), RoLoRA](https://arxiv.org/abs/2502.01755) | arXiv February 3, 2025; accepted to NeurIPS 2025 | Direct LoRA weights | Emphasizes alternating optimization over both down- and up-projection matrices | Why “freeze one factor” can be too restrictive |
| [Li et al. (2026), Rethinking LoRA Aggregation for Federated Fine-tuning of Foundation Models](https://openreview.net/forum?id=k5SgTEKdA2) | ICLR 2026 submission, September 19, 2025 | Direct LoRA weights | Studies row-level conflicts and cross-term noise, then proposes conflict-aware regulation and re-decomposition | The sharpest recent critique of direct factor averaging |
| [Singhal et al. (2026), Fed-SB](https://openreview.net/forum?id=87UyFEhzyP) | TMLR accepted, March 5, 2026 | Low-rank subspace / reparameterization | Learns a small square matrix between fixed adapters so exact aggregation happens on the latent object rather than the full factors | The strongest current “aggregate a smaller object” paper |
| [Lee et al. (2025), FedSVD](https://openreview.net/forum?id=Qq19n9LZ97) | NeurIPS 2025 poster, September 18, 2025 | Low-rank subspace / orthogonal basis | Uses server-side SVD refactorization to preserve principal directions and stabilize DP-SGD | The cleanest privacy-oriented subspace paper |
| [Fang et al. (2026), Federated Sketching LoRA](https://openreview.net/forum?id=wy41I8a3Mr) | ICLR 2026 submission, September 18, 2025 | Low-rank subspace / sketching | Lets clients update submatrices of a global LoRA object based on resource constraints | Heterogeneous-rank participation without a single fixed adapter size |
| [Meng et al. (2026), FLoRG](https://openreview.net/forum?id=kntrZOm2AQ) | ICLR 2026 poster, January 26, 2026 | Gram matrices | Aggregates a low-rank Gram matrix and uses Procrustes alignment to reduce decomposition drift | The best current reference for Gram-matrix aggregation |
| [Yang et al. (2025), Bi-level Personalization for Federated Foundation Models](https://arxiv.org/abs/2509.12697) | arXiv September 16, 2025 | Task vectors | Uses client task vectors to form similarity-aware server aggregation groups | The clearest task-vector personalization paper |
| [Jhunjhunwala et al. (2025), FedRPCA](https://arxiv.org/abs/2506.01194) | arXiv June 1, 2025 | Task vectors / merged deltas | Decomposes LoRA updates into common low-rank and client-specific sparse parts, inspired by task arithmetic and model merging | A bridge between task arithmetic and federated aggregation |
| [Wang et al. (2025), FedLEASE](https://openreview.net/forum?id=es4TTVGJ9x) | NeurIPS 2025 poster, September 18, 2025 | Expert routing | Allocates LoRA experts by client clusters and uses adaptive top-`M` selection | Expert selection over multiple LoRA specialists |
| [Liu et al. (2025), FLEx](https://arxiv.org/abs/2506.00965) | arXiv June 1, 2025 | Expert grafting | Freezes pretrained MoE experts, trains grafted local experts, and updates gating | What expert routing looks like when the base model is already MoE |

## Synthesis

### 1. Direct LoRA aggregation is still the right baseline, but no longer the whole story

The foundational move in this line is to keep the aggregation object close to the actual trainable adapter factors. [Wang et al. (2024), FLoRA](https://openreview.net/forum?id=TcCorXxNJQ) is the key canonical anchor because it made the “naive LoRA averaging is mathematically wrong under heterogeneity” critique explicit and gave the field a concrete alternative. [Chen et al. (2025), RoLoRA](https://arxiv.org/abs/2502.01755) pushes this line by arguing that both projections should remain expressive, while [Li et al. (2026), HFLoRA](https://openreview.net/forum?id=k5SgTEKdA2) sharpens the diagnosis around row-level conflict and cross-term noise.

This family is still the best default if you want the simplest mental model and strong baselines. If a new method cannot beat a corrected direct-LoRA baseline, it probably should not change your system design.

### 2. Low-rank subspace methods are the most important competing family

The moment clients no longer share the same feasible rank, or differential privacy becomes central, the server often wants to aggregate a more stable low-dimensional object than the raw LoRA factors.

[Singhal et al. (2026), Fed-SB](https://openreview.net/forum?id=87UyFEhzyP) is the most important recent paper here because it pushes the aggregation target into a tiny square matrix and claims exact updates on that latent object, with TMLR acceptance on March 5, 2026. [Lee et al. (2025), FedSVD](https://openreview.net/forum?id=Qq19n9LZ97) is the strongest privacy-oriented representative because it periodically re-orthogonalizes the low-rank representation, while [Fang et al. (2026), FSLoRA](https://openreview.net/forum?id=wy41I8a3Mr) makes the resource-heterogeneity story explicit through client-specific sketching ratios.

If the practical bottleneck is `heterogeneous ranks`, `privacy noise`, or `communication budget`, this family is currently the most compelling alternative to direct factor aggregation.

### 3. Gram matrices are the cleanest recent mathematical reformulation

[Meng et al. (2026), FLoRG](https://openreview.net/forum?id=kntrZOm2AQ), published as an ICLR 2026 poster on January 26, 2026, is the clearest argument that the aggregation object should be the geometry of the low-rank update rather than its raw decomposition. Its core contribution is to aggregate a low-rank Gram matrix and then control decomposition drift with Procrustes alignment.

Conceptually, this is the cleanest paper in the space. The tradeoff is that it is optimized for a strong global object, not for the most aggressive notion of personalization.

### 4. Task vectors are the best current route to grouped personalization

Task-vector aggregation is attractive because it lets the server ask “which clients should share updates?” before asking “how should I average them?” [Yang et al. (2025), Bi-level Personalization for Federated Foundation Models](https://arxiv.org/abs/2509.12697) is the cleanest direct paper in this line. [Jhunjhunwala et al. (2025), FedRPCA](https://arxiv.org/abs/2506.01194) is also useful here because it explicitly decomposes client updates into common and client-specific components, borrowing intuition from task arithmetic and model merging.

This family feels promising, but the evidence is still thinner than for LoRA-centric or subspace-centric methods. Right now it looks best for `group-wise personalization`, not yet as a universal server object for all FedLLM settings.

### 5. Expert routing and grafting are the highest-upside but least universal option

This family changes the question entirely: instead of searching for one merged low-rank update, it tries to decide which experts should exist, which clients should use them, and which parts remain shared. [Wang et al. (2025), FedLEASE](https://openreview.net/forum?id=es4TTVGJ9x) is the strongest current paper if the experts themselves are LoRA modules. [Liu et al. (2025), FLEx](https://arxiv.org/abs/2506.00965) is the clearer MoE-native version, where pretrained experts are preserved and client-specific experts are grafted and routed by the gate.

This is the right direction when heterogeneity is semantic enough that a single shared adapter is obviously too blunt. But it is not yet a general-purpose default, because it assumes more architectural commitment and more routing complexity than the other families.

## Evidence And Benchmark Caveats

| Evidence pattern | What it is useful for | What it does not settle |
|---|---|---|
| Non-IID benchmark gains on language tasks | Whether the aggregation object helps under client heterogeneity | Whether the method survives real cross-silo deployment constraints |
| MMLU or knowledge-preservation checks | Whether personalization destroys general world knowledge | Whether the method helps on domain-specific private tasks |
| DP-SGD evaluations | Whether the representation is robust to privacy noise | Whether the same gains hold without privacy constraints |
| Communication-cost claims | Whether the server object is lighter to move around | Whether the full system is simpler to maintain or debug |

The literature is still heavily benchmark-driven. Most papers use simulated federated splits rather than real regulated cross-silo deployments, so strong paper results should still be treated as `evidence for an aggregation object`, not `proof of deployment readiness`.

## Practical Recommendation

If I had to choose an evaluation ladder today, I would compare in this order:

1. `Corrected direct LoRA aggregation`
   Start with [Wang et al. (2024), FLoRA](https://openreview.net/forum?id=TcCorXxNJQ) or [Chen et al. (2025), RoLoRA](https://arxiv.org/abs/2502.01755) as the baseline family.
2. `Subspace or reparameterized aggregation`
   Move to [Singhal et al. (2026), Fed-SB](https://openreview.net/forum?id=87UyFEhzyP) if communication or privacy is the bottleneck, and to [Fang et al. (2026), FSLoRA](https://openreview.net/forum?id=wy41I8a3Mr) if client ranks differ sharply.
3. `Gram-matrix aggregation`
   Use [Meng et al. (2026), FLoRG](https://openreview.net/forum?id=kntrZOm2AQ) when the main concern is stable global aggregation and decomposition consistency.
4. `Task-vector aggregation`
   Use [Yang et al. (2025), Bi-level Personalization for Federated Foundation Models](https://arxiv.org/abs/2509.12697) when clients should be clustered by task similarity rather than forced into one merge.
5. `Expert routing or grafting`
   Use [Wang et al. (2025), FedLEASE](https://openreview.net/forum?id=es4TTVGJ9x) or [Liu et al. (2025), FLEx](https://arxiv.org/abs/2506.00965) only when the heterogeneity is large enough to justify modular specialization.

## Recommended Reading Order

1. [Wu et al. (2026), A Survey on Federated Fine-Tuning of Large Language Models](https://openreview.net/forum?id=rnCqbuIWnn)
   The current survey anchor, accepted by TMLR on February 13, 2026.
2. [Wang et al. (2024), FLoRA](https://openreview.net/forum?id=TcCorXxNJQ)
   The canonical “why naive LoRA averaging is not enough” paper.
3. [Singhal et al. (2026), Fed-SB](https://openreview.net/forum?id=87UyFEhzyP)
   The strongest current case for aggregating a smaller latent object instead of full LoRA factors.
4. [Meng et al. (2026), FLoRG](https://openreview.net/forum?id=kntrZOm2AQ)
   The cleanest recent mathematical reformulation.
5. [Yang et al. (2025), Bi-level Personalization for Federated Foundation Models](https://arxiv.org/abs/2509.12697)
   The sharpest read if your real question is personalization rather than global merging.
6. [Wang et al. (2025), FedLEASE](https://openreview.net/forum?id=es4TTVGJ9x) or [Liu et al. (2025), FLEx](https://arxiv.org/abs/2506.00965)
   Read these only if you think expert structure should be part of the aggregation object itself.

## Suggested Next Steps

- What to read:
  Pair [Wang et al. (2024), FLoRA](https://openreview.net/forum?id=TcCorXxNJQ) with [Meng et al. (2026), FLoRG](https://openreview.net/forum?id=kntrZOm2AQ) to see the shift from factor averaging to geometry-aware aggregation.
- What to read:
  Pair [Singhal et al. (2026), Fed-SB](https://openreview.net/forum?id=87UyFEhzyP) with [Lee et al. (2025), FedSVD](https://openreview.net/forum?id=Qq19n9LZ97) if privacy or communication limits are the main system constraint.
- What to compare:
  Compare `Fed-SB` versus `FLoRG` on the same non-IID split. This is the cleanest current test of `latent subspace object` versus `Gram-matrix object`.
- What to compare:
  Compare `Bi-level task-vector aggregation` versus `FedLEASE` when the downstream question is personalization. This tests whether grouped deltas or modular experts are the better abstraction.
- What to build:
  Build a small ablation where clients differ in feasible LoRA rank. This is the fastest way to see whether your setting really needs subspace-aware aggregation instead of a corrected direct-LoRA baseline.

## Open Questions

- Can one server object handle both strong personalization and stable global knowledge preservation, or do those goals require different aggregation objects?
- Will Gram-matrix or subspace-based methods remain superior once we move from simulated splits to real cross-silo deployments with client churn?
- Are task vectors a temporary personalization tool, or the beginning of a more general similarity-aware server protocol for FedLLM?
- Will expert routing stay architecture-specific, or become the default aggregation abstraction for heterogeneous multimodal federations?

## Related Notes

- [Federated Learning](./federated-learning.md)
- [Distributed Learning](./index.md)
- [AI Systems](../index.md)
