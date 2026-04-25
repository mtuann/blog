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

## Key Resources

- **Course**: [CS329S: Machine Learning Systems Design](https://stanford-cs329s.github.io/).
- **Blog**: [Chip Huyen's blog](https://huyenchip.com/).
- **Paper**: [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473).
