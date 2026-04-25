---
title: Efficient AI
summary: Model-level efficiency techniques for training and serving large models under real resource constraints.
status: evergreen
updated: 2026-04-24
tags:
  - efficient ai
  - quantization
  - inference
---

<div class="hero-shell section-hero efficiency-hero">
<p class="hero-eyebrow">Model Efficiency</p>

<h1>Efficient AI</h1>

<p class="hero-lead">This section focuses on efficiency techniques at the model and algorithm level: compression, quantization, sparse computation, efficient architectures, and inference tricks that change the cost profile of real workloads.</p>

<div class="chip-row">
<span class="chip">Quantization</span>
<span class="chip">Sparsity</span>
<span class="chip">Efficient architectures</span>
<span class="chip">Inference optimization</span>
</div>

<div class="hero-actions">
<a class="md-button md-button--primary" href="../research-notes/reading-maps/efficient-llm-inference/">Read the Inference Reading Map</a>
<a class="md-button" href="../research-notes/roundups/2026-04-kv-cache-optimization/">Read the KV Cache Roundup</a>
</div>
</div>

<div class="hub-grid">
<div class="hub-panel">
<h3>Main Tracks</h3>
<ul>
  <li>Quantization and compression</li>
  <li>Efficient architectures beyond standard attention</li>
  <li>Inference optimization and cache strategy</li>
  <li>Sparsity and pruning</li>
</ul>
</div>

<div class="hub-panel">
<h3>Boundary With AI Systems</h3>
<ul>
  <li>If the question is about clusters, communication, memory hierarchy, or CUDA kernels, it belongs under <strong>AI Systems</strong>.</li>
  <li>If the question is about shrinking the model, reducing FLOPs, or changing the algorithmic cost profile, it belongs here.</li>
</ul>
</div>

<div class="hub-panel">
<h3>Latest Notes</h3>
<ul class="link-stack">
  <li><a href="../research-notes/roundups/2026-04-kv-cache-optimization/">April 2026 Roundup: KV Cache Optimization Becomes A Systems Problem</a></li>
  <li><a href="../research-notes/reading-maps/efficient-llm-inference/">Reading Map: Efficient LLM Inference</a></li>
  <li><a href="../ai-systems/prefill-decode-goodput/">Prefill, Decode, and Goodput</a></li>
</ul>
</div>
</div>

## Research Radar

Updated April 24, 2026.

This radar now leans toward 2025-2026 work. A 2024 paper remains only when it is still the clearest impact paper for the efficiency pattern.

### Active Directions

- Quantization is increasingly inseparable from kernel design and serving runtime behavior.
- KV-cache compression is moving from toy eviction policies toward hardware-aware, layout-aware, and multimodal-aware methods.
- Speculative decoding is evolving beyond a small draft model into self-speculation, partial verification, and heterogeneous execution.
- Low-precision training is shifting from "can FP8 work?" to "which end-to-end recipe survives scale and real workloads?"
- Efficient architectures are converging on hybrid designs that mix attention with state-space or memory-heavy components rather than betting on a single replacement.

### Keywords To Track

`KV cache compression`, `FP8`, `MXFP4`, `W4A8`, `system co-design`, `self-speculative decoding`, `partial verification`, `Mamba`, `hybrid architectures`, `long-context efficiency`

### Recent Papers By Direction

#### Quantization And Low-Precision Training

- [LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving](https://arxiv.org/abs/2509.01229) (2025)
- [Towards Fully FP8 GEMM LLM Training at Scale](https://arxiv.org/abs/2505.20524) (2025)
- [Training LLMs with MXFP4](https://arxiv.org/abs/2502.20586) (2025)
- [QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving](https://arxiv.org/abs/2405.04532) (2024, kept as an impact paper for quantization-plus-systems co-design)

#### KV Cache Compression And Reuse

- [Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving](https://arxiv.org/abs/2503.24000) (2025)
- [Revisiting Multimodal KV Cache Compression: A Frequency-Domain-Guided Outlier-KV-Aware Approach](https://arxiv.org/abs/2511.16786) (2025)
- [DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity](https://arxiv.org/abs/2602.08005) (2026)
- [HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/abs/2604.05887) (2026)

#### Speculative And Accelerated Decoding

- [Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding](https://arxiv.org/abs/2512.01278) (2025)
- [Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference](https://arxiv.org/abs/2510.13161) (2025)
- [SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification](https://arxiv.org/abs/2512.02337) (2025)

#### Efficient Architectures Beyond Dense Attention

- [Hybrid Architectures for Language Models: Systematic Analysis and Design Insights](https://arxiv.org/abs/2510.04800) (2025)
- [Characterizing State Space Model and Hybrid Language Model Performance with Long Context](https://arxiv.org/abs/2507.12442) (2025)

### Sources To Follow

- [vLLM Documentation](https://docs.vllm.ai/)
- [Hugging Face Quantization Guide](https://huggingface.co/docs/optimum/concept_guides/quantization)
- [NVIDIA TensorRT-LLM Documentation](https://docs.nvidia.com/tensorrt-llm/index.html)
- [LMCache Documentation](https://docs.lmcache.ai/)
- [OpenReview](https://openreview.net/) for fresh efficiency and inference papers before the story settles

### Canonical References Worth Keeping

- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
- [FlashAttention-2](https://arxiv.org/abs/2307.08691)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752)

## Key Resources

- **Blog**: [Tim Dettmers' blog](https://timdettmers.com/).
- **Engineering notes**: [vLLM blog](https://blog.vllm.ai/).
- **Paper**: [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314).
