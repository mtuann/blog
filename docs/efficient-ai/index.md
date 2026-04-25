---
title: Efficient AI
summary: Live research directions in quantization, speculative decoding, efficient architectures, and model-level efficiency.
status: evergreen
updated: 2026-04-24
tags:
  - efficient ai
  - quantization
  - inference
---

This page is a living map of model-level efficiency research. It focuses on techniques that change the compute, memory, or algorithmic cost profile inside the model stack; cluster orchestration and serving-runtime decisions stay under AI Systems.

## Topic Map

- **Quantization and low-precision training**
  This is no longer just about fitting models into memory. The real research question is which low-bit schemes preserve useful optimization dynamics and which ones merely create brittle benchmark wins.
- **Cache compression and reuse**
  KV-cache work belongs here when it changes the effective memory footprint or algorithmic behavior of the model, not merely the runtime scheduler around it.
- **Speculative and accelerated decoding**
  The frontier has moved from draft models to self-speculation, partial verification, and other schemes that reduce serial generation cost without collapsing output quality.
- **Efficient architectures**
  The interesting question is no longer “attention or not?” but which hybrid combinations of attention, state-space, and memory mechanisms actually shift the cost-quality frontier.
- **Boundary with AI Systems**
  If the main question is orchestration, serving topology, or hardware scheduling, it belongs under AI Systems. If the main question is changing FLOPs, memory, or the model’s own execution pattern, it belongs here.

## Research Questions Right Now

- Which efficiency techniques still help when evaluated end-to-end rather than in isolated kernel or benchmark settings?
- When does quantization change the optimization problem itself, rather than just the final deployment format?
- Which cache-compression schemes generalize across long-context, multimodal, and reasoning-heavy workloads?
- How much speculative decoding speedup remains after verification cost and failure cases are measured honestly?
- Which efficient architectures are genuinely new regimes, and which are just temporary workarounds for current hardware bottlenecks?

## Research Radar

Updated April 24, 2026.

This radar leans toward 2025-2026 work. A 2024 paper remains only when it is still the clearest impact paper for the efficiency pattern.

### Active Directions

- Quantization is increasingly inseparable from kernel design and serving runtime behavior.
- KV-cache compression is moving from toy eviction policies toward hardware-aware, layout-aware, and multimodal-aware methods.
- Speculative decoding is evolving beyond a small draft model into self-speculation, partial verification, and heterogeneous execution.
- Low-precision training is shifting from "can FP8 work?" to "which end-to-end recipe survives scale and real workloads?"
- Efficient architectures are converging on hybrid designs that mix attention with state-space or memory-heavy components rather than betting on a single replacement.

### Keywords To Track

`KV cache compression`, `FP8`, `MXFP4`, `W4A8`, `system co-design`, `self-speculative decoding`, `partial verification`, `Mamba`, `hybrid architectures`, `long-context efficiency`

### Recent Papers And Research Signals By Direction

#### Quantization And Low-Precision Training

- [Hu et al. (2025), LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving](https://arxiv.org/abs/2509.01229)
- [Hernández-Cano et al. (2025), Towards Fully FP8 GEMM LLM Training at Scale](https://arxiv.org/abs/2505.20524)
- [Tseng et al. (2025), Training LLMs with MXFP4](https://arxiv.org/abs/2502.20586)
- [Lin et al. (2024), QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving](https://arxiv.org/abs/2405.04532) (kept as an impact paper)

#### KV Cache Compression And Reuse

- [Gao et al. (2025), Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving](https://arxiv.org/abs/2503.24000)
- [Yang et al. (2025), Revisiting Multimodal KV Cache Compression: A Frequency-Domain-Guided Outlier-KV-Aware Approach](https://arxiv.org/abs/2511.16786)
- [Hao et al. (2026), DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity](https://arxiv.org/abs/2602.08005)
- [Zeng et al. (2026), HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/abs/2604.05887)

#### Speculative And Accelerated Decoding

- [Zhao et al. (2025), Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding](https://arxiv.org/abs/2512.01278)
- [Bhendawade et al. (2025), Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference](https://arxiv.org/abs/2510.13161)
- [Tan et al. (2025), SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification](https://arxiv.org/abs/2512.02337)

#### Efficient Architectures Beyond Dense Attention

- [Bae et al. (2025), Hybrid Architectures for Language Models: Systematic Analysis and Design Insights](https://arxiv.org/abs/2510.04800)
- [Mitra et al. (2025), Characterizing State Space Model and Hybrid Language Model Performance with Long Context](https://arxiv.org/abs/2507.12442)

### Related Notes

- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
- [April 2026 Roundup: KV Cache Optimization Becomes A Systems Problem](../research-notes/roundups/2026-04-kv-cache-optimization.md)

## Site Coverage

- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
  The best internal guide for inference papers that touch this topic from multiple angles.
- [April 2026 Roundup: KV Cache Optimization Becomes A Systems Problem](../research-notes/roundups/2026-04-kv-cache-optimization.md)
  A narrower internal note focused on the cache frontier where efficiency and systems begin to overlap.
- [AI Systems](../ai-systems/index.md)
  The place to go when a question stops being about model cost structure and starts being about runtime orchestration.

## Sources To Follow

- [vLLM Documentation](https://docs.vllm.ai/)
- [Hugging Face Quantization Guide](https://huggingface.co/docs/optimum/concept_guides/quantization)
- [NVIDIA TensorRT-LLM Documentation](https://docs.nvidia.com/tensorrt-llm/index.html)
- [OpenReview](https://openreview.net/)

## Open Backlog

- A dedicated note on quantization as a research area, not just an inference trick: W4A8, FP8, MXFP4, and what “fair comparison” should mean.
- A reading map on speculative decoding families and the failure modes hidden by synthetic workloads.
- A deeper note on KV-cache compression across language-only and multimodal settings.
- A research note on efficient architectures after Mamba, with explicit criteria for what counts as a real frontier shift.
- A boundary note explaining where Efficient AI should hand off to AI Systems and where it should not.
