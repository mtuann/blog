---
title: GPU Systems & CUDA
summary: Live research directions in GPU kernels, graph capture, low-precision CUDA engineering, and compiler-driven performance work.
status: evergreen
updated: 2026-04-24
tags:
  - cuda
  - gpu
  - ai systems
---

This page is a living map of GPU-systems and CUDA research. It focuses on live kernel, compiler, graph-capture, and hardware-generation shifts that matter for frontier training and inference stacks, rather than trying to be a beginner roadmap.

## Topic Map

- **Attention and fused kernels**
  This remains the flagship research surface: how to move less data, fuse more work, and match kernel structure to the asymmetries of new hardware generations.
- **Graph capture and runtime materialization**
  CUDA graphs are no longer an implementation footnote. They now shape startup latency, autoscaling behavior, and deployment-time flexibility.
- **Compiler and kernel authoring stacks**
  CUTLASS, CuTe DSL, Triton, and adjacent compiler tooling are increasingly the real productivity layer for performance work, not raw CUDA alone.
- **Low-precision numerics**
  FP8 and other low-precision paths matter when they survive scale, preserve useful optimization dynamics, and remain compatible with fused-kernel design.
- **AI-assisted kernel generation**
  A new frontier is whether models can meaningfully search, synthesize, or refine high-performance kernels instead of only writing toy code snippets.

## Research Questions Right Now

- Which kernel design ideas survive the transition from Hopper-era assumptions to Blackwell-era hardware behavior?
- How much of serving cold-start and deployment friction is now a graph-materialization problem?
- When should a team invest in CUTLASS/CuTe/Triton-based specialization instead of relying on vendor or framework defaults?
- Which low-precision kernel paths are genuinely production-stable rather than benchmark-specific?
- Can AI-generated kernels become trustworthy components of the optimization workflow, or are they still mostly search-time assistants for humans?

## Research Radar

Updated April 24, 2026.

This radar prefers 2025-2026 work. Older CUDA papers stay only when they still teach the core engineering pattern better than newer papers do.

### Active Directions

- Attention kernels are now explicitly hardware-generation-aware: Hopper lessons are no longer enough for Blackwell.
- CUDA graph capture is becoming a deployment bottleneck in its own right, especially for autoscaling and dynamic reconfiguration.
- CUTLASS, CuTe DSL, and Triton are becoming the main productivity-performance interface for serious kernel work.
- FP8 and low-precision engineering is increasingly about numerics-aware architecture design plus kernel/runtime integration.
- Kernel generation by LLMs is becoming a real research direction rather than a novelty demo.
- Memory movement, not raw FLOPs, remains the governing constraint for many production kernels.

### Keywords To Track

`FlashAttention`, `Blackwell`, `WGMMA`, `TMA`, `CUTLASS`, `CuTe DSL`, `Triton`, `FP8 GEMM`, `CUDA graphs`, `kernel autotuning`

### Recent Papers And Research Signals By Direction

#### Attention And Fused Kernel Design

- [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/abs/2603.05451) (2026)
- [The Anatomy of a Triton Attention Kernel](https://arxiv.org/abs/2511.11581) (2025)
- [A Case Study in CUDA Kernel Fusion: Implementing FlashAttention-2 on NVIDIA Hopper Architecture using the CUTLASS Library](https://arxiv.org/abs/2312.11918) (2023, kept as a best-in-class public case study)

#### Graph Capture, Startup, And Runtime Materialization

- [Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start](https://arxiv.org/abs/2604.06664) (2026)

#### Low-Precision And Numerics-Aware CUDA Engineering

- [Towards Fully FP8 GEMM LLM Training at Scale](https://arxiv.org/abs/2505.20524) (2025)

#### AI-Assisted Kernel Generation

- [TritonRL: Training LLMs to Think and Code Triton Without Cheating](https://arxiv.org/abs/2510.17891) (2025)
- [DRTriton: Large-Scale Synthetic Data Reinforcement Learning for Triton Kernel Generation](https://arxiv.org/abs/2603.21465) (2026)

### Related Notes

- [AI Systems](../ai-systems/index.md)
- [Prefill, Decode, and Goodput](../ai-systems/prefill-decode-goodput.md)

## Site Coverage

- [AI Systems](../ai-systems/index.md)
  The parent systems overview for runtime, serving, and deployment questions that sit above kernel-level work.
- [Prefill, Decode, and Goodput](../ai-systems/prefill-decode-goodput.md)
  The best adjacent internal note when kernel choices start affecting latency and serving behavior, not just raw throughput.

## Sources To Follow

- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [CUTLASS Documentation](https://docs.nvidia.com/cutlass/latest/overview.html)
- [Triton Documentation](https://triton-lang.org/main/index)
- [NVIDIA TensorRT-LLM Documentation](https://docs.nvidia.com/tensorrt-llm/index.html)
- [GPU Mode](https://github.com/gpu-mode/resource-stream)

## Open Backlog

- A deeper note on attention-kernel evolution from FlashAttention-2 to FlashAttention-4 and what changed in the hardware assumptions.
- A practical research note on CUDA graphs, runtime materialization, and cold-start behavior in serving stacks.
- A comparison page for CUDA, CUTLASS, CuTe DSL, and Triton as research and engineering interfaces.
- A focused note on FP8 kernel engineering and where numerics, layout, and fusion choices interact.
- A future page on AI-assisted kernel generation and how to evaluate generated kernels honestly.
