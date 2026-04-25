---
title: AI Systems
summary: Training, serving, and operating modern AI workloads from cluster design to GPU systems.
status: evergreen
updated: 2026-04-24
tags:
  - ai systems
  - distributed training
  - inference
---

<div class="hero-shell section-hero systems-hero">
<p class="hero-eyebrow">Execution Layer</p>

<h1>AI Systems</h1>

<p class="hero-lead">This section is about the machinery that makes modern AI possible in practice: distributed training, serving, GPU systems, memory behavior, scheduling, and the tradeoffs that determine whether a model is merely impressive or actually deployable.</p>

<div class="chip-row">
<span class="chip">Distributed training</span>
<span class="chip">Inference systems</span>
<span class="chip">Goodput</span>
<span class="chip">GPU systems</span>
</div>

<div class="hero-actions">
<a class="md-button md-button--primary" href="distributed-training-playbook/">Read Distributed Training Playbook</a>
<a class="md-button" href="prefill-decode-goodput/">Read Prefill, Decode, and Goodput</a>
</div>
</div>

<div class="hub-grid">
<div class="hub-panel">
<h3>Start Here</h3>
<ul class="link-stack">
  <li><a href="distributed-training-playbook/">Distributed Training Playbook</a></li>
  <li><a href="prefill-decode-goodput/">Prefill, Decode, and Goodput</a></li>
  <li><a href="../cuda/">GPU Systems &amp; CUDA</a></li>
  <li><a href="../research-notes/reading-maps/efficient-llm-inference/">Reading Map: Efficient LLM Inference</a></li>
</ul>
</div>

<div class="hub-panel">
<h3>Systems Playbook</h3>
<ul>
  <li>Use DDP when the model fits and you need straightforward scale-out.</li>
  <li>Use ZeRO or FSDP when replicated model state is the main memory problem.</li>
  <li>Use tensor or pipeline parallelism when layer size or stage partitioning becomes the real constraint.</li>
  <li>Optimize serving for TTFT, TPOT, and goodput rather than raw throughput alone.</li>
</ul>
</div>

<div class="hub-panel">
<h3>Latest Notes</h3>
<ul class="link-stack">
  <li><a href="distributed-training-playbook/">Distributed Training Playbook</a></li>
  <li><a href="prefill-decode-goodput/">Prefill, Decode, and Goodput</a></li>
  <li><a href="../research-notes/roundups/2026-04-kv-cache-optimization/">April 2026 Roundup: KV Cache Optimization Becomes A Systems Problem</a></li>
  <li><a href="../research-notes/reading-maps/efficient-llm-inference/">Reading Map: Efficient LLM Inference</a></li>
</ul>
</div>
</div>

## Why CUDA Lives Here

CUDA is nested under AI Systems because it is part of the execution substrate: hardware-software interaction, profiling, kernel design, and memory behavior. Efficient AI stays separate because it focuses on model-level efficiency techniques rather than GPU programming itself.

## Research Radar

Updated April 24, 2026.

This radar now prefers 2025-2026 systems work. A 2024 paper stays only if it clearly shaped the current serving stack or remains the most useful public systems reference.

### Active Directions

- Prefill and decode are no longer a simple binary design choice; newer systems are explicitly blending aggregation and disaggregation based on SLO mix and goodput targets.
- KV-cache management is becoming a storage-hierarchy problem spanning HBM, CPU memory, and SSD, with cache-aware scheduling and adaptive compression.
- Prompt reuse and prefix-aware scheduling are becoming first-class runtime policies rather than isolated optimizations.
- Serving systems are increasingly co-designed with hardware assumptions, especially around decode bandwidth, communication overhead, and tiered memory.
- Training-side systems work remains centered on practical combinations of FSDP, ZeRO, tensor parallelism, and pipeline parallelism, but the public frontier is moving fastest on inference stacks.

### Keywords To Track

`TTFT`, `TPOT`, `goodput`, `prefill-decode disaggregation`, `disaggregation-aggregation`, `hierarchical KV cache`, `cache-aware scheduling`, `prefix reuse`, `request migration`, `FSDP`, `ZeRO`

### Recent Papers By Direction

#### Prefill / Decode Serving Architectures

- [Prefill-Decode Aggregation or Disaggregation? Unifying Both for Goodput-Optimized LLM Serving](https://arxiv.org/abs/2508.01989) (2025)
- [Disaggregated Prefill and Decoding Inference System for Large Language Model Serving on Multi-Vendor GPUs](https://arxiv.org/abs/2509.17542) (2025)
- [SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference](https://arxiv.org/abs/2510.08544) (2025)
- [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://arxiv.org/abs/2401.09670) (2024, kept as the impact reference that pushed disaggregation into the mainstream)
- [P/D-Serve: Serving Disaggregated Large Language Model at Scale](https://arxiv.org/abs/2408.08147) (2024, kept as an important deployment-oriented follow-up)

#### Hierarchical KV Cache And Memory Management

- [Strata: Hierarchical Context Caching for Long Context Language Model Serving](https://arxiv.org/abs/2508.18572) (2025)
- [AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving](https://arxiv.org/abs/2509.00105) (2025)
- [Adaptive Multi-Objective Tiered Storage Configuration for KV Cache in LLM Service](https://arxiv.org/abs/2603.08739) (2026)
- [Mell: Memory-Efficient Large Language Model Serving via Multi-GPU KV Cache Management](https://arxiv.org/abs/2501.06709) (2025)
- [Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving](https://arxiv.org/abs/2407.00079) (2024, kept as a defining KV-cache-centric architecture paper)

#### Prefix Reuse And Runtime Scheduling

- [Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving](https://arxiv.org/abs/2504.07494) (2025)
- [Preble: Efficient Distributed Prompt Scheduling for LLM Serving](https://arxiv.org/abs/2407.00023) (2024, kept because prompt-sharing is still a core systems pattern)

### Sources To Follow

- [vLLM Documentation](https://docs.vllm.ai/)
- [PyTorch FSDP Documentation](https://docs.pytorch.org/docs/stable/fsdp.html)
- [NVIDIA TensorRT-LLM Documentation](https://docs.nvidia.com/tensorrt-llm/index.html)
- [LMCache Documentation](https://docs.lmcache.ai/)
- [OpenReview](https://openreview.net/) for current systems papers before they settle into surveys

### Canonical References Worth Keeping

- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054)
- [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)

## Key Resources

- **Course**: [CS329S: Machine Learning Systems Design](https://stanford-cs329s.github.io/).
- **Blog**: [Chip Huyen's blog](https://huyenchip.com/).
- **Paper**: [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473).
