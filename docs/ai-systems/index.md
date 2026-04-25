---
title: AI Systems
summary: Live research directions in AI serving, runtime design, memory systems, and GPU-aware deployment.
status: evergreen
updated: 2026-04-24
tags:
  - ai systems
  - serving
  - inference
---

This page is a living map of AI systems research around training and serving stacks. It is intentionally biased toward runtime design, serving orchestration, cache and memory behavior, and hardware-aware execution; distributed optimization lives under the Distributed Learning subtopic, and kernel-level performance work lives under GPU Systems & CUDA.

## Topic Map

- **Serving architectures**
  This is the core of the page: prefill/decode decomposition, aggregation versus disaggregation, request routing, and runtime structure for large-model serving.
- **Cache and memory systems**
  KV cache is no longer a local optimization detail. It has become a hierarchy design problem spanning HBM, CPU memory, SSD, and scheduling policy.
- **Scheduling, SLOs, and goodput**
  The field is converging on goodput, latency distribution, and cache efficiency as the metrics that actually matter, rather than raw tokens-per-second.
- **Distributed Learning**
  Training-parallelism research now has enough depth to deserve its own subtrack. Use [Distributed Learning](distributed-learning/index.md) when the question is about FSDP, tensor parallelism, decentralized training, or checkpointing at scale.
- **GPU Systems & CUDA**
  Use [GPU Systems & CUDA](../cuda/index.md) when the question is about kernels, graph capture, compiler/runtime integration, or hardware-generation-specific optimizations.

## Research Questions Right Now

- When should serving stacks aggregate prefill and decode, and when should they disaggregate them?
- What cache tiering policies actually survive real workloads rather than only synthetic benchmarks?
- How should goodput be measured when requests vary wildly in prompt length, generation length, and prefix overlap?
- Which runtime decisions belong in software scheduling, and which now justify custom hardware or hardware-specific serving paths?
- How much of the future serving advantage comes from better algorithms versus better workload shape assumptions?

## Research Radar

Updated April 24, 2026.

This radar prefers 2025-2026 systems work. A 2024 paper stays only if it clearly shaped the current serving stack or remains the most useful public systems reference.

### Active Directions

- Prefill and decode are no longer a simple binary design choice; newer systems are explicitly blending aggregation and disaggregation based on SLO mix and goodput targets.
- KV-cache management is becoming a storage-hierarchy problem spanning HBM, CPU memory, and SSD, with cache-aware scheduling and adaptive compression.
- Prompt reuse and prefix-aware scheduling are becoming first-class runtime policies rather than isolated optimizations.
- Serving systems are increasingly co-designed with hardware assumptions, especially around decode bandwidth, communication overhead, and tiered memory.
- Runtime systems are increasingly evaluated in terms of goodput, tail latency, and cache hit behavior rather than raw tokens-per-second alone.

### Keywords To Track

`TTFT`, `TPOT`, `goodput`, `prefill-decode disaggregation`, `disaggregation-aggregation`, `hierarchical KV cache`, `cache-aware scheduling`, `prefix reuse`, `request migration`, `decode bandwidth`

### Recent Papers And Research Signals By Direction

#### Prefill / Decode Serving Architectures

- [Wang et al. (2025), Prefill-Decode Aggregation or Disaggregation? Unifying Both for Goodput-Optimized LLM Serving](https://arxiv.org/abs/2508.01989)
- [Chen et al. (2025), Disaggregated Prefill and Decoding Inference System for Large Language Model Serving on Multi-Vendor GPUs](https://arxiv.org/abs/2509.17542)
- [Zhang et al. (2025), SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference](https://arxiv.org/abs/2510.08544)
- [Zhong et al. (2024), DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://arxiv.org/abs/2401.09670) (kept as an impact reference)
- [Jin et al. (2024), P/D-Serve: Serving Disaggregated Large Language Model at Scale](https://arxiv.org/abs/2408.08147) (kept as an important deployment follow-up)

#### Hierarchical KV Cache And Memory Management

- [Xie et al. (2025), Strata: Hierarchical Context Caching for Long Context Language Model Serving](https://arxiv.org/abs/2508.18572)
- [Feng et al. (2025), AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving](https://arxiv.org/abs/2509.00105)
- [Zheng et al. (2026), Adaptive Multi-Objective Tiered Storage Configuration for KV Cache in LLM Service](https://arxiv.org/abs/2603.08739)
- [Qianli et al. (2025), Mell: Memory-Efficient Large Language Model Serving via Multi-GPU KV Cache Management](https://arxiv.org/abs/2501.06709)
- [Qin et al. (2024), Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving](https://arxiv.org/abs/2407.00079) (kept as a defining architecture paper)

#### Prefix Reuse And Runtime Scheduling

- [Gao et al. (2025), Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving](https://arxiv.org/abs/2504.07494)
- [Srivatsa et al. (2024), Preble: Efficient Distributed Prompt Scheduling for LLM Serving](https://arxiv.org/abs/2407.00023) (kept because prompt-sharing is still a core systems pattern)

### Related Notes

- [Distributed Learning](distributed-learning/index.md)
- [Prefill, Decode, and Goodput](prefill-decode-goodput.md)
- [April 2026 Roundup: KV Cache Optimization Becomes A Systems Problem](../research-notes/roundups/2026-04-kv-cache-optimization.md)
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)

## Site Coverage

- [Distributed Learning](distributed-learning/index.md)
  The systems-facing training track for hybrid parallelism, communication efficiency, and resilience at scale.
- [Prefill, Decode, and Goodput](prefill-decode-goodput.md)
  The best internal note for the serving metrics and latency tradeoffs that dominate real deployment.
- [GPU Systems & CUDA](../cuda/index.md)
  The kernel and compiler layer beneath the serving/runtime stack.
- [Reading Map: Efficient LLM Inference](../research-notes/reading-maps/efficient-llm-inference.md)
  A guided path through inference papers that complement this overview without making it too dense.

## Sources To Follow

- [vLLM Documentation](https://docs.vllm.ai/)
- [NVIDIA TensorRT-LLM Documentation](https://docs.nvidia.com/tensorrt-llm/index.html)
- [LMCache Documentation](https://docs.lmcache.ai/)
- [OpenReview](https://openreview.net/)

## Open Backlog

- A deeper systems note on aggregation versus disaggregation for prefill/decode under different workload regimes.
- A comparative note on vLLM, TensorRT-LLM, LMCache, and where their abstractions differ in practice.
- A research note on benchmarking methodology for serving: goodput, tail latency, and cache-aware workloads.
- A dedicated page on hierarchical KV-cache design patterns, not just individual papers.
- A future overview of hardware-software co-design in serving, including what is moving into accelerator-specific paths.
