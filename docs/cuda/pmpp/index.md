# Programming Massively Parallel Processors (PMPP) - Overview

=== "English"

    ## Syllabus: PMPP (4th Edition) {#en-syllabus}

    This syllabus is organized into four major phases: Foundations, Performance Optimization, Parallel Patterns, and Advanced Applications (AI/ML).

    ### Phase 1: Foundations of GPU Computing {#en-phase1}
    1. **Introduction to Heterogeneous Computing**: Why parallel computing? The shift from "faster clocks" to "more cores."
    2. **The CUDA Programming Model**: Kernels, grids, blocks, and threads. Your first "Vector Addition" program.
    3. **Data-Parallel Execution Model**: Understanding the SIMT (Single Instruction, Multiple Threads) architecture and hardware multithreading.
    4. **GPU Memory Hierarchy**: Global, constant, and shared memory; registers and caches.

    ### Phase 2: Performance and Hardware Architecture {#en-phase2}
    1. **Performance Considerations**: Thread divergence, memory coalescing, and latency hiding.
    2. **Compute Capability and Occupancy**: How to balance resources (registers/shared memory) to keep the GPU fully utilized.
    3. **Floating Point Excellence**: Understanding precision (FP32, FP16, BF16) and numerical stability.

    ### Phase 3: Fundamental Parallel Patterns {#en-phase3}
    1. **Convolution**: Implementation of 1D and 2D filters.
    2. **Prefix Sum (Scan)**: Solving problems that seem inherently sequential.
    3. **Reduction**: Efficiently summing or finding the max/min of billions of elements.
    4. **Stencil Computation**: Grid-based updates (used in weather simulations).
    5. **Histogramming**: Dealing with "atomic" operations and memory contention.
    6. **Sparse Matrix-Vector Multiplication (SpMV)**: Handling data where most values are zero.
    7. **Merge Sort**: Implementing high-performance sorting on the GPU.

    ### Phase 4: Advanced Topics and Modern AI {#en-phase4}
    1. **Deep Learning and Tensor Cores**: (New in 4th Ed) How GPUs accelerate Transformers and CNNs.
    2. **Graph Processing**: Navigating irregular data structures.
    3. **Dynamic Parallelism**: Kernels launching other kernels.
    4. **Multi-GPU Programming**: Using NVLink and MPI.

    ## What makes this book unique? {#en-unique}

    The 4th Edition is a masterclass in **"Thinking in Parallel."**

    1. **Pattern-Based Teaching**: Focuses on "Algorithmic Patterns" like Reduction, Scan, and Convolution rather than just syntax.
    2. **Bridging Software and Hardware**: Explains *why* code is slow by looking at hardware limitations (bandwidth, warp scheduling).
    3. **Focus on Modern AI**: Significant new content on **Tensor Cores** and **Mixed Precision** (FP16/INT8).

=== "Tiếng Việt"

    ## Lộ trình học: PMPP (Ấn bản thứ 4) {#vi-syllabus}

    Lộ trình này được chia thành bốn giai đoạn chính: Nền tảng, Tối ưu hóa hiệu năng, Các mẫu song song (Parallel Patterns), và Ứng dụng nâng cao (AI/ML).

    ### Giai đoạn 1: Nền tảng của Tính toán GPU {#vi-phase1}
    1. **Giới thiệu về Tính toán không đồng nhất**: Tại sao cần tính toán song song? Sự chuyển dịch từ "tăng xung nhịp" sang "tăng số lõi".
    2. **Mô hình lập trình CUDA**: Kernel, grid, block, và thread. Chương trình "Cộng vector" đầu tiên.
    3. **Mô hình thực thi song song dữ liệu**: Hiểu về kiến trúc SIMT (Single Instruction, Multiple Threads) và đa luồng phần cứng.
    4. **Hệ thống phân cấp bộ nhớ GPU**: Bộ nhớ global, constant, và shared; register và cache.

    ### Giai đoạn 2: Hiệu năng và Kiến trúc phần cứng {#vi-phase2}
    1. **Các cân nhắc về hiệu năng**: Phân kỳ luồng (thread divergence), gộp bộ nhớ (memory coalescing), và che giấu độ trễ.
    2. **Khả năng tính toán và Độ lấp đầy (Occupancy)**: Cách cân bằng tài nguyên để GPU luôn hoạt động hết công suất.
    3. **Độ chính xác số thực**: Hiểu về FP32, FP16, BF16 và tính ổn định số học.

    ### Giai đoạn 3: Các mẫu song song cơ bản {#vi-phase3}
    1. **Tích chập (Convolution)**: Triển khai các bộ lọc 1D và 2D.
    2. **Prefix Sum (Scan)**: Giải quyết các bài toán có vẻ tuần tự.
    3. **Reduction (Gom nhóm)**: Tính tổng hoặc tìm max/min một cách hiệu quả.
    4. **Stencil Computation**: Cập nhật dựa trên lưới (dùng trong mô phỏng thời tiết).
    5. **Histogramming (Biểu đồ tần suất)**: Xử lý các thao tác "atomic" và tranh chấp bộ nhớ.
    6. **Nhân ma trận thưa (SpMV)**: Xử lý dữ liệu có nhiều giá trị bằng không.
    7. **Merge Sort**: Triển khai sắp xếp hiệu năng cao trên GPU.

    ### Giai đoạn 4: Chủ đề nâng cao và AI hiện đại {#vi-phase4}
    1. **Deep Learning và Tensor Cores**: (Mới ở bản 4) Cách GPU tăng tốc Transformer và CNN.
    2. **Xử lý đồ thị**: Điều hướng các cấu trúc dữ liệu không đều.
    3. **Dynamic Parallelism**: Kernel khởi tạo kernel khác.
    4. **Lập trình Multi-GPU**: Sử dụng NVLink và MPI.

    ## Tại sao cuốn sách này đặc biệt? {#vi-unique}

    Ấn bản thứ 4 là một khóa học chuyên sâu về **"Tư duy song song".**

    1. **Phương pháp dạy dựa trên mẫu (Pattern-Based)**: Tập trung vào "Các mẫu thuật toán" như Reduction, Scan, Tích chập thay vì chỉ dạy cú pháp.
    2. **Kết nối Phần mềm và Phần cứng**: Giải thích *tại sao* code chạy chậm thông qua các giới hạn phần cứng (băng thông, warp scheduling).
    3. **Tập trung vào AI hiện đại**: Nội dung mới về **Tensor Cores** và **Độ chính xác hỗn hợp** (FP16/INT8).
