# Chapter 18: Molecular Dynamics and Spatial Binning

=== "English"

    This chapter provides a case study in molecular dynamics. It demonstrates how to handle algorithms that have massive data sizes and how to transition from an accurate but slow algorithm to a highly scalable one.

    ## 18.1 Background {#en-background}

    *   **Visual Molecular Dynamics (VMD):** A tool used by biologists to visualize biomolecular systems (viruses, proteins).
    *   **The Problem:** Calculating the "Electrostatic Potential Map"—a grid where each point represents the electrical potential energy exerted by all atoms in a system.
    *   **Direct Coulomb Summation (DCS):** The potential at grid point $j$ is the sum of (charge of atom $i$ / distance between $i$ and $j$).
    *   **Computational Challenge:** The complexity is $O(\text{Atoms} \times \text{GridPoints})$. As the volume of a system grows, the number of calculations grows quadratically, making it too slow for large biological systems.

    ## 18.2 Scatter versus Gather in Kernel Design {#en-scatter-gather}

    *   **Scatter Approach:** Assign one thread to each **atom**. Each thread "scatters" its charge contribution to all grid points.
        *   *Problem:* Multiple threads try to update the same grid point at once, requiring **Atomic Operations** which are extremely slow in this context.
    *   **Gather Approach:** Assign one thread to each **grid point**. Each thread "gathers" the contribution from all atoms.
        *   *Benefit:* No atomic operations are needed.
        *   *Optimization:* Since all grid points in a 2D slice share the same $Z$ coordinate, the $Z$-distance of an atom only needs to be calculated once per slice and can be reused.

    ## 18.3 Thread Coarsening {#en-coarsening}

    *   **Observation:** All grid points in a single row share the same $Y$ coordinate.
    *   **The Optimization:** Coarsen the thread so that one thread calculates **four adjacent grid points** in a row.
    *   **Result:** By calculating the $Y$ and $Z$ components of the distance once and reusing them for four points, the kernel drastically reduces the number of constant memory accesses and redundant math operations.

    ## 18.4 Memory Coalescing {#en-coalescing}

    *   **The Problem:** If coarsened threads write to their four points in a simple sequence (Point 0, 1, 2, 3), the writes across the warp will be "strided" and uncoalesced.
    *   **The Fix:** Reorganize the thread mapping so that adjacent threads in a warp write to **adjacent memory locations**.
    *   **Impact:** This ensures the GPU can use a single memory transaction to write the results of 32 threads, maximizing write bandwidth.

    ## 18.5 Cutoff Binning for Data Size Scalability {#en-cutoff}

    *   **The Scaling Wall:** For millions of atoms, even an optimized Gather kernel is too slow because it still checks every atom for every grid point.
    *   **The Insight:** The influence of an atom decreases with distance. Contributions from atoms far away are negligible.
    *   **Cutoff Summation:** Only calculate contributions from atoms within a fixed radius (e.g., 12 Ångströms). This changes the complexity from $O(N^2)$ to $O(N)$.
    *   **Spatial Binning:** To avoid checking every atom to see if it is "close," the system partitions the space into **Bins** (cubical boxes).
    *   **The Parallel Algorithm:**
    
        1. Sort atoms into bins.
        2. For a block of grid points, identify a "neighborhood" of bins.
        3. Threads only iterate through the atoms contained in those specific neighbor bins.
        
    *   **Overflow Handling:** Since some bins might have more atoms than others, the system uses an "overflow list" for dense areas to maintain a regular workload for the GPU.

    ## 18.6 Summary {#en-summary}

    *   **Transformation:** The chapter tracks the journey from a basic "Scatter" kernel to a "Gather" kernel, then adds "Coarsening" and "Coalescing."
    *   **Final Result:** The implementation of **Cutoff Binning** allows the application to handle massive molecular systems that were previously impossible to simulate.
    *   **Lesson:** Higher-level algorithmic changes (like moving to Bins and Cutoffs) often yield much larger speedups than low-level code tuning once the data size reaches a certain threshold.

    ---

    **Key Takeaway:** Chapter 18 teaches you how to manage **Computational Complexity.** It shows that while low-level hardware tuning (coalescing/registers) is important, scaling to "Big Data" requires smart data structures like **Spatial Binning** to avoid doing unnecessary work.

=== "Tiếng Việt"

    Chương này cung cấp một nghiên cứu điển hình trong động học phân tử. Nó minh họa cách xử lý các thuật toán có kích thước dữ liệu khổng lồ và cách chuyển đổi từ một thuật toán chính xác nhưng chậm sang một thuật toán có khả năng mở rộng cao.

    ## 18.1 Bối cảnh {#vi-background}

    *   **Visual Molecular Dynamics (VMD):** Một công cụ được các nhà sinh học sử dụng để hình ảnh hóa các hệ thống phân tử sinh học (virus, protein).
    *   **Vấn đề:** Tính toán "Bản đồ tiềm năng tĩnh điện (Electrostatic Potential Map)"—một lưới nơi mỗi điểm đại diện cho thế năng điện được tạo ra bởi tất cả các nguyên tử trong một hệ thống.
    *   **Direct Coulomb Summation (DCS):** Tiềm năng tại điểm lưới $j$ là tổng của (điện tích của nguyên tử $i$ / khoảng cách giữa $i$ và $j$).
    *   **Thách thức tính toán:** Độ phức tạp là $O(\text{Nguyên tử} \times \text{Điểm lưới})$. Khi thể tích của một hệ thống tăng lên, số lượng phép tính tăng theo cấp số nhân, khiến nó quá chậm đối với các hệ thống sinh học lớn.

    ## 18.2 Scatter vs. Gather trong thiết kế Kernel {#vi-scatter-gather}

    *   **Cách tiếp cận Scatter (Phân tán):** Gán một luồng cho mỗi **nguyên tử**. Mỗi luồng "phân tán" đóng góp điện tích của nó cho tất cả các điểm lưới.
        *   *Vấn đề:* Nhiều luồng cố gắng cập nhật cùng một điểm lưới cùng lúc, yêu cầu các **Atomic Operations** vốn cực kỳ chậm trong bối cảnh này.
    *   **Cách tiếp cận Gather (Tập hợp):** Gán một luồng cho mỗi **điểm lưới**. Mỗi luồng "tập hợp" đóng góp từ tất cả các nguyên tử.
        *   *Lợi ích:* Không cần các thao tác atomic.
        *   *Tối ưu hóa:* Vì tất cả các điểm lưới trong một lát cắt 2D chia sẻ cùng một tọa độ $Z$, khoảng cách $Z$ của một nguyên tử chỉ cần được tính một lần cho mỗi lát cắt và có thể được sử dụng lại.

    ## 18.3 Thread Coarsening (Làm thô luồng) {#vi-coarsening}

    *   **Quan sát:** Tất cả các điểm lưới trong một hàng duy nhất chia sẻ cùng một tọa độ $Y$.
    *   **Tối ưu hóa:** Làm thô luồng để một luồng tính toán **bốn điểm lưới liền kề** trong một hàng.
    *   **Kết quả:** Bằng cách tính toán các thành phần $Y$ và $Z$ của khoảng cách một lần và sử dụng lại chúng cho bốn điểm, kernel giảm đáng kể số lượng truy cập bộ nhớ constant và các phép toán thừa.

    ## 18.4 Memory Coalescing (Gộp bộ nhớ) {#vi-coalescing}

    *   **Vấn đề:** Nếu các luồng đã được làm thô ghi vào bốn điểm của chúng theo một trình tự đơn giản (Điểm 0, 1, 2, 3), các thao tác ghi trên warp sẽ bị "strided" (cách quãng) và không được gộp lại.
    *   **Giải pháp:** Tổ chức lại việc ánh xạ luồng sao cho các luồng liền kề trong một warp ghi vào **các vị trí bộ nhớ liền kề**.
    *   **Tác động:** Điều này đảm bảo GPU có thể sử dụng một giao dịch bộ nhớ duy nhất để ghi kết quả của 32 luồng, tối đa hóa băng thông ghi.

    ## 18.5 Cutoff Binning cho khả năng mở rộng kích thước dữ liệu {#vi-cutoff}

    *   **Bức tường mở rộng:** Đối với hàng triệu nguyên tử, ngay cả một kernel Gather đã được tối ưu hóa cũng quá chậm vì nó vẫn phải kiểm tra mọi nguyên tử cho mọi điểm lưới.
    *   **Cơ sở khoa học:** Ảnh hưởng của một nguyên tử giảm dần theo khoảng cách. Đóng góp từ các nguyên tử ở xa là không đáng kể.
    *   **Cutoff Summation (Tổng có ngưỡng):** Chỉ tính toán đóng góp từ các nguyên tử trong một bán kính cố định (ví dụ: 12 Ångströms). Điều này thay đổi độ phức tạp từ $O(N^2)$ sang $O(N)$.
    *   **Spatial Binning (Phân thùng không gian):** Để tránh việc phải kiểm tra mọi nguyên tử xem nó có "gần" hay không, hệ thống chia không gian thành các **Thùng (Bins)** (các hộp hình lập phương).
    *   **Thuật toán song song:**
    
        1. Sắp xếp các nguyên tử vào các thùng.
        2. Đối với một khối các điểm lưới, xác định một "vùng lân cận" của các thùng.
        3. Các luồng chỉ lặp qua các nguyên tử có trong các thùng lân cận cụ thể đó.
        
    *   **Xử lý tràn:** Vì một số thùng có thể có nhiều nguyên tử hơn những thùng khác, hệ thống sử dụng một "danh sách tràn" cho các khu vực dày đặc để duy trì khối lượng công việc đều đặn cho GPU.

    ## 18.6 Tóm tắt {#vi-summary}

    *   **Sự biến đổi:** Chương theo dõi hành trình từ một kernel "Scatter" cơ bản sang một kernel "Gather", sau đó thêm "Coarsening" và "Coalescing".
    *   **Kết quả cuối cùng:** Việc triển khai **Cutoff Binning** cho phép ứng dụng xử lý các hệ thống phân tử khổng lồ mà trước đây không thể mô phỏng được.
    *   **Bài học:** Thay đổi thuật toán ở cấp độ cao hơn (như chuyển sang Bins và Cutoffs) thường mang lại hiệu quả tăng tốc lớn hơn nhiều so với việc điều chỉnh mã ở cấp độ thấp một khi kích thước dữ liệu đạt đến một ngưỡng nhất định.

    ---

    **Điểm chính:** Chương 18 dạy bạn cách quản lý **Độ phức tạp tính toán.** Nó chỉ ra rằng trong khi điều chỉnh phần cứng cấp thấp (coalescing/registers) là quan trọng, việc mở rộng lên "Dữ liệu lớn" đòi hỏi các cấu trúc dữ liệu thông minh như **Spatial Binning** để tránh làm những công việc không cần thiết.
