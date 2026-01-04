# Chapter 13: Parallel Sorting

=== "English"

    Sorting is one of the most fundamental operations in computer science. This chapter explores how to adapt various sorting algorithms for the GPU, focusing on balancing workload and memory efficiency.

    ## 13.1 Background {#en-background}

    **Categories:**

    *   **Comparison-based:** Lower bound of $O(N \log N)$ (e.g., Merge Sort).
    *   **Non-comparison-based:** Can achieve $O(N)$ but is often limited to specific data types like integers (e.g., Radix Sort).

    ## 13.2 Radix Sort {#en-radix-sort}

    **The Concept:** Distributes keys into "buckets" based on their individual digits or bits.
    
    **LSD approach:** The book focuses on the **Least Significant Digit** approach, starting from the rightmost bit and moving to the leftmost.
    
    **Iterations:** For $N$-bit keys, the algorithm requires $N$ iterations if using a 1-bit radix.

    ## 13.3 Parallel Radix Sort {#en-parallel-radix}

    **Mapping:** Assign one thread to each input key.
    
    **The Challenge:** Each thread must calculate where its key goes in the output array (the **Destination Index**).
    
    **The Logic:**
    
    *   If the key's bit is **0**: Its index is the count of all "0" bits before it.
    *   If the key's bit is **1**: Its index is the total count of "0"s in the list plus the count of all "1" bits before it.
    
    **The Primitive:** This is solved by performing an **Exclusive Scan** (from Chapter 11) on the bit values.

    ## 13.4 Optimizing for Memory Coalescing {#en-coalescing}

    **The Problem:** The basic parallel radix sort has a "scatter" write pattern. Since threads in a warp have different bits (0 or 1), they try to write to distant parts of the global memory simultaneously, resulting in **uncoalesced writes**.
    
    **The Optimization:** Sort locally in **Shared Memory** first.
    
    **The Process:** Threads in a block perform a local sort to create two contiguous "sub-buckets" (one for 0s, one for 1s) in shared memory. Then, the block writes these sub-buckets to global memory in a perfectly **coalesced** manner.

    ## 13.5 Choice of Radix Value {#en-radix-value}

    **Trade-offs:** You can use a larger radix (e.g., 4 bits at a time instead of 1).
    
    *   **Pros:** Fewer total kernel passes (e.g., 8 passes for 32-bit keys instead of 32).
    *   **Cons:** More buckets ($2^4 = 16$ buckets). This fragments the memory writes, making coalescing harder and increasing the size of the auxiliary scan table.

    ## 13.6 Thread Coarsening to Improve Coalescing {#en-coarsening}

    **The Strategy:** Assign multiple keys to each thread.
    
    **Benefit:** This creates larger local buckets within each block. Larger local buckets are more likely to fill up DRAM "bursts," leading to higher effective memory bandwidth and reducing the total number of thread blocks (lowering scan overhead).

    ## 13.7 Parallel Merge Sort {#en-merge-sort}

    **The Concept:** Use a "Divide and Conquer" approach.
    
    **The Process:**
    
    1. Sort small segments of the array locally (e.g., using a fast local sort).
    2. Iteratively merge these segments using the **Parallel Merge** pattern (from Chapter 12).
    
    **Comparison:** Unlike Radix Sort, Merge Sort is more general and can handle complex data types that only define a "less than" operator.

    ## 13.8 Other Parallel Sort Methods {#en-other}

    *   **Odd-Even Transposition Sort:** Simple but inefficient ($O(N^2)$).
    *   **Sorting Networks (Bitonic Sort):** Uses a fixed pattern of comparisons; very efficient for small, fixed-size lists.
    *   **Sample Sort:** A "Top-Down" approach that partitions data into many buckets based on "samples"; excellent for very large scales and multi-GPU systems.

    ---

    **Key Takeaway:** Chapter 13 teaches that sorting on a GPU is less about "sorting logic" and more about **efficient data movement.** The most performant sorts (like Radix) rely heavily on **Exclusive Scan** to calculate indices and use **Shared Memory Buffering** to ensure that writes to global memory are coalesced.

=== "Tiếng Việt"

    Sắp xếp là một trong những thao tác cơ bản nhất trong khoa học máy tính. Chương này khám phá cách điều chỉnh các thuật toán sắp xếp khác nhau cho GPU, tập trung vào việc cân bằng khối lượng công việc và hiệu quả bộ nhớ.

    ## 13.1 Bối cảnh {#vi-background}

    **Các loại:**

    *   **Dựa trên so sánh:** Giới hạn dưới của $O(N \log N)$ (ví dụ: Merge Sort).
    *   **Không dựa trên so sánh:** Có thể đạt được $O(N)$ nhưng thường giới hạn ở các loại dữ liệu cụ thể như số nguyên (ví dụ: Radix Sort).

    ## 13.2 Radix Sort {#vi-radix-sort}

    **Khái niệm:** Phân phối các khóa vào các "thùng (bucket)" dựa trên các chữ số hoặc bit riêng lẻ của chúng.
    
    **Cách tiếp cận LSD:** Cuốn sách tập trung vào cách tiếp cận **Least Significant Digit** (chữ số ít quan trọng nhất), bắt đầu từ bit tận cùng bên phải và di chuyển sang bên trái.
    
    **Số lần lặp:** Đối với các khóa $N$-bit, thuật toán yêu cầu $N$ lần lặp nếu sử dụng cơ số (radix) 1-bit.

    ## 13.3 Parallel Radix Sort {#vi-parallel-radix}

    **Ánh xạ:** Gán một luồng cho mỗi khóa đầu vào.
    
    **Thách thức:** Mỗi luồng phải tính toán nơi khóa của nó sẽ đến trong mảng đầu ra (**Destination Index**).
    
    **Logic:**
    
    *   Nếu bit của khóa là **0**: Chỉ số của nó là số lượng tất cả các bit "0" trước nó.
    *   Nếu bit của khóa là **1**: Chỉ số của nó là tổng số lượng các bit "0" trong danh sách cộng với số lượng tất cả các bit "1" trước nó.
    
    **Nguyên thủy:** Điều này được giải quyết bằng cách thực hiện một phép **Exclusive Scan** (từ Chương 11) trên các giá trị bit.

    ## 13.4 Tối ưu hóa cho Memory Coalescing {#vi-coalescing}

    **Vấn đề:** Sắp xếp radix song song cơ bản có mẫu ghi dữ liệu "phân tán (scatter)". Vì các luồng trong cùng một warp có các bit khác nhau (0 hoặc 1), chúng cố gắng ghi vào các phần cách xa nhau trên bộ nhớ global đồng thời, dẫn đến **các thao tác ghi không gộp (uncoalesced)**.
    
    **Tối ưu hóa:** Sắp xếp cục bộ trong **Shared Memory** trước.
    
    **Quy trình:** Các luồng trong một block thực hiện sắp xếp cục bộ để tạo ra hai "thùng con" liên tiếp (một cho bit 0, một cho bit 1) trong shared memory. Sau đó, block ghi các thùng con này vào bộ nhớ global theo cách **gộp (coalesced)** hoàn hảo.

    ## 13.5 Lựa chọn giá trị Radix {#vi-radix-value}

    **Đánh đổi:** Bạn có thể sử dụng cơ số lớn hơn (ví dụ: 4 bit một lúc thay vì 1).
    
    *   **Ưu điểm:** Tổng số lần chạy kernel ít hơn (ví dụ: 8 lần cho khóa 32-bit thay vì 32).
    *   **Nhược điểm:** Nhiều thùng hơn ($2^4 = 16$ thùng). Điều này làm phân mảnh các thao tác ghi bộ nhớ, khiến việc gộp dữ liệu khó khăn hơn và làm tăng kích thước của bảng scan phụ trợ.

    ## 13.6 Thread Coarsening để cải thiện Coalescing {#vi-coarsening}

    **Chiến lược:** Gán nhiều khóa cho mỗi luồng.
    
    **Lợi ích:** Điều này tạo ra các thùng cục bộ lớn hơn trong mỗi block. Các thùng cục bộ lớn hơn có nhiều khả năng làm đầy các "bursts" của DRAM, dẫn đến băng thông bộ nhớ hiệu dụng cao hơn và giảm tổng số thread block (giảm chi phí scan).

    ## 13.7 Parallel Merge Sort {#vi-merge-sort}

    **Khái niệm:** Sử dụng cách tiếp cận "Chia để trị (Divide and Conquer)".
    
    **Quy trình:**
    
    1. Sắp xếp các đoạn nhỏ của mảng cục bộ (ví dụ: sử dụng sắp xếp cục bộ nhanh).
    2. Hợp nhất lặp đi lặp lại các đoạn này bằng cách sử dụng mẫu **Parallel Merge** (từ Chương 12).
    
    **So sánh:** Không giống như Radix Sort, Merge Sort tổng quát hơn và có thể xử lý các kiểu dữ liệu phức tạp chỉ xác định toán tử "nhỏ hơn".

    ## 13.8 Các phương pháp sắp xếp song song khác {#vi-other}

    *   **Odd-Even Transposition Sort:** Đơn giản nhưng không hiệu quả ($O(N^2)$).
    *   **Sorting Networks (Bitonic Sort):** Sử dụng một mẫu so sánh cố định; rất hiệu quả cho các danh sách có kích thước cố định và nhỏ.
    *   **Sample Sort:** Một cách tiếp cận "Từ trên xuống" phân chia dữ liệu thành nhiều thùng dựa trên các "mẫu (samples)"; xuất sắc cho quy mô rất lớn và hệ thống đa GPU.

    ---

    **Điểm chính:** Chương 13 dạy rằng sắp xếp trên GPU ít quan trọng về "logic sắp xếp" mà quan trọng hơn về **di chuyển dữ liệu hiệu quả.** Các loại sắp xếp hiệu suất cao nhất (như Radix) dựa trên **Exclusive Scan** để tính toán chỉ số và sử dụng **Shared Memory Buffering** để đảm bảo các thao tác ghi vào bộ nhớ global được gộp lại.
