---
title: Reading Map - Efficient LLM Inference
date: 2026-04-24
updated: 2026-04-24
tags:
  - reading map
  - ai systems
  - efficient ai
  - llm inference
status: evergreen
series: reading-maps
summary: A guided path from transformer attention fundamentals to modern serving systems, kernel work, quantization, and KV-cache management.
---

# Reading Map: Efficient LLM Inference

This reading map is for one question: **how do we get from the math of attention to high-throughput, cost-aware, production-grade LLM serving?**

The trick is to not start with serving infrastructure too early. Efficient inference only makes sense once you understand what the model is computing, where the memory goes, and why prefill and decode behave so differently.

## Stage 0: Internal Prerequisites

- [Transformer & Attention Foundations](../../genai/transformer-attention.md)
- [AI Systems Overview](../../ai-systems/index.md)
- [Efficient AI Overview](../../efficient-ai/index.md)

## Stage 1: Understand The Basic Cost Surface

Start with the original transformer paper:

- [Vaswani et al. (2017), Attention Is All You Need](https://arxiv.org/abs/1706.03762)

What to focus on:

- Why attention creates a dense interaction pattern.
- Why sequence length stresses memory and bandwidth.
- Why efficient inference is not the same problem as efficient training.

## Stage 2: Learn Why Kernels Matter

Then move to IO-aware attention:

- [Dao et al. (2022), FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
- [Dao et al. (2023), FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691)

What to focus on:

- The difference between FLOP counting and memory traffic.
- Why better tiling and work partitioning can change practical performance dramatically.
- How kernel design shapes which architectural ideas are actually deployable.

## Stage 3: Shift From Kernels To Serving State

Once attention kernels make sense, move to serving-time memory management:

- [Kwon et al. (2023), Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)

What to focus on:

- Why KV-cache fragmentation becomes a batch-size limiter.
- Why serving systems need virtual-memory style ideas.
- How a systems abstraction can unlock throughput without changing the model.

## Stage 4: Understand Serving Architecture

Now look at phase-aware and disaggregated serving:

- [Zhong et al. (2024), DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://arxiv.org/abs/2401.09670)
- [Qin et al. (2024), Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving](https://arxiv.org/abs/2407.00079)
- [Lee et al. (2024), InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management](https://arxiv.org/abs/2406.19707)

What to focus on:

- Why prefill and decode want different resource allocations.
- How serving architectures change the meaning of "bottleneck."
- Why cache placement and movement are now as important as raw model execution.

## Stage 5: Study Efficiency Co-Design

After the serving architecture papers, look at system-aware efficiency:

- [Lin et al. (2024), QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving](https://arxiv.org/abs/2405.04532)
- [Gao et al. (2025), Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving](https://arxiv.org/abs/2503.24000)
- [Hao et al. (2026), DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity](https://arxiv.org/abs/2602.08005)
- [Zeng et al. (2026), HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/abs/2604.05887)

What to focus on:

- Which efficiency ideas survive contact with hardware and deployment complexity.
- When quantization or cache compression helps throughput versus only reducing memory footprint.
- Why multimodal and long-context workloads stress different parts of the system.

## If You Only Have One Weekend

Read these in order:

1. [Transformer & Attention Foundations](../../genai/transformer-attention.md)
2. [Dao et al. (2022), FlashAttention](https://arxiv.org/abs/2205.14135)
3. [Kwon et al. (2023), PagedAttention](https://arxiv.org/abs/2309.06180)
4. [Zhong et al. (2024), DistServe](https://arxiv.org/abs/2401.09670)
5. [Gao et al. (2025), Rethinking KV Cache Compression](https://arxiv.org/abs/2503.24000)

That sequence gives you a strong mental model from algorithm to deployment.

## Open Questions

- Which KV-cache compression methods remain attractive once implementation overhead is included?
- When does disaggregated serving beat a simpler colocated design in practice?
- How should we think about efficient inference for multimodal models where visual tokens dominate the cache?

## Related Notes

- [April 2026 Roundup: KV Cache Optimization](../roundups/2026-04-kv-cache-optimization.md)
- [GPU Systems & CUDA](../../cuda/index.md)
- [Paper Reviews](../../paper-reviews/index.md)
