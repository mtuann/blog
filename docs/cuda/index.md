# CUDA Engineering

The path to mastering GPU programming, High-Performance Computing (HPC), and securing a role at NVIDIA/Core AI Labs.

## Zero to Hero Roadmap

### 0. The Foundation (Prerequisites)
*   **Modern C++**: Pointers, Memory Layout, RAII, and `std::vector` internals. NVIDIA requires strong C++ skills, not just Python.
*   **Computer Architecture**: Cache hierarchies (L1/L2), SIMD concepts, and Latency vs Throughput.

### 1. Kernel Basics
*   **GPU Architecture**: SMs, Warps, Scheduling, and the execution hierarchy.
*   **Structuring Kernels**: Grids, Blocks, Threads mapping.
*   **Hello World**: Vector Addition, Matrix Multiplication (Naive).

### 2. Tools of the Trade (Crucial)
*   **Profiling**: Using **Nsight Compute (NCU)** and **Nsight Systems (NSYS)** to identify bottlenecks.
*   **Debugging**: Compute Sanitizer and `printf` debugging strategies.

### 3. Memory Mastery
*   **Global Memory**: Coalescing patterns to maximize bandwidth.
*   **Shared Memory**: Using the L1/Shared cache for tiling (Tiled MatMul).
*   **Register File**: Optimization and preventing spills.

### 4. Compute Optimization
*   **Control Flow**: Branch divergence minimization.
*   **Warp Primitives**: Shuffle instructions for fast reductions.
*   **Occupancy**: Calculating optimal thread/block usage.

### 5. Advanced & Modern CUDA
*   **Tensor Cores**: Using `wmma` intrinsics (Volta/Ampere/Hopper).
*   **CUTLASS**: Understanding the template library for high-performance GEMMs.
*   **Triton**: The Pythonic way to write CUDA (OpenAI).

### 6. Capstone Projects (Resume Builders)
*   **Optimized MatMul**: Implementing tiling and analyzing performance vs cuBLAS.
*   **Custom Attention**: Writing FlashAttention from scratch.
*   **Requirement**: Every project must include **Benchmarks** (Op/s, Bandwidth) and Nsight timeline analysis.

## 📖 Deep Dive: PMPP Study Notes
I am currently working through the 4th Edition of **"Programming Massively Parallel Processors"**. 

*   [**PMPP Book Overview**](pmpp/index.md): Syllabus and core concepts.
*   [**Chapter 1: Introduction**](pmpp/chapter-01.md): The shift to throughput-oriented computing.
*   [**Chapter 2: Data Parallel Computing**](pmpp/chapter-02.md): Kernels, Grids, Blocks, and Threads.
*   [**Chapter 3: Multidimensional Grids**](pmpp/chapter-03.md): 2D/3D mapping and matrix operations.
*   [**Chapter 4: Compute Architecture**](pmpp/chapter-04.md): SMs, warps, and occupancy.
*   [**Chapter 5: Memory Architecture**](pmpp/chapter-05.md): Tiling and shared memory optimization.
*   [**Chapter 6: Performance Considerations**](pmpp/chapter-06.md): Coalescing and thread coarsening.
*   [**Chapter 7: Convolution**](pmpp/chapter-07.md): Constant memory and halo cells.
*   [**Chapter 8: Stencil**](pmpp/chapter-08.md): 3D patterns and register tiling.
*   [**Chapter 9: Parallel Histogram**](pmpp/chapter-09.md): Atomic operations and privatization.
*   [**Chapter 10: Reduction**](pmpp/chapter-10.md): Minimizing divergence and hierarchical reduction.

## Key Resources
*   **Book**: [Programming Massively Parallel Processors](https://shop.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) (The "Bible" of GPU programming).
*   **Official Docs**: [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) & [Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/).
*   **Community**: [CUDA Mode](https://github.com/gpu-mode/resource-stream) (Excellent lectures & repo).
*   **Interactive**: [GPU Mode Lectures](https://www.youtube.com/@GPUMODE) (YouTube).
