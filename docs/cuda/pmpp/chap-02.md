# Chapter 2: Heterogeneous Data Parallel Computing

=== "English"

    ## 2.1 Data Parallelism {#en-data-parallelism}
    The core of CUDA is applying the same operation independently to many data elements. This provides **scalability**: as data grows, we increase threads to maintain performance.

    ## 2.2 CUDA C Program Structure {#en-structure}
    *   **Host (CPU)**: Controls execution, manages memory, and launches kernels.
    *   **Device (GPU)**: Executes the parallel kernel functions.
    *   **Kernel**: A function executed $N$ times in parallel by $N$ different CUDA threads.

    ## 2.3 Memory Management {#en-memory}
    *   **Global Memory**: The DRAM on the GPU.
    *   `cudaMalloc`: Allocate memory on the GPU.
    *   `cudaFree`: Release GPU memory.
    *   `cudaMemcpy`: Transfer data between Host and Device (must specify direction).

    ## 2.4 The Thread Hierarchy {#en-hierarchy}
    CUDA organizes threads into a hierarchy: **Grid $\rightarrow$ Block $\rightarrow$ Thread**.
    *   **Built-in Variables**: `threadIdx`, `blockIdx`, `blockDim`.
    *   **Global Index Calculation**: 
        ```c
        int i = blockIdx.x * blockDim.x + threadIdx.x;
        ```

    ## 2.5 Kernel Configuration {#en-configuration}
    Kernels are launched with: `kernel<<<numBlocks, threadsPerBlock>>>(...)`.
    Always include a boundary check: `if (i < n)` to prevent out-of-bounds memory access.

=== "Tiếng Việt"

    ## 2.1 Song song dữ liệu (Data Parallelism) {#vi-data-parallelism}
    Cốt lõi của CUDA là áp dụng cùng một phép toán một cách độc lập lên nhiều phần tử dữ liệu. Điều này mang lại khả năng **mở rộng (scalability)**: khi dữ liệu tăng lên, chúng ta tăng số luồng để duy trì hiệu năng.

    ## 2.2 Cấu trúc chương trình CUDA C {#vi-structure}
    *   **Host (CPU)**: Điều khiển thực thi, quản lý bộ nhớ và gọi kernel.
    *   **Device (GPU)**: Thực thi các hàm kernel song song.
    *   **Kernel**: Một hàm được thực thi $N$ lần song song bởi $N$ luồng CUDA khác nhau.

    ## 2.3 Quản lý bộ nhớ {#vi-memory}
    *   **Bộ nhớ Global**: RAM trên GPU.
    *   `cudaMalloc`: Cấp phát bộ nhớ trên GPU.
    *   `cudaFree`: Giải phóng bộ nhớ GPU.
    *   `cudaMemcpy`: Chuyển dữ liệu giữa Host và Device (phải chỉ rõ hướng).

    ## 2.4 Hệ phân cấp Luồng (Thread Hierarchy) {#vi-hierarchy}
    CUDA tổ chức các luồng theo kiến trúc: **Grid $\rightarrow$ Block $\rightarrow$ Thread**.
    *   **Biến dựng sẵn**: `threadIdx`, `blockIdx`, `blockDim`.
    *   **Tính chỉ số toàn cục (Global Index)**: 
        ```c
        int i = blockIdx.x * blockDim.x + threadIdx.x;
        ```

    ## 2.5 Cấu hình thực thi Kernel {#vi-configuration}
    Kernel được gọi bằng cú pháp: `kernel<<<số_block, số_thread_mỗi_block>>>(...)`.
    Luôn bao gồm kiểm tra biên: `if (i < n)` để ngăn chặn truy cập bộ nhớ ngoài phạm vi.

    ---

    > **Main takeaway**: CUDA doesn't tell the GPU *how many loops* to run, but describes *what one thread does* and clones that behavior thousands of times.
