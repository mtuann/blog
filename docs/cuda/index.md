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
*   [**Chapter 11: Prefix Sum (Scan)**](pmpp/chapter-11.md): Parallelizing sequential recursions.
*   [**Chapter 12: Parallel Merge**](pmpp/chapter-12.md): Data-dependent workload boundaries.
*   [**Chapter 13: Parallel Sorting**](pmpp/chapter-13.md): Efficient data movement for sorting.
*   [**Chapter 14: Sparse Matrix Computation**](pmpp/chapter-14.md): Handling irregular data structures.
*   [**Chapter 15: Parallel Graph Algorithms**](pmpp/chapter-15.md): Vertex and edge centric processing.
*   [**Chapter 16: Deep Learning**](pmpp/chapter-16.md): Modern AI as matrix multiplications.
*   [**Chapter 17: MRI Reconstruction**](pmpp/chapter-17.md): Hardware trigonometry and constant cache.
*   [**Chapter 18: Molecular Dynamics**](pmpp/chapter-18.md): Spatial binning and cutoff summation.
*   [**Chapter 19: Programming Strategy**](pmpp/chapter-19.md): Computational thinking and algorithm selection.
*   [**Chapter 20: Heterogeneous Clusters**](pmpp/chapter-20.md): Scaling with MPI and CUDA Streams.
*   [**Chapter 21: Dynamic Parallelism**](pmpp/chapter-21.md): Kernels launching other kernels.
*   [**Chapter 22: Evolution and Trends**](pmpp/chapter-22.md): Unified Memory and task-level concurrency.
*   [**Chapter 23: Conclusion**](pmpp/chapter-23.md): The future of throughput-oriented computing.
*   [**Appendix A: Numerical Issues**](pmpp/appendix-a.md): Floating-point precision and stability.
*   [**GPU Engineer Roadmap**](pmpp/engineer.md): Career advice and landing roles at top tech companies.

## Key Resources
*   **Book**: [Programming Massively Parallel Processors](https://shop.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) (The "Bible" of GPU programming).
*   **Official Docs**: [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) & [Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/).
*   **Community**: [CUDA Mode](https://github.com/gpu-mode/resource-stream) (Excellent lectures & repo).
*   **Interactive**: [GPU Mode Lectures](https://www.youtube.com/@GPUMODE) (YouTube).
