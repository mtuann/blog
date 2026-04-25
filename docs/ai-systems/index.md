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

<div class="hero-shell section-hero systems-hero" markdown>
<p class="hero-eyebrow">Execution Layer</p>

# AI Systems

<p class="hero-lead">This section is about the machinery that makes modern AI possible in practice: distributed training, serving, GPU systems, memory behavior, scheduling, and the tradeoffs that determine whether a model is merely impressive or actually deployable.</p>

<div class="chip-row">
<span class="chip">Distributed training</span>
<span class="chip">Inference systems</span>
<span class="chip">Goodput</span>
<span class="chip">GPU systems</span>
</div>

<div class="hero-actions" markdown>
[Read Distributed Training Playbook](distributed-training-playbook.md){ .md-button .md-button--primary }
[Read Prefill, Decode, and Goodput](prefill-decode-goodput.md){ .md-button }
</div>
</div>

<div class="hub-grid">
<div class="hub-panel" markdown>
### Start Here

- [Distributed Training Playbook](distributed-training-playbook.md)
- [Prefill, Decode, and Goodput](prefill-decode-goodput.md)
- [GPU Systems & CUDA](../cuda/index.md)
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
</div>

<div class="hub-panel" markdown>
### Systems Playbook

- Use DDP when the model fits and you need straightforward scale-out.
- Use ZeRO or FSDP when replicated model state is the main memory problem.
- Use tensor or pipeline parallelism when layer size or stage partitioning becomes the real constraint.
- Optimize serving for TTFT, TPOT, and goodput rather than raw throughput alone.
</div>

<div class="hub-panel" markdown>
### Latest Notes

- [Distributed Training Playbook](distributed-training-playbook.md)
- [Prefill, Decode, and Goodput](prefill-decode-goodput.md)
- [April 2026 Roundup: KV Cache Optimization Becomes A Systems Problem](../research-notes/roundups/2026-04-kv-cache-optimization.md)
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
</div>
</div>

## Why CUDA Lives Here

CUDA is nested under AI Systems because it is part of the execution substrate: hardware-software interaction, profiling, kernel design, and memory behavior. Efficient AI stays separate because it focuses on model-level efficiency techniques rather than GPU programming itself.

## Key Resources

- **Course**: [CS329S: Machine Learning Systems Design](https://stanford-cs329s.github.io/).
- **Blog**: [Chip Huyen's blog](https://huyenchip.com/).
- **Paper**: [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473).
