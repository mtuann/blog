# Chapter 21: CUDA Dynamic Parallelism

=== "English"

    This chapter introduces one of the most significant changes to the CUDA programming model since its inception: the ability for a GPU to launch its own kernels.

    ## 21.1 Background {#en-background}

    *   **The Traditional Limit:** In early CUDA versions, only the Host (CPU) could launch kernels. If a kernel discovered it needed more detail, it had to exit, report back to the CPU, and wait for the CPU to launch a new "refining" kernel. This caused high overhead and latency.
    *   **The Solution:** Dynamic Parallelism allows the GPU to discover new work and launch "child" kernels to handle it without ever involving the CPU.

    ## 21.2 Dynamic Parallelism Overview {#en-overview}

    *   **Syntax:** Launching a kernel from inside another kernel uses the same `<<<Dg, Db, Ns, S>>>` syntax as a host launch.
    *   **Hierarchy:**
        *   **Parent Grid:** The grid launched from the host.
        *   **Child Grid:** The grid launched from a thread inside the parent grid.
    *   **Asynchronous Nature:** Child grids are asynchronous. A parent thread continues executing after a launch unless it explicitly calls `cudaDeviceSynchronize()`. However, a parent **block** is not considered finished until all its child grids have completed.

    ## 21.3 Example: Bezier Curves {#en-bezier}

    *   **Context:** Used in computer graphics to draw smooth curves.
    *   **Variable Workload:** The "curvature" of a line determines how many points are needed to make it look smooth.
    *   **The Optimization:**
        *   **Without Dynamic Parallelism:** One thread block handles one curve. If one curve is sharp and another is flat, threads in the same warp have different amounts of work, leading to **Control Divergence**.
        *   **With Dynamic Parallelism:** A "parent" thread analyzes the curve. If it's complex, it launches a "child" grid specifically sized for that curvature. This ensures every thread in the child grid has exactly one unit of work, eliminating divergence.

    ## 21.4 A Recursive Example: Quadtrees {#en-quadtree}

    *   **Context:** Spatial partitioning where a 2D space is subdivided into four quadrants.
    *   **Algorithm:**
    
        1. A block is assigned a quadrant.
        2. It counts how many points are in that quadrant.
        3. If the number exceeds a threshold, the block launches **four child blocks** to subdivide further.
        
    *   **Recursion:** This process repeats until the quadrants are small enough or the maximum depth is reached. This demonstrates the GPU's ability to handle recursive tree structures that were previously very difficult to program.

    ## 21.5 Important Considerations {#en-considerations}

    *   **Memory Visibility:** Parent threads and child grids only share **Global** and **Constant** memory. A parent thread **cannot** pass a pointer to its *Shared* or *Local* memory to a child grid.
    *   **Pending Launch Pool:** There is a hardware limit on how many kernels can be "waiting" to execute (default is 2048). If exceeded, performance drops significantly. This can be increased using `cudaDeviceSetLimit()`.
    *   **Streams:** By default, child grids launched from the same block are serialized. To run child kernels in parallel, the programmer must use **named streams** within the device code.
    *   **Nesting Depth:** Current hardware supports a maximum of **24 levels** of nested kernel launches.

    ## 21.6 Summary {#en-summary}

    *   Dynamic parallelism removes the CPU-GPU communication bottleneck for irregular data.
    *   It supports **Device-side `cudaMalloc`**, allowing threads to allocate memory for their children.
    *   It simplifies the implementation of complex algorithms like adaptive mesh refinement, graph search, and recursive trees.

    ---

    **Key Takeaway:** Chapter 21 teaches you how to make the GPU **self-scheduling**. By allowing threads to launch kernels, you move from "static" parallelism (fixed data sizes) to "dynamic" parallelism, which is necessary for complex, real-world simulations where work is discovered on the fly.

=== "Tiếng Việt"

    Chương này giới thiệu một trong những thay đổi quan trọng nhất đối với mô hình lập trình CUDA kể từ khi ra đời: khả năng GPU tự khởi chạy các kernel của chính nó.

    ## 21.1 Bối cảnh {#vi-background}

    *   **Giới hạn truyền thống:** Trong các phiên bản CUDA đầu tiên, chỉ có Host (CPU) mới có thể khởi chạy kernel. Nếu một kernel phát hiện ra nó cần xử lý chi tiết hơn, nó phải thoát ra, báo cáo lại cho CPU và chờ CPU khởi chạy một kernel "tinh chỉnh" mới. Điều này gây ra chi phí quản lý (overhead) và độ trễ cao.
    *   **Giải pháp:** Dynamic Parallelism cho phép GPU tự khám phá khối lượng công việc mới và khởi chạy các kernel "con (child)" để xử lý công việc đó mà không cần sự tham gia của CPU.

    ## 21.2 Tổng quan về Dynamic Parallelism {#vi-overview}

    *   **Cú pháp:** Khởi chạy một kernel từ bên trong một kernel khác sử dụng cùng cú pháp `<<<Dg, Db, Ns, S>>>` như khi khởi chạy từ host.
    *   **Phân cấp:**
        *   **Parent Grid:** Lưới được khởi chạy từ host.
        *   **Child Grid:** Lưới được khởi chạy từ một luồng bên trong parent grid.
    *   **Bản chất bất đồng bộ:** Các lưới con (child grids) là bất đồng bộ. Một luồng cha tiếp tục thực thi sau khi khởi chạy trừ khi nó gọi `cudaDeviceSynchronize()` một cách rõ ràng. Tuy nhiên, một **block** cha không được coi là kết thúc cho đến khi tất cả các lưới con của nó hoàn thành.

    ## 21.3 Ví dụ: Đường cong Bezier {#vi-bezier}

    *   **Ngữ cảnh:** Được sử dụng trong đồ họa máy tính để vẽ các đường cong mượt mà.
    *   **Khối lượng công việc thay đổi:** "Độ cong" của một đường xác định cần bao nhiêu điểm để làm cho nó trông mượt mà.
    *   **Tối ưu hóa:**
        *   **Không có Dynamic Parallelism:** Một khối luồng xử lý một đường cong. Nếu một đường cong sắc nét và một đường khác phẳng, các luồng trong cùng một warp có khối lượng công việc khác nhau, dẫn đến **Phân kỳ điều khiển (Control Divergence)**.
        *   **Có Dynamic Parallelism:** Một luồng "cha" phân tích đường cong. Nếu nó phức tạp, nó sẽ khởi chạy một lưới "con" có kích thước cụ thể cho độ cong đó. Điều này đảm bảo mọi luồng trong lưới con đều có đúng một đơn vị công việc, loại bỏ phân kỳ.

    ## 21.4 Ví dụ đệ quy: Quadtrees {#vi-quadtree}

    *   **Ngữ cảnh:** Phân vùng không gian nơi một không gian 2D được chia nhỏ thành bốn góc phần tư.
    *   **Thuật toán:**
    
        1. Một block được gán cho một góc phần tư.
        2. Nó đếm xem có bao nhiêu điểm trong góc phần tư đó.
        3. Nếu số lượng vượt quá một ngưỡng, block sẽ khởi chạy **bốn block con** để phân chia thêm.
        
    *   **Đệ quy:** Quá trình này lặp lại cho đến khi các góc phần tư đủ nhỏ hoặc đạt đến độ sâu tối đa. Điều này minh chứng cho khả năng của GPU trong việc xử lý các cấu trúc cây đệ quy mà trước đây rất khó lập trình.

    ## 21.5 Các lưu ý quan trọng {#vi-considerations}

    *   **Khả năng hiển thị bộ nhớ:** Các luồng cha và lưới con chỉ chia sẻ bộ nhớ **Global** và **Constant**. Một luồng cha **không thể** truyền một con trỏ tới bộ nhớ *Shared* hoặc *Local* của nó cho một lưới con.
    *   **Bể chứa lệnh khởi chạy đang chờ (Pending Launch Pool):** Có một giới hạn phần cứng về số lượng kernel có thể "đang chờ" thực thi (mặc định là 2048). Nếu vượt quá, hiệu suất sẽ giảm đáng kể. Điều này có thể được tăng lên bằng cách sử dụng `cudaDeviceSetLimit()`.
    *   **Streams:** Theo mặc định, các lưới con được khởi chạy từ cùng một block sẽ được tuần tự hóa. Để chạy các kernel con song song, lập trình viên phải sử dụng **named streams** bên trong mã thiết bị.
    *   **Độ sâu lồng nhau:** Phần cứng hiện tại hỗ trợ tối đa **24 cấp độ** khởi chạy kernel lồng nhau.

    ## 21.6 Tóm tắt {#vi-summary}

    *   Dynamic parallelism loại bỏ nút thắt cổ chai truyền thông CPU-GPU đối với dữ liệu không đều.
    *   Nó hỗ trợ **`cudaMalloc` phía thiết bị**, cho phép các luồng cấp phát bộ nhớ cho các luồng con của chúng.
    *   Nó đơn giản hóa việc triển khai các thuật toán phức tạp như làm mịn lưới thích ứng, tìm kiếm đồ thị và cây đệ quy.

    ---

    **Điểm chính:** Chương 21 dạy bạn cách làm cho GPU **tự lập lịch**. Bằng cách cho phép các luồng khởi chạy kernel, bạn chuyển từ tính song song "tĩnh" (kích thước dữ liệu cố định) sang tính song song "động", điều cần thiết cho các mô phỏng thực tế phức tạp nơi khối lượng công việc được phát hiện ngay lập tức.
