# Chapter 10: Reduction

=== "English"

    This is a newly added chapter in the 4th Edition. It focuses on the "Reduction" pattern—taking an array of values and condensing them into a single result (e.g., sum, max, min)—to teach the critical skill of **minimizing thread and memory divergence.**

    ## 10.1 Background {#en-background}

    **Definition:** A reduction derives a single value from an array using a binary associative operator (like $+$ or $\times$).
    
    **Identity Values:** Every operator needs an identity value (e.g., $0.0$ for addition, $1.0$ for multiplication, $-\infty$ for Max).
    
    **Sequential vs. Parallel:** Sequential reduction is $O(N)$. Parallel reduction aims to reduce this to $O(\log N)$ steps using a tree structure.

    ## 10.2 Reduction Trees {#en-trees}

    **The Structure:** Threads are organized into a "tree" where pairs of elements are summed in rounds.
    
    **Mathematical Requirements:**
    
    *   **Associativity:** $(a+b)+c = a+(b+c)$. This allows us to change the order of operations.
    *   **Commutativity:** $a+b = b+a$. This allows us to rearrange the data for better hardware efficiency.
    
    **Complexity:** While the number of steps is low ($O(\log N)$), the hardware must handle a massive drop in parallelism as the tree reaches the top (half the threads drop out every round).

    ## 10.3 A Simple Reduction Kernel {#en-simple}

    **Implementation:** An initial kernel where each thread adds two adjacent elements.
    
    **Limitations:** This basic version is limited to a single thread block, meaning it can only process up to 2048 elements (since a block has 1024 threads).

    ## 10.4 Minimizing Control Divergence (The "Convergent" Kernel) {#en-convergent}

    **The Problem:** The "simple" kernel uses a modulo operator (`%`) and strided indexing. This causes threads in the same warp to take different paths (some active, some idle), leading to heavy **Control Divergence** and wasting up to **65%** of hardware potential.
    
    **The Optimization:** The authors introduce a "Convergent" indexing strategy. By rearranging which threads do the work, they ensure that all active threads are packed into the same warps while idle threads are packed into separate warps. This effectively doubles the efficiency.

    ## 10.5 Minimizing Memory Divergence {#en-memory-divergence}

    **Coalescing:** The convergent indexing not only fixes the `if-else` pathing but also ensures that threads in a warp access adjacent memory locations.
    
    **Result:** This results in **3.9x fewer** global memory requests compared to the unoptimized version.

    ## 10.6 Minimizing Global Memory Accesses {#en-shared}

    **Shared Memory Strategy:** Instead of writing partial sums back to slow global memory at every level of the tree, threads load data into **Shared Memory** and perform the entire tree reduction there.
    
    **Efficiency:** This reduces global memory traffic to a single load per element and one final write.

    ## 10.7 Hierarchical Reduction for Arbitrary Length {#en-hierarchical}

    **The Scaling Problem:** Single blocks cannot process millions of elements.
    
    **Segmented Reduction:** The input is divided into segments, each handled by a different block.
    
    **Atomic Add:** Each block computes its local sum and then uses `atomicAdd` to update a single global variable. This allows the pattern to scale to datasets of any size.

    ## 10.8 Thread Coarsening for Reduced Overhead {#en-coarsening}

    **The Strategy:** Before starting the reduction tree, each thread sequentially sums a "chunk" of elements (e.g., 4 or 8 elements).
    
    **Benefit:** This reduces the total number of blocks and the amount of expensive synchronization (`__syncthreads`) required. It makes the kernel much more "work-efficient" and closer to the sequential speed for the initial phase.

    ---

    **Key Takeaway:** Chapter 10 is a masterclass in **hardware-aware algorithm design.** It teaches you that the *order* in which you process data (the tree structure) matters less for the math, but matters *enormously* for the hardware. By ensuring active threads stay together (Convergent indexing), you maximize the GPU's throughput.

=== "Tiếng Việt"

    Đây là chương mới được thêm vào Ấn bản thứ 4. Nó tập trung vào mẫu "Reduction"—lấy một mảng giá trị và rút gọn chúng thành một kết quả duy nhất (ví dụ: tổng, max, min)—để dạy kỹ năng quan trọng về **giảm thiểu phân kỳ luồng và bộ nhớ.**

    ## 10.1 Bối cảnh {#vi-background}

    **Định nghĩa:** Reduction tạo ra một giá trị duy nhất từ mảng bằng cách sử dụng toán tử kết hợp nhị phân (như $+$ hoặc $\times$).
    
    **Giá trị đơn vị:** Mỗi toán tử cần một giá trị đơn vị (ví dụ: $0.0$ cho phép cộng, $1.0$ cho phép nhân, $-\infty$ cho Max).
    
    **Tuần tự vs. Song song:** Reduction tuần tự là $O(N)$. Reduction song song nhằm giảm xuống $O(\log N)$ bước bằng cách sử dụng cấu trúc cây.

    ## 10.2 Cây Reduction {#vi-trees}

    **Cấu trúc:** Các luồng được tổ chức thành "cây" nơi các cặp phần tử được cộng trong các vòng.
    
    **Yêu cầu toán học:**
    
    *   **Tính kết hợp:** $(a+b)+c = a+(b+c)$. Điều này cho phép chúng ta thay đổi thứ tự các phép toán.
    *   **Tính giao hoán:** $a+b = b+a$. Điều này cho phép chúng ta sắp xếp lại dữ liệu để có hiệu quả phần cứng tốt hơn.
    
    **Độ phức tạp:** Trong khi số bước thấp ($O(\log N)$), phần cứng phải xử lý sự sụt giảm lớn về tính song song khi cây đạt đến đỉnh (một nửa số luồng rơi ra mỗi vòng).

    ## 10.3 Kernel Reduction đơn giản {#vi-simple}

    **Triển khai:** Kernel ban đầu nơi mỗi luồng cộng hai phần tử liền kề.
    
    **Giới hạn:** Phiên bản cơ bản này bị giới hạn ở một thread block duy nhất, nghĩa là nó chỉ có thể xử lý tối đa 2048 phần tử (vì một block có 1024 luồng).

    ## 10.4 Giảm thiểu phân kỳ điều khiển (Kernel "Convergent") {#vi-convergent}

    **Vấn đề:** Kernel "đơn giản" sử dụng toán tử modulo (`%`) và chỉ số bước nhảy. Điều này khiến các luồng trong cùng một warp đi theo các đường khác nhau (một số hoạt động, một số nhàn rỗi), dẫn đến **Phân kỳ điều khiển** nặng và lãng phí tới **65%** tiềm năng phần cứng.
    
    **Tối ưu hóa:** Các tác giả giới thiệu chiến lược chỉ số "Convergent". Bằng cách sắp xếp lại luồng nào làm việc, họ đảm bảo rằng tất cả các luồng hoạt động được đóng gói vào cùng các warp trong khi các luồng nhàn rỗi được đóng gói vào các warp riêng biệt. Điều này tăng gấp đôi hiệu quả.

    ## 10.5 Giảm thiểu phân kỳ bộ nhớ {#vi-memory-divergence}

    **Coalescing:** Chỉ số convergent không chỉ sửa đường dẫn `if-else` mà còn đảm bảo rằng các luồng trong warp truy cập các vị trí bộ nhớ liền kề.
    
    **Kết quả:** Điều này dẫn đến **ít hơn 3.9 lần** yêu cầu bộ nhớ global so với phiên bản chưa tối ưu.

    ## 10.6 Giảm thiểu truy cập bộ nhớ Global {#vi-shared}

    **Chiến lược Shared Memory:** Thay vì ghi tổng một phần trở lại bộ nhớ global chậm ở mọi cấp của cây, các luồng tải dữ liệu vào **Shared Memory** và thực hiện toàn bộ reduction cây ở đó.
    
    **Hiệu quả:** Điều này giảm lưu lượng bộ nhớ global xuống một lần tải mỗi phần tử và một lần ghi cuối cùng.

    ## 10.7 Reduction phân cấp cho độ dài tùy ý {#vi-hierarchical}

    **Vấn đề mở rộng:** Block đơn lẻ không thể xử lý hàng triệu phần tử.
    
    **Reduction phân đoạn:** Đầu vào được chia thành các đoạn, mỗi đoạn được xử lý bởi một block khác nhau.
    
    **Atomic Add:** Mỗi block tính tổng cục bộ của nó và sau đó sử dụng `atomicAdd` để cập nhật một biến global duy nhất. Điều này cho phép mẫu mở rộng đến tập dữ liệu có kích thước bất kỳ.

    ## 10.8 Thread Coarsening để giảm chi phí quản lý {#vi-coarsening}

    **Chiến lược:** Trước khi bắt đầu cây reduction, mỗi luồng tuần tự cộng một "khối" các phần tử (ví dụ: 4 hoặc 8 phần tử).
    
    **Lợi ích:** Điều này giảm tổng số block và lượng đồng bộ hóa đắt tiền (`__syncthreads`) cần thiết. Nó làm cho kernel "hiệu quả công việc" hơn nhiều và gần hơn với tốc độ tuần tự cho giai đoạn đầu.

    ---

    **Điểm chính:** Chương 10 là một lớp học chuyên sâu về **thiết kế thuật toán nhận thức phần cứng.** Nó dạy bạn rằng *thứ tự* mà bạn xử lý dữ liệu (cấu trúc cây) ít quan trọng hơn cho toán học, nhưng quan trọng *cực kỳ* cho phần cứng. Bằng cách đảm bảo các luồng hoạt động ở cùng nhau (Chỉ số convergent), bạn tối đa hóa thông lượng của GPU.
