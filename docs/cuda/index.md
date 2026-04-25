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

<div class="hero-shell section-hero cuda-hero" markdown>
<p class="hero-eyebrow">Hardware-Software Interface</p>

# GPU Systems & CUDA

<p class="hero-lead">This section lives under <strong>AI Systems</strong> because GPU programming is part of the execution substrate for training and inference. The goal here is to move from conceptual understanding to performance-aware engineering.</p>

<div class="chip-row">
<span class="chip">GPU architecture</span>
<span class="chip">Profiling</span>
<span class="chip">Memory hierarchy</span>
<span class="chip">CUDA and Triton</span>
</div>

<div class="hero-actions" markdown>
[Read the PMPP Overview](pmpp/index.md){ .md-button .md-button--primary }
[Back to AI Systems](../ai-systems/index.md){ .md-button }
</div>
</div>

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
