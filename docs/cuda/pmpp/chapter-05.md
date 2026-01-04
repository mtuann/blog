# Chapter 5: Memory Architecture and Data Locality

=== "English"

    This is one of the most important chapters in the book. It explains how to overcome the "Memory Wall"—the fact that moving data is often much slower than doing the actual math.

    ## 5.1 Importance of Memory Access Efficiency {#en-efficiency}

    **The Problem:** Global memory (DRAM) is off-chip and slow. A kernel can be "memory-bound," meaning its execution speed is limited by how fast data can be delivered, not how fast the processors are.
    
    **Arithmetic Intensity:** This is the ratio of floating-point operations (FLOPs) to the number of bytes (B) accessed from global memory.
    
    *   *Example:* Simple matrix multiplication has a ratio of **0.25 OP/B** (2 operations for every 8 bytes loaded).
    *   *The Bottleneck:* On an A100 GPU, this low ratio means you only utilize **2%** of the GPU's potential math power because the threads are constantly waiting for data.

    ## 5.2 CUDA Memory Types {#en-memory-types}

    CUDA provides a hierarchy of memory to help programmers manage data locality:
    
    *   **Registers:** Fastest. Per-thread. Used for automatic variables.
    *   **Shared Memory:** Very fast. Per-block. Accessible by all threads in a block. It is "scratchpad memory" that the programmer controls explicitly.
    *   **Constant Memory:** Read-only, cached, and very fast when all threads in a warp access the same address.
    *   **Local Memory:** Not actually local; it resides in global memory. Used when a thread runs out of registers ("register spilling").
    *   **Global Memory:** High capacity but slow. Accessible by all threads in all grids.

    ## 5.3 Tiling for Reduced Memory Traffic {#en-tiling}

    **The Concept of Tiling:** A strategy to partition data into small subsets (tiles) that fit into the high-speed **Shared Memory**.
    
    **The Goal:** Instead of every thread loading the same data from slow global memory multiple times, the threads in a block collaborate to load a tile into shared memory **once** and then reuse it many times.
    
    **Locality:** By focusing on a small subset of data, we exploit "data reuse," drastically reducing the traffic to the slow DRAM.

    ## 5.4 A Tiled Matrix Multiplication Kernel {#en-tiled-matmul}

    **Phase-Based Execution:** Tiled kernels operate in phases:
    
    1. **Collaborative Load:** Each thread in a block loads one element from the global matrix into a shared memory array.
    2. **Barrier (`__syncthreads()`):** Ensure all threads have finished loading the tile before anyone starts the math.
    3. **Computation:** Threads perform the dot product using the data now in fast shared memory.
    4. **Barrier (`__syncthreads()`):** Ensure all threads are finished with the current tile before loading the next one (prevents overwriting data still in use).
    
    **The Payoff:** Global memory traffic is reduced by a factor equal to the `TILE_WIDTH`. If you use 16x16 tiles, you cut global memory requests by **16 times**.

    ## 5.5 Boundary Checks {#en-boundary}

    **Arbitrary Sizes:** Real-world matrices aren't always perfect multiples of the tile size.
    
    **The "Padding" Strategy:** If a tile goes over the edge of the actual data, the threads must detect this and load a **0.0** into shared memory. This allows the dot product math to continue without crashing or producing wrong results (since adding 0 doesn't change a sum).

    ## 5.6 Impact of Memory Usage on Occupancy {#en-occupancy}

    **Resource Limits:** Every SM has a fixed amount of shared memory (e.g., 64KB or 164KB).
    
    **Occupancy Trade-off:** If your kernel requests too much shared memory per block, the hardware will be able to run fewer blocks simultaneously. This reduces **occupancy**, which may make it harder for the GPU to hide latency (as explained in Chapter 4).
    
    **Dynamic Allocation:** Explains how to use the `extern __shared__` keyword to allow the host code to decide the amount of shared memory at runtime.

    ---

    **Key Takeaway:** Chapter 5 introduces **Tiling**, the single most important optimization technique for GPU programming. It teaches you to stop treating the GPU as a "black box" and start manually managing data movement between slow global memory and fast on-chip shared memory.

=== "Tiếng Việt"

    Đây là một trong những chương quan trọng nhất trong cuốn sách. Nó giải thích cách vượt qua "Bức tường bộ nhớ"—thực tế là di chuyển dữ liệu thường chậm hơn nhiều so với thực hiện phép toán.

    ## 5.1 Tầm quan trọng của hiệu quả truy cập bộ nhớ {#vi-efficiency}

    **Vấn đề:** Bộ nhớ global (DRAM) nằm ngoài chip và chậm. Một kernel có thể bị "giới hạn bộ nhớ", nghĩa là tốc độ thực thi của nó bị giới hạn bởi tốc độ cung cấp dữ liệu, không phải tốc độ của bộ xử lý.
    
    **Cường độ số học:** Đây là tỷ lệ các phép toán dấu phẩy động (FLOPs) so với số byte (B) được truy cập từ bộ nhớ global.
    
    *   *Ví dụ:* Nhân ma trận đơn giản có tỷ lệ **0.25 OP/B** (2 phép toán cho mỗi 8 byte được tải).
    *   *Nút thắt cổ chai:* Trên GPU A100, tỷ lệ thấp này có nghĩa là bạn chỉ sử dụng **2%** sức mạnh toán học tiềm năng của GPU vì các luồng liên tục chờ dữ liệu.

    ## 5.2 Các loại bộ nhớ CUDA {#vi-memory-types}

    CUDA cung cấp phân cấp bộ nhớ để giúp lập trình viên quản lý tính địa phương của dữ liệu:
    
    *   **Register:** Nhanh nhất. Mỗi luồng. Được sử dụng cho các biến tự động.
    *   **Shared Memory:** Rất nhanh. Mỗi block. Có thể truy cập bởi tất cả các luồng trong block. Đây là "bộ nhớ tạm" mà lập trình viên kiểm soát rõ ràng.
    *   **Constant Memory:** Chỉ đọc, được cache và rất nhanh khi tất cả các luồng trong warp truy cập cùng một địa chỉ.
    *   **Local Memory:** Không thực sự local; nó nằm trong bộ nhớ global. Được sử dụng khi luồng hết register ("register spilling").
    *   **Global Memory:** Dung lượng cao nhưng chậm. Có thể truy cập bởi tất cả các luồng trong tất cả các grid.

    ## 5.3 Tiling để giảm lưu lượng bộ nhớ {#vi-tiling}

    **Khái niệm Tiling:** Chiến lược phân vùng dữ liệu thành các tập con nhỏ (tile) phù hợp với **Shared Memory** tốc độ cao.
    
    **Mục tiêu:** Thay vì mỗi luồng tải cùng một dữ liệu từ bộ nhớ global chậm nhiều lần, các luồng trong block cộng tác để tải tile vào shared memory **một lần** và sau đó tái sử dụng nhiều lần.
    
    **Tính địa phương:** Bằng cách tập trung vào tập con dữ liệu nhỏ, chúng ta khai thác "tái sử dụng dữ liệu", giảm đáng kể lưu lượng đến DRAM chậm.

    ## 5.4 Kernel nhân ma trận Tiled {#vi-tiled-matmul}

    **Thực thi theo giai đoạn:** Kernel tiled hoạt động theo các giai đoạn:
    
    1. **Tải cộng tác:** Mỗi luồng trong block tải một phần tử từ ma trận global vào mảng shared memory.
    2. **Rào cản (`__syncthreads()`):** Đảm bảo tất cả các luồng đã hoàn thành việc tải tile trước khi bất kỳ ai bắt đầu tính toán.
    3. **Tính toán:** Các luồng thực hiện tích vô hướng sử dụng dữ liệu hiện có trong shared memory nhanh.
    4. **Rào cản (`__syncthreads()`):** Đảm bảo tất cả các luồng đã hoàn thành với tile hiện tại trước khi tải tile tiếp theo (ngăn ghi đè dữ liệu vẫn đang sử dụng).
    
    **Lợi ích:** Lưu lượng bộ nhớ global được giảm theo hệ số bằng `TILE_WIDTH`. Nếu bạn sử dụng tile 16x16, bạn cắt giảm yêu cầu bộ nhớ global **16 lần**.

    ## 5.5 Kiểm tra biên {#vi-boundary}

    **Kích thước tùy ý:** Ma trận thực tế không phải lúc nào cũng là bội số hoàn hảo của kích thước tile.
    
    **Chiến lược "Đệm":** Nếu tile vượt ra ngoài cạnh của dữ liệu thực tế, các luồng phải phát hiện điều này và tải **0.0** vào shared memory. Điều này cho phép phép toán tích vô hướng tiếp tục mà không bị lỗi hoặc tạo ra kết quả sai (vì cộng 0 không thay đổi tổng).

    ## 5.6 Tác động của việc sử dụng bộ nhớ đến Occupancy {#vi-occupancy}

    **Giới hạn tài nguyên:** Mỗi SM có số lượng shared memory cố định (ví dụ: 64KB hoặc 164KB).
    
    **Đánh đổi Occupancy:** Nếu kernel của bạn yêu cầu quá nhiều shared memory mỗi block, phần cứng sẽ chỉ có thể chạy ít block đồng thời hơn. Điều này làm giảm **occupancy**, có thể khiến GPU khó che giấu độ trễ hơn (như giải thích trong Chương 4).
    
    **Cấp phát động:** Giải thích cách sử dụng từ khóa `extern __shared__` để cho phép code host quyết định số lượng shared memory tại runtime.

    ---

    **Điểm chính:** Chương 5 giới thiệu **Tiling**, kỹ thuật tối ưu hóa quan trọng nhất cho lập trình GPU. Nó dạy bạn ngừng coi GPU như "hộp đen" và bắt đầu quản lý thủ công di chuyển dữ liệu giữa bộ nhớ global chậm và shared memory nhanh trên chip.
