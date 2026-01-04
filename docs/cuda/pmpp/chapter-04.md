# Chapter 4: Compute Architecture and Scheduling

=== "English"

    While Chapter 2 and 3 focused on how to write code, Chapter 4 explains **how the hardware actually executes that code**. It bridges the gap between the software "Grid/Block" model and the physical GPU.

    ## 4.1 Architecture of a Modern GPU {#en-architecture}

    **Streaming Multiprocessors (SM):** The GPU is organized into an array of SMs. This is the heart of the GPU.
    
    **Cores:** Each SM contains many processing units, often called "CUDA cores."
    
    **Example (Ampere A100):** This architecture features 108 SMs, each with 64 cores, totaling 6,912 cores.
    
    **Resource Sharing:** All cores within a single SM share control logic and instruction caches.

    ## 4.2 Block Scheduling {#en-scheduling}

    **Distribution:** When a kernel is launched, the CUDA runtime assigns thread blocks to available SMs.
    
    **Block Integrity:** A thread block is assigned to exactly **one** SM and cannot be split across multiple SMs.
    
    **Capacity:** An SM can host multiple blocks at the same time, but there is a hardware limit based on available registers and memory.

    ## 4.3 Synchronization and Transparent Scalability {#en-sync}

    **`__syncthreads()`:** A barrier synchronization function. All threads in a block must reach this call before any are allowed to proceed.
    
    **Deadlock Warning:** If `__syncthreads()` is placed inside a conditional (if-else), all threads must either enter the conditional or none at all; otherwise, the block will hang (deadlock).
    
    **Transparent Scalability:** Because blocks are independent and cannot synchronize with other blocks, the same code can run on a cheap GPU (with 2 SMs) or a high-end GPU (with 100 SMs) without any changes. The hardware simply handles more blocks in parallel on the larger chip.

    ## 4.4 Warps and SIMD Hardware {#en-warps}

    **The Warp:** This is the actual unit of thread scheduling. In current NVIDIA hardware, a warp consists of **32 threads**.
    
    **SIMT (Single Instruction, Multiple Threads):** All 32 threads in a warp execute the same instruction at the same time.
    
    **Hardware Efficiency:** This allows the GPU to use a single "Control" unit for many "ALUs" (math units), saving space on the chip for more math power.

    ## 4.5 Control Divergence {#en-divergence}

    **The Problem:** What happens if 16 threads in a warp want to do the `if` path and 16 want to do the `else` path?
    
    **The Penalty:** The hardware must execute both paths sequentially. While the `if` path runs, the `else` threads are disabled, and vice versa. This is called **Control Divergence**.
    
    **Impact:** Performance is best when all threads in a warp follow the same path. Divergence on boundary checks becomes less impactful as data size increases, because fewer warps "straddle" the boundary.

    ## 4.6 Warp Scheduling and Latency Tolerance {#en-latency}

    **Latency Hiding:** Memory accesses are slow (taking hundreds of cycles).
    
    **Context Switching:** While one warp is waiting for data from memory, the SM's scheduler immediately switches to another warp that is ready to perform math.
    
    **Zero-Overhead:** Unlike CPUs, where switching tasks is "expensive" (requires saving and loading state), GPU threads have their own registers already loaded. Switching between warps costs **zero** clock cycles.

    ## 4.7 Resource Partitioning and Occupancy {#en-occupancy}

    **Occupancy:** The ratio of active warps on an SM to the maximum number of warps the SM could potentially support.
    
    **Resource Limits:** SMs have a fixed amount of:
    
    1. **Registers** (per SM).
    2. **Shared Memory** (per SM).
    3. **Thread Block Slots**.
    
    **The Performance Cliff:** If your kernel uses too many registers per thread, the SM will be able to host fewer blocks. This can lead to a sudden drop in performance (a "cliff") because there aren't enough active warps to hide memory latency.

    ## 4.8 Querying Device Properties {#en-query}

    **Portability:** To write code that runs well on different GPUs, programmers can use API functions:
    
    *   `cudaGetDeviceCount()`: Finds how many GPUs are in the system.
    *   `cudaGetDeviceProperties()`: Returns a struct (`cudaDeviceProp`) containing the number of SMs, max threads per block, and total memory.

    ---

    **Key Takeaway:** Chapter 4 explains that the "magic" of GPU speed comes from **latency hiding**. By having thousands of threads "resident" on the chip, the GPU always has math to do while it waits for slow memory transfers to complete. High performance requires maintaining high **occupancy** and avoiding **control divergence**.

=== "Tiếng Việt"

    Trong khi Chương 2 và 3 tập trung vào cách viết code, Chương 4 giải thích **cách phần cứng thực sự thực thi code đó**. Nó kết nối khoảng cách giữa mô hình phần mềm "Grid/Block" và GPU vật lý.

    ## 4.1 Kiến trúc GPU hiện đại {#vi-architecture}

    **Streaming Multiprocessors (SM):** GPU được tổ chức thành mảng các SM. Đây là trái tim của GPU.
    
    **Lõi:** Mỗi SM chứa nhiều đơn vị xử lý, thường được gọi là "CUDA cores".
    
    **Ví dụ (Ampere A100):** Kiến trúc này có 108 SM, mỗi SM có 64 lõi, tổng cộng 6,912 lõi.
    
    **Chia sẻ tài nguyên:** Tất cả các lõi trong một SM chia sẻ logic điều khiển và cache lệnh.

    ## 4.2 Lập lịch Block {#vi-scheduling}

    **Phân phối:** Khi kernel được khởi chạy, CUDA runtime gán các thread block cho các SM có sẵn.
    
    **Tính toàn vẹn Block:** Một thread block được gán cho chính xác **một** SM và không thể chia nhỏ trên nhiều SM.
    
    **Dung lượng:** Một SM có thể chứa nhiều block cùng lúc, nhưng có giới hạn phần cứng dựa trên register và bộ nhớ có sẵn.

    ## 4.3 Đồng bộ hóa và Khả năng mở rộng trong suốt {#vi-sync}

    **`__syncthreads()`:** Hàm đồng bộ hóa rào cản. Tất cả các luồng trong block phải đạt đến lệnh gọi này trước khi bất kỳ luồng nào được phép tiếp tục.
    
    **Cảnh báo Deadlock:** Nếu `__syncthreads()` được đặt bên trong điều kiện (if-else), tất cả các luồng phải hoặc vào điều kiện hoặc không vào; nếu không, block sẽ bị treo (deadlock).
    
    **Khả năng mở rộng trong suốt:** Vì các block độc lập và không thể đồng bộ với các block khác, cùng một code có thể chạy trên GPU rẻ (với 2 SM) hoặc GPU cao cấp (với 100 SM) mà không cần thay đổi. Phần cứng đơn giản xử lý nhiều block song song hơn trên chip lớn hơn.

    ## 4.4 Warp và Phần cứng SIMD {#vi-warps}

    **Warp:** Đây là đơn vị thực tế của lập lịch luồng. Trong phần cứng NVIDIA hiện tại, một warp bao gồm **32 luồng**.
    
    **SIMT (Single Instruction, Multiple Threads):** Tất cả 32 luồng trong warp thực thi cùng một lệnh cùng lúc.
    
    **Hiệu quả phần cứng:** Điều này cho phép GPU sử dụng một đơn vị "Điều khiển" duy nhất cho nhiều "ALU" (đơn vị toán học), tiết kiệm không gian trên chip cho nhiều sức mạnh toán học hơn.

    ## 4.5 Phân kỳ điều khiển {#vi-divergence}

    **Vấn đề:** Điều gì xảy ra nếu 16 luồng trong warp muốn đi đường `if` và 16 muốn đi đường `else`?
    
    **Hình phạt:** Phần cứng phải thực thi cả hai đường tuần tự. Trong khi đường `if` chạy, các luồng `else` bị vô hiệu hóa, và ngược lại. Đây được gọi là **Phân kỳ điều khiển**.
    
    **Tác động:** Hiệu năng tốt nhất khi tất cả các luồng trong warp đi theo cùng một đường. Phân kỳ trên kiểm tra biên trở nên ít tác động hơn khi kích thước dữ liệu tăng, vì ít warp "nằm chồng" biên hơn.

    ## 4.6 Lập lịch Warp và Dung sai độ trễ {#vi-latency}

    **Che giấu độ trễ:** Truy cập bộ nhớ chậm (mất hàng trăm chu kỳ).
    
    **Chuyển ngữ cảnh:** Trong khi một warp đang chờ dữ liệu từ bộ nhớ, bộ lập lịch của SM ngay lập tức chuyển sang warp khác sẵn sàng thực hiện toán học.
    
    **Không có chi phí:** Không giống như CPU, nơi chuyển tác vụ "tốn kém" (yêu cầu lưu và tải trạng thái), các luồng GPU có register riêng đã được tải. Chuyển đổi giữa các warp không tốn **chu kỳ đồng hồ nào**.

    ## 4.7 Phân vùng tài nguyên và Độ lấp đầy {#vi-occupancy}

    **Độ lấp đầy (Occupancy):** Tỷ lệ warp hoạt động trên SM so với số lượng warp tối đa mà SM có thể hỗ trợ.
    
    **Giới hạn tài nguyên:** SM có số lượng cố định:
    
    1. **Register** (mỗi SM).
    2. **Shared Memory** (mỗi SM).
    3. **Thread Block Slots**.
    
    **Vách đá hiệu năng:** Nếu kernel của bạn sử dụng quá nhiều register mỗi luồng, SM sẽ chỉ có thể chứa ít block hơn. Điều này có thể dẫn đến sụt giảm hiệu năng đột ngột (một "vách đá") vì không có đủ warp hoạt động để che giấu độ trễ bộ nhớ.

    ## 4.8 Truy vấn thuộc tính Device {#vi-query}

    **Tính di động:** Để viết code chạy tốt trên các GPU khác nhau, lập trình viên có thể sử dụng các hàm API:
    
    *   `cudaGetDeviceCount()`: Tìm số lượng GPU trong hệ thống.
    *   `cudaGetDeviceProperties()`: Trả về struct (`cudaDeviceProp`) chứa số lượng SM, số luồng tối đa mỗi block và tổng bộ nhớ.

    ---

    **Điểm chính:** Chương 4 giải thích rằng "phép màu" của tốc độ GPU đến từ **che giấu độ trễ**. Bằng cách có hàng nghìn luồng "thường trú" trên chip, GPU luôn có toán học để làm trong khi chờ các chuyển bộ nhớ chậm hoàn thành. Hiệu năng cao yêu cầu duy trì **độ lấp đầy** cao và tránh **phân kỳ điều khiển**.
