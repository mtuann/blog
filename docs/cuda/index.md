---
title: GPU Systems & CUDA
summary: GPU architecture, profiling, memory behavior, and CUDA engineering as part of the AI systems stack.
status: evergreen
updated: 2026-04-24
tags:
  - cuda
  - gpu
  - ai systems
---

<div class="hero-shell section-hero cuda-hero">
<p class="hero-eyebrow">Hardware-Software Interface</p>

<h1>GPU Systems &amp; CUDA</h1>

<p class="hero-lead">This section lives under <strong>AI Systems</strong> because GPU programming is part of the execution substrate for training and inference. The goal here is to move from conceptual understanding to performance-aware engineering.</p>

<div class="chip-row">
<span class="chip">GPU architecture</span>
<span class="chip">Profiling</span>
<span class="chip">Memory hierarchy</span>
<span class="chip">CUDA and Triton</span>
</div>

<div class="hero-actions">
<a class="md-button md-button--primary" href="pmpp/">Read the PMPP Overview</a>
<a class="md-button" href="../ai-systems/">Back to AI Systems</a>
</div>
</div>

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

### Recent Papers By Direction

#### Attention And Fused Kernel Design

- [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/abs/2603.05451) (2026)
- [The Anatomy of a Triton Attention Kernel](https://arxiv.org/abs/2511.11581) (2025)
- [A Case Study in CUDA Kernel Fusion: Implementing FlashAttention-2 on NVIDIA Hopper Architecture using the CUTLASS Library](https://arxiv.org/abs/2312.11918) (2023, kept because it is still one of the best public "how a real fused kernel is built" references)

#### Graph Capture, Startup, And Runtime Materialization

- [Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start](https://arxiv.org/abs/2604.06664) (2026)

#### Low-Precision And Numerics-Aware CUDA Engineering

- [Towards Fully FP8 GEMM LLM Training at Scale](https://arxiv.org/abs/2505.20524) (2025)

#### AI-Assisted Kernel Generation

- [TritonRL: Training LLMs to Think and Code Triton Without Cheating](https://arxiv.org/abs/2510.17891) (2025)
- [DRTriton: Large-Scale Synthetic Data Reinforcement Learning for Triton Kernel Generation](https://arxiv.org/abs/2603.21465) (2026)

### Sources To Follow

- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [CUTLASS Documentation](https://docs.nvidia.com/cutlass/latest/overview.html)
- [Triton Documentation](https://triton-lang.org/main/index)
- [NVIDIA TensorRT-LLM Documentation](https://docs.nvidia.com/tensorrt-llm/index.html)
- [GPU Mode](https://github.com/gpu-mode/resource-stream)
- [NVIDIA Developer Blog](https://developer.nvidia.com/blog/)

### Canonical References Worth Keeping

- [FlashAttention-2](https://arxiv.org/abs/2307.08691)

## Zero To Hero Roadmap

### 1. Foundations

- Modern C++ memory semantics and layout intuition.
- Throughput-oriented architecture: SMs, warps, occupancy, and memory hierarchy.
- The difference between writing a correct kernel and writing a fast kernel.

### 2. Tooling

- Profiling with **Nsight Compute** and **Nsight Systems**.
- Debugging with Compute Sanitizer and careful instrumentation.
- Building the habit of measuring before optimizing.

### 3. Memory And Compute Optimization

- Global-memory coalescing and shared-memory tiling.
- Register pressure, divergence, occupancy, and warp-level primitives.
- How to reason about bandwidth ceilings and arithmetic intensity.

### 4. Modern GPU Software Stacks

- CUDA as the core execution model.
- CUTLASS for high-performance GEMM design patterns.
- Triton for custom kernels in an AI workflow.

### 5. Capstone Work

- Optimized matrix multiplication with benchmarks against vendor libraries.
- Custom attention kernels with careful memory analysis.
- Every serious project should include benchmark tables and profiler screenshots.

## PMPP Study Notes

I am using the 4th edition of **Programming Massively Parallel Processors** as a structured study track.

### Foundations

- [PMPP Overview](pmpp/index.md)
- [Chapter 1: Introduction](pmpp/chapter-01.md)
- [Chapter 2: Data Parallel Computing](pmpp/chapter-02.md)
- [Chapter 3: Multidimensional Grids](pmpp/chapter-03.md)
- [Chapter 4: Compute Architecture](pmpp/chapter-04.md)
- [Chapter 5: Memory Architecture](pmpp/chapter-05.md)
- [Chapter 6: Performance Considerations](pmpp/chapter-06.md)

### Parallel Patterns

- [Chapter 7: Convolution](pmpp/chapter-07.md)
- [Chapter 8: Stencil](pmpp/chapter-08.md)
- [Chapter 9: Parallel Histogram](pmpp/chapter-09.md)
- [Chapter 10: Reduction](pmpp/chapter-10.md)
- [Chapter 11: Prefix Sum (Scan)](pmpp/chapter-11.md)
- [Chapter 12: Parallel Merge](pmpp/chapter-12.md)
- [Chapter 13: Parallel Sorting](pmpp/chapter-13.md)
- [Chapter 14: Sparse Matrix Computation](pmpp/chapter-14.md)
- [Chapter 15: Parallel Graph Algorithms](pmpp/chapter-15.md)

### AI And Advanced Systems

- [Chapter 16: Deep Learning](pmpp/chapter-16.md)
- [Chapter 17: MRI Reconstruction](pmpp/chapter-17.md)
- [Chapter 18: Molecular Dynamics](pmpp/chapter-18.md)
- [Chapter 19: Programming Strategy](pmpp/chapter-19.md)
- [Chapter 20: Heterogeneous Clusters](pmpp/chapter-20.md)
- [Chapter 21: Dynamic Parallelism](pmpp/chapter-21.md)
- [Chapter 22: Evolution and Trends](pmpp/chapter-22.md)
- [Chapter 23: Conclusion](pmpp/chapter-23.md)
- [Appendix A: Numerical Issues](pmpp/appendix-a.md)
- [GPU Engineer Roadmap](pmpp/engineer.md)

## Key Resources

- **Book**: [Programming Massively Parallel Processors](https://shop.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0).
- **Official Docs**: [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) and [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/).
- **Community**: [GPU Mode](https://github.com/gpu-mode/resource-stream).
