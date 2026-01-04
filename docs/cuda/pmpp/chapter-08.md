# Chapter 8: Stencil

=== "English"

    This is a new chapter in the 4th Edition. While stencils resemble convolution, they are primarily used in scientific computing to solve differential equations (e.g., fluid dynamics, heat conductance) and present unique 3D optimization challenges.

    ## 8.1 Background {#en-background}

    **Definition:** A stencil is a geometric pattern of weights applied to each point of a structured grid to approximate derivatives (finite-difference methods).
    
    **Stencil vs. Convolution:**
    
    *   **Similarities:** Both use a neighbor-based weighted sum and must handle halo/ghost cells.
    *   **Differences:** Stencils are typically **iterative** (the output of one step becomes the input of the next) and often use **high-precision data** (double precision), which consumes more on-chip memory.
    
    **Discretization:** Explains how a continuous function (like a sine wave) is represented as discrete points on a grid with a specific spacing ($h$).

    ## 8.2 Parallel Stencil: A Basic Algorithm {#en-basic}

    **3D Stencil:** Most real-world stencils are 3D. A common example is the **7-point stencil**, where each point is calculated using itself plus 6 neighbors (North, South, East, West, Up, and Down).
    
    **The Bottleneck:** The basic parallel version has extremely low arithmetic intensity (**~0.46 OP/B**). Memory access is the primary limiting factor, as each data point is loaded multiple times from global memory.

    ## 8.3 Shared Memory Tiling for Stencil Sweep {#en-tiling}

    **The 3D Challenge:** In 3D, thread blocks are limited by the 1024-thread maximum. An $8 \times 8 \times 8$ cube uses 512 threads, but the "Halo" elements (border cells) account for a massive **58%** of the data loaded.
    
    **Inefficiency:** This high halo-to-internal-data ratio means shared memory tiling is much less effective in 3D than in 2D unless further optimized.
    
    **Coalescing:** Small 3D tiles often lead to poor memory coalescing because threads in a warp end up accessing distant memory locations.

    ## 8.4 Thread Coarsening (Coarsening in Z) {#en-coarsening}

    **The Strategy:** To overcome the 1024-thread limit and the high cost of halos, the authors introduce **thread coarsening in the Z-direction**.
    
    **The Approach:** Instead of one thread calculating one point, each thread calculates a **vertical column** of points.
    
    **Benefit:** In a 3D sweep, you only need to load one "new" plane into shared memory at each step. You reuse the "current" and "previous" planes already on the chip. This significantly reduces global memory traffic and increases the compute-to-memory ratio.

    ## 8.5 Register Tiling {#en-register}

    **The Insight:** In a 7-point stencil, the "Up" and "Down" neighbors (along the Z-axis) are only used by the specific thread assigned to that $(x, y)$ coordinate.
    
    **The Optimization:**
    
    *   The "North, South, East, West" neighbors must stay in **Shared Memory** because they are shared across multiple threads.
    *   The "Up" and "Down" values can be stored in **Registers**, which are even faster and don't take up shared memory capacity.
    
    **Result:** This reduces shared memory usage to **1/3** of the original tiled version, allowing for larger tiles and higher occupancy.

    ## 8.6 Summary of Stencil Optimizations {#en-summary}

    *   **Tiling:** Increases data reuse.
    *   **Coarsening:** Handles the dimensionality of 3D data efficiently.
    *   **Register Tiling:** Further reduces pressure on shared memory by utilizing the register file.

    ---

    **Key Takeaway:** Chapter 8 demonstrates that for 3D patterns, standard tiling isn't enough. High performance requires **"thinking in planes"**—using thread coarsening to sweep through the volume while combining shared memory and registers to minimize the "halo" overhead.

=== "Tiếng Việt"

    Đây là chương mới trong Ấn bản thứ 4. Trong khi stencil giống tích chập, chúng chủ yếu được sử dụng trong tính toán khoa học để giải phương trình vi phân (ví dụ: động lực học chất lỏng, dẫn nhiệt) và đưa ra các thách thức tối ưu hóa 3D độc đáo.

    ## 8.1 Bối cảnh {#vi-background}

    **Định nghĩa:** Stencil là mẫu hình học của các trọng số được áp dụng cho mỗi điểm của lưới có cấu trúc để xấp xỉ đạo hàm (phương pháp sai phân hữu hạn).
    
    **Stencil vs. Tích chập:**
    
    *   **Giống nhau:** Cả hai đều sử dụng tổng có trọng số dựa trên lân cận và phải xử lý halo/ghost cell.
    *   **Khác nhau:** Stencil thường **lặp** (đầu ra của một bước trở thành đầu vào của bước tiếp theo) và thường sử dụng **dữ liệu độ chính xác cao** (double precision), tiêu thụ nhiều bộ nhớ trên chip hơn.
    
    **Rời rạc hóa:** Giải thích cách một hàm liên tục (như sóng sin) được biểu diễn dưới dạng các điểm rời rạc trên lưới với khoảng cách cụ thể ($h$).

    ## 8.2 Stencil song song: Thuật toán cơ bản {#vi-basic}

    **Stencil 3D:** Hầu hết các stencil thực tế là 3D. Một ví dụ phổ biến là **stencil 7 điểm**, trong đó mỗi điểm được tính bằng chính nó cộng với 6 lân cận (Bắc, Nam, Đông, Tây, Trên và Dưới).
    
    **Nút thắt cổ chai:** Phiên bản song song cơ bản có cường độ số học cực thấp (**~0.46 OP/B**). Truy cập bộ nhớ là yếu tố giới hạn chính, vì mỗi điểm dữ liệu được tải nhiều lần từ bộ nhớ global.

    ## 8.3 Tiling Shared Memory cho Stencil Sweep {#vi-tiling}

    **Thách thức 3D:** Trong 3D, thread block bị giới hạn bởi tối đa 1024 luồng. Một khối $8 \times 8 \times 8$ sử dụng 512 luồng, nhưng các phần tử "Halo" (cell biên) chiếm **58%** dữ liệu được tải.
    
    **Không hiệu quả:** Tỷ lệ halo-dữ liệu-bên-trong cao này có nghĩa là tiling shared memory ít hiệu quả hơn nhiều trong 3D so với 2D trừ khi được tối ưu hóa thêm.
    
    **Coalescing:** Tile 3D nhỏ thường dẫn đến coalescing bộ nhớ kém vì các luồng trong warp truy cập các vị trí bộ nhớ xa nhau.

    ## 8.4 Thread Coarsening (Làm thô theo Z) {#vi-coarsening}

    **Chiến lược:** Để vượt qua giới hạn 1024 luồng và chi phí cao của halo, các tác giả giới thiệu **thread coarsening theo hướng Z**.
    
    **Cách tiếp cận:** Thay vì một luồng tính một điểm, mỗi luồng tính một **cột dọc** các điểm.
    
    **Lợi ích:** Trong sweep 3D, bạn chỉ cần tải một mặt phẳng "mới" vào shared memory ở mỗi bước. Bạn tái sử dụng các mặt phẳng "hiện tại" và "trước đó" đã có trên chip. Điều này giảm đáng kể lưu lượng bộ nhớ global và tăng tỷ lệ tính toán-bộ nhớ.

    ## 8.5 Register Tiling {#vi-register}

    **Hiểu biết:** Trong stencil 7 điểm, các lân cận "Trên" và "Dưới" (dọc theo trục Z) chỉ được sử dụng bởi luồng cụ thể được gán cho tọa độ $(x, y)$ đó.
    
    **Tối ưu hóa:**
    
    *   Các lân cận "Bắc, Nam, Đông, Tây" phải ở trong **Shared Memory** vì chúng được chia sẻ giữa nhiều luồng.
    *   Các giá trị "Trên" và "Dưới" có thể được lưu trữ trong **Register**, nhanh hơn và không chiếm dung lượng shared memory.
    
    **Kết quả:** Điều này giảm việc sử dụng shared memory xuống **1/3** phiên bản tiled ban đầu, cho phép tile lớn hơn và occupancy cao hơn.

    ## 8.6 Tóm tắt tối ưu hóa Stencil {#vi-summary}

    *   **Tiling:** Tăng tái sử dụng dữ liệu.
    *   **Coarsening:** Xử lý chiều của dữ liệu 3D một cách hiệu quả.
    *   **Register Tiling:** Giảm thêm áp lực lên shared memory bằng cách sử dụng register file.

    ---

    **Điểm chính:** Chương 8 chứng minh rằng đối với các mẫu 3D, tiling tiêu chuẩn là chưa đủ. Hiệu năng cao yêu cầu **"tư duy theo mặt phẳng"**—sử dụng thread coarsening để quét qua khối lượng trong khi kết hợp shared memory và register để giảm thiểu chi phí "halo".
