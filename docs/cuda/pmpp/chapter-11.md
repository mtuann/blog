# Chapter 11: Prefix Sum (Parallel Scan)

=== "English"

    This chapter explores one of the most powerful parallel primitives. Scan is used to parallelize problems that appear to be purely sequential (recursions), such as resource allocation, polynomial evaluation, and sorting.

    ## 11.1 Background {#en-background}

    **Definition:** Given an input $[x_0, x_1, x_2, ...]$, scan produces an output where each element is the sum of all preceding elements.
    
    **Inclusive Scan:** The $i$-th output includes $x_i$ (e.g., $[x_0, x_0+x_1, x_0+x_1+x_2, ...]$).
    
    **Exclusive Scan:** The $i$-th output excludes $x_i$ and starts with an identity value (0) (e.g., $[0, x_0, x_0+x_1, ...]$).
    
    **Sequential Complexity:** $O(N)$. It is very efficient on a CPU but entirely serial.

    ## 11.2 Parallel Scan: The Kogge-Stone Algorithm {#en-kogge-stone}

    **The Concept:** An in-place algorithm that doubles the range of the sum in each step. After step $k$, each position contains the sum of $2^k$ elements.
    
    **Steps:** Completes in $\log_2 N$ steps.
    
    **The Race Condition (Write-After-Read):** A major hardware hurdle. Because threads read from and write to the same array, a thread might read a value that was already updated by another thread in the current step, leading to wrong results.
    
    **The Fix:**
    
    1. Use a temporary variable (register) and an extra `__syncthreads()`.
    2. Use **Double Buffering**: Alternate between two different shared memory arrays in each iteration.

    ## 11.3 Work Efficiency Consideration {#en-work-efficiency}

    **The Downside of Kogge-Stone:** It performs $O(N \log N)$ operations.
    
    **Comparison:** For 1,024 elements, a CPU does ~1,000 additions. Kogge-Stone does ~10,000.
    
    **Conclusion:** Kogge-Stone is **not work-efficient**. It is fast only if you have a massive surplus of execution units to "waste" on redundant additions.

    ## 11.4 Parallel Scan: The Brent-Kung Algorithm {#en-brent-kung}

    **The Goal:** Achieve $O(N)$ complexity to match the CPU's efficiency.
    
    **The Two-Phase Approach:**
    
    1. **Reduction Phase (Up-sweep):** Builds a reduction tree to calculate the total sum of the block.
    2. **Distribution Phase (Down-sweep):** Uses the partial sums from the tree to fill in the missing prefix sums for all other elements.
    
    **Efficiency:** It performs roughly $2N$ operations. It is **work-efficient** and consumes less energy/bandwidth than Kogge-Stone, though it takes more steps ($2 \log N$).

    ## 11.5 Coarsening for Even More Efficiency {#en-coarsening}

    **The Strategy:** Each thread handles a segment of the data (e.g., 4 or 8 elements) sequentially first.
    
    **Three-Phase Process:**
    
    1. Local sequential scan of the segments.
    2. Parallel scan of the "tails" (last elements) of each segment.
    3. Local update to add the results back to the internal elements.
    
    **Result:** Drastically reduces the number of threads and synchronization points required.

    ## 11.6 Segmented Scan for Arbitrary Length {#en-segmented}

    **The Problem:** Hardware limits block sizes to 1,024 threads.
    
    **The Hierarchical Solution:**
    
    1. Scan sections of the data independently.
    2. Write the "last" element of each section to an auxiliary array.
    3. Scan the auxiliary array.
    4. Add the scanned values back to the corresponding sections.

    ## 11.7 Single-Pass Scan (Domino Scan) {#en-domino}

    **The Advanced Optimization:** Avoids multiple kernel launches by passing values between blocks while the kernel is still running.
    
    **Adjacent Synchronization:** Blocks use "flags" and atomic operations in global memory to signal to the "next" block that their partial sum is ready.
    
    **Deadlock Prevention:** Uses **Dynamic Block Indexing** to ensure that blocks are processed in the correct order, as the default hardware scheduler does not guarantee linear execution.

    ---

    **Key Takeaway:** Chapter 11 teaches that parallelizing a sequential recursion requires a fundamental change in the algorithm. You must choose between **Kogge-Stone** (fast but wasteful) and **Brent-Kung** (work-efficient) and use **Hierarchical** or **Domino** strategies to scale to real-world data sizes.

=== "Tiếng Việt"

    Chương này khám phá một trong những nguyên thủy song song mạnh mẽ nhất. Scan được sử dụng để song song hóa các bài toán có vẻ hoàn toàn tuần tự (đệ quy), chẳng hạn như phân bổ tài nguyên, đánh giá đa thức và sắp xếp.

    ## 11.1 Bối cảnh {#vi-background}

    **Định nghĩa:** Cho đầu vào $[x_0, x_1, x_2, ...]$, scan tạo ra đầu ra trong đó mỗi phần tử là tổng của tất cả các phần tử trước đó.
    
    **Inclusive Scan:** Đầu ra thứ $i$ bao gồm $x_i$ (ví dụ: $[x_0, x_0+x_1, x_0+x_1+x_2, ...]$).
    
    **Exclusive Scan:** Đầu ra thứ $i$ loại trừ $x_i$ và bắt đầu bằng giá trị đơn vị (0) (ví dụ: $[0, x_0, x_0+x_1, ...]$).
    
    **Độ phức tạp tuần tự:** $O(N)$. Rất hiệu quả trên CPU nhưng hoàn toàn tuần tự.

    ## 11.2 Scan song song: Thuật toán Kogge-Stone {#vi-kogge-stone}

    **Khái niệm:** Thuật toán tại chỗ tăng gấp đôi phạm vi tổng ở mỗi bước. Sau bước $k$, mỗi vị trí chứa tổng của $2^k$ phần tử.
    
    **Các bước:** Hoàn thành trong $\log_2 N$ bước.
    
    **Điều kiện tranh chấp (Write-After-Read):** Rào cản phần cứng lớn. Vì các luồng đọc và ghi vào cùng một mảng, một luồng có thể đọc giá trị đã được cập nhật bởi luồng khác trong bước hiện tại, dẫn đến kết quả sai.
    
    **Giải pháp:**
    
    1. Sử dụng biến tạm thời (register) và thêm `__syncthreads()`.
    2. Sử dụng **Double Buffering**: Xen kẽ giữa hai mảng shared memory khác nhau trong mỗi lần lặp.

    ## 11.3 Cân nhắc hiệu quả công việc {#vi-work-efficiency}

    **Nhược điểm của Kogge-Stone:** Nó thực hiện $O(N \log N)$ phép toán.
    
    **So sánh:** Với 1,024 phần tử, CPU thực hiện ~1,000 phép cộng. Kogge-Stone thực hiện ~10,000.
    
    **Kết luận:** Kogge-Stone **không hiệu quả công việc**. Nó chỉ nhanh nếu bạn có thừa lớn các đơn vị thực thi để "lãng phí" vào các phép cộng dư thừa.

    ## 11.4 Scan song song: Thuật toán Brent-Kung {#vi-brent-kung}

    **Mục tiêu:** Đạt được độ phức tạp $O(N)$ để phù hợp với hiệu quả của CPU.
    
    **Cách tiếp cận hai giai đoạn:**
    
    1. **Giai đoạn Reduction (Up-sweep):** Xây dựng cây reduction để tính tổng toàn bộ của block.
    2. **Giai đoạn Distribution (Down-sweep):** Sử dụng các tổng một phần từ cây để điền các tổng tiền tố còn thiếu cho tất cả các phần tử khác.
    
    **Hiệu quả:** Nó thực hiện khoảng $2N$ phép toán. Nó **hiệu quả công việc** và tiêu thụ ít năng lượng/băng thông hơn Kogge-Stone, mặc dù mất nhiều bước hơn ($2 \log N$).

    ## 11.5 Coarsening để hiệu quả hơn nữa {#vi-coarsening}

    **Chiến lược:** Mỗi luồng xử lý một đoạn dữ liệu (ví dụ: 4 hoặc 8 phần tử) tuần tự trước.
    
    **Quy trình ba giai đoạn:**
    
    1. Scan tuần tự cục bộ các đoạn.
    2. Scan song song các "đuôi" (phần tử cuối) của mỗi đoạn.
    3. Cập nhật cục bộ để thêm kết quả trở lại các phần tử bên trong.
    
    **Kết quả:** Giảm đáng kể số lượng luồng và điểm đồng bộ hóa cần thiết.

    ## 11.6 Segmented Scan cho độ dài tùy ý {#vi-segmented}

    **Vấn đề:** Phần cứng giới hạn kích thước block ở 1,024 luồng.
    
    **Giải pháp phân cấp:**
    
    1. Scan các phần của dữ liệu độc lập.
    2. Ghi phần tử "cuối cùng" của mỗi phần vào mảng phụ.
    3. Scan mảng phụ.
    4. Thêm các giá trị đã scan trở lại các phần tương ứng.

    ## 11.7 Single-Pass Scan (Domino Scan) {#vi-domino}

    **Tối ưu hóa nâng cao:** Tránh nhiều lần khởi chạy kernel bằng cách truyền giá trị giữa các block trong khi kernel vẫn đang chạy.
    
    **Đồng bộ hóa liền kề:** Các block sử dụng "cờ" và atomic operation trong global memory để báo hiệu cho block "tiếp theo" rằng tổng một phần của chúng đã sẵn sàng.
    
    **Ngăn chặn Deadlock:** Sử dụng **Dynamic Block Indexing** để đảm bảo các block được xử lý theo đúng thứ tự, vì bộ lập lịch phần cứng mặc định không đảm bảo thực thi tuyến tính.

    ---

    **Điểm chính:** Chương 11 dạy rằng song song hóa đệ quy tuần tự yêu cầu thay đổi cơ bản trong thuật toán. Bạn phải chọn giữa **Kogge-Stone** (nhanh nhưng lãng phí) và **Brent-Kung** (hiệu quả công việc) và sử dụng chiến lược **Phân cấp** hoặc **Domino** để mở rộng đến kích thước dữ liệu thực tế.
