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

## Key Resources
*   **Book**: [Programming Massively Parallel Processors](https://shop.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) (The "Bible" of GPU programming).
*   **Official Docs**: [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) & [Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/).
*   **Community**: [CUDA Mode](https://github.com/gpu-mode/resource-stream) (Excellent lectures & repo).
*   **Interactive**: [GPU Mode Lectures](https://www.youtube.com/@GPUMODE) (YouTube).
