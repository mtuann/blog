# Chapter 12: Parallel Merge

=== "English"

    This chapter explores the **Parallel Merge** pattern, which is the foundation of many complex algorithms, including Parallel Merge Sort. It introduces the challenge of **dynamic input identification**—where threads cannot know which data to process until they perform a search.

    ## 12.1 Background {#en-background}

    **Definition:** An ordered merge takes two previously sorted lists ($A$ and $B$) and combines them into a single sorted list ($C$).
    
    **Stability:** A "stable" merge ensures that if two elements have the same value, their relative order from the original lists is preserved.
    
    **Importance:** Merge is the core of the Merge Sort algorithm and is a critical component of modern MapReduce frameworks used in big data processing.

    ## 12.2 A Sequential Merge Algorithm {#en-sequential}

    **The Logic:** A simple `while` loop compares the current head of list $A$ with the current head of list $B$, picking the smaller one and moving a pointer forward.
    
    **Complexity:** $O(m + n)$, where $m$ and $n$ are the lengths of the lists. It is highly efficient for a single processor but entirely serial.

    ## 12.3 A Parallelization Approach {#en-parallelization}

    **The Strategy:** Partition the output array ($C$) into equal-sized segments and assign each segment to a thread.
    
    **The Problem:** Because the lists are sorted but the values are unknown, a thread doesn't know where its assigned segment of $C$ begins in the input lists $A$ and $B$.
    
    **The Solution (Co-rank):** Each thread must find its "split points" in the input arrays using a **Co-rank function**.

    ## 12.4 Co-rank Function Implementation {#en-co-rank}

    **The Concept:** The co-rank function uses a **Binary Search** to find the unique $i$ and $j$ indices in arrays $A$ and $B$ that contribute to a specific position $k$ in the output array $C$.
    
    **Logic:** It searches for a point where $A[i-1] \le B[j]$ and $B[j-1] < A[i]$.
    
    **Complexity:** $O(\log N)$, where $N$ is the length of the longer input list. This search is performed by every thread to determine its work boundaries.

    ## 12.5 A Basic Parallel Merge Kernel {#en-basic}

    **Execution:** Each thread calls the co-rank function to find its starting and ending points in $A$ and $B$, then performs a standard sequential merge on those specific sub-segments.
    
    **Bottleneck:** This basic version suffers from **uncoalesced memory accesses** because threads in a warp are merging different data values at different speeds, jumping around the global memory.

    ## 12.6 A Tiled Merge Kernel to Improve Coalescing {#en-tiled}

    **The Optimization:** Threads in a block collaborate to load tiles of $A$ and $B$ into **Shared Memory**.
    
    **The Challenge:** Unlike previous patterns, we don't know the "A-to-B ratio" for a tile. In the worst case, a tile's output might require *only* elements from $A$ or *only* elements from $B$.
    
    **Handling Uncertainty:** Each block must load a tile of $A$ and a tile of $B$. This ensures all necessary data is on-chip, but it results in only about 50% of the loaded data being used in each step.

    ## 12.7 A Circular Buffer Merge Kernel {#en-circular}

    **The Advanced Optimization:** To fix the 50% data waste in standard tiling, the authors introduce a **Circular Buffer** in shared memory.
    
    **Mechanism:** Threads keep track of "leftover" elements in shared memory that weren't used in the previous phase. They only load enough new elements from global memory to refill the buffer.
    
    **Payoff:** This maximizes memory bandwidth utilization but significantly increases code complexity, requiring a "simplified model" for threads to index into the wrapped buffer.

    ## 12.8 Thread Coarsening for Merge {#en-coarsening}

    **Efficiency:** The co-rank binary search is a high-overhead operation.
    
    **The Strategy:** By having each thread process more elements (coarsening), the "cost" of the binary search is amortized over a larger amount of work, improving the overall work efficiency of the kernel.

    ---

    **Key Takeaway:** Chapter 12 teaches you how to parallelize algorithms where **workload boundaries are data-dependent.** The core lesson is the **Co-rank function**, which uses binary search to let threads independently "claim" their portion of a global task, while **Circular Buffers** solve the unique memory efficiency problems created by this dynamic behavior.

=== "Tiếng Việt"

    Chương này khám phá mẫu **Parallel Merge**, là nền tảng của nhiều thuật toán phức tạp, bao gồm Parallel Merge Sort. Nó giới thiệu thách thức về **xác định đầu vào động**—nơi các luồng không thể biết dữ liệu nào cần xử lý cho đến khi chúng thực hiện tìm kiếm.

    ## 12.1 Bối cảnh {#vi-background}

    **Định nghĩa:** Một phép hợp nhất có thứ tự lấy hai danh sách đã được sắp xếp trước đó ($A$ và $B$) và kết hợp chúng thành một danh sách sắp xếp duy nhất ($C$).
    
    **Tính ổn định:** Hợp nhất "ổn định" đảm bảo rằng nếu hai phần tử có cùng giá trị, thứ tự tương đối của chúng từ các danh sách ban đầu được giữ nguyên.
    
    **Tầm quan trọng:** Merge là cốt lõi của thuật toán Merge Sort và là thành phần quan trọng của các khung MapReduce hiện đại được sử dụng trong xử lý dữ liệu lớn.

    ## 12.2 Thuật toán hợp nhất tuần tự {#vi-sequential}

    **Logic:** Vòng lặp `while` đơn giản so sánh phần đầu hiện tại của danh sách $A$ với phần đầu hiện tại của danh sách $B$, chọn phần tử nhỏ hơn và di chuyển con trỏ về phía trước.
    
    **Độ phức tạp:** $O(m + n)$, trong đó $m$ và $n$ là độ dài của các danh sách. Nó rất hiệu quả cho một bộ xử lý đơn lẻ nhưng hoàn toàn tuần tự.

    ## 12.3 Cách tiếp cận song song hóa {#vi-parallelization}

    **Chiến lược:** Phân chia mảng đầu ra ($C$) thành các đoạn có kích thước bằng nhau và gán mỗi đoạn cho một luồng.
    
    **Vấn đề:** Vì các danh sách đã được sắp xếp nhưng giá trị chưa biết, một luồng không biết phân đoạn $C$ được gán của nó bắt đầu từ đâu trong các danh sách đầu vào $A$ và $B$.
    
    **Giải pháp (Co-rank):** Mỗi luồng phải tìm "điểm chia" của nó trong các mảng đầu vào bằng cách sử dụng **hàm Co-rank**.

    ## 12.4 Triển khai hàm Co-rank {#vi-co-rank}

    **Khái niệm:** Hàm co-rank sử dụng **Tìm kiếm nhị phân** để tìm các chỉ số $i$ và $j$ duy nhất trong các mảng $A$ và $B$ đóng góp vào một vị trí $k$ cụ thể trong mảng đầu ra $C$.
    
    **Logic:** Nó tìm kiếm điểm mà $A[i-1] \le B[j]$ và $B[j-1] < A[i]$.
    
    **Độ phức tạp:** $O(\log N)$, trong đó $N$ là độ dài của danh sách đầu vào dài hơn. Việc tìm kiếm này được thực hiện bởi mọi luồng để xác định ranh giới công việc của nó.

    ## 12.5 Kernel Parallel Merge cơ bản {#vi-basic}

    **Thực thi:** Mỗi luồng gọi hàm co-rank để tìm điểm bắt đầu và điểm kết thúc của nó trong $A$ và $B$, sau đó thực hiện hợp nhất tuần tự tiêu chuẩn trên các phân đoạn cụ thể đó.
    
    **Nút thắt cổ chai:** Phiên bản cơ bản này bị hiện tượng **truy cập bộ nhớ không gộp (uncoalesced)** vì các luồng trong cùng một warp hợp nhất các giá trị dữ liệu khác nhau với tốc độ khác nhau, nhảy xung quanh bộ nhớ global.

    ## 12.6 Kernel Merge Tiled để cải thiện Coalescing {#vi-tiled}

    **Tối ưu hóa:** Các luồng trong một block cộng tác để tải các tile của $A$ và $B$ vào **Shared Memory**.
    
    **Thách thức:** Không giống như các mẫu trước đó, chúng ta không biết "tỷ lệ A-so-với-B" cho một tile. Trong trường hợp xấu nhất, đầu ra của một tile có thể *chỉ* yêu cầu các phần tử từ $A$ hoặc *chỉ* từ $B$.
    
    **Xử lý sự không chắc chắn:** Mỗi block phải tải một tile của $A$ và một tile của $B$. Điều này đảm bảo tất cả dữ liệu cần thiết đều có trên chip, nhưng dẫn đến việc chỉ khoảng 50% dữ liệu đã tải thực sự được sử dụng trong mỗi bước.

    ## 12.7 Kernel Merge Circular Buffer {#vi-circular}

    **Tối ưu hóa nâng cao:** Để khắc phục việc lãng phí 50% dữ liệu trong tiling tiêu chuẩn, các tác giả giới thiệu **Circular Buffer** trong shared memory.
    
    **Cơ chế:** Các luồng theo dõi các phần tử "dư thừa" trong shared memory không được sử dụng ở giai đoạn trước. Chúng chỉ tải đủ các phần tử mới từ bộ nhớ global để làm đầy lại buffer.
    
    **Lợi ích:** Điều này tối đa hóa việc sử dụng băng thông bộ nhớ nhưng làm tăng đáng kể độ phức tạp của mã nguồn, yêu cầu một "mô hình đơn giản hóa" để các luồng đánh chỉ số vào buffer vòng.

    ## 12.8 Thread Coarsening cho Merge {#vi-coarsening}

    **Hiệu quả:** Tìm kiếm nhị phân co-rank là một thao tác có chi phí cao.
    
    **Chiến lược:** Bằng cách để mỗi luồng xử lý nhiều phần tử hơn (làm thô), "chi phí" của việc tìm kiếm nhị phân được phân bổ cho một lượng công việc lớn hơn, cải thiện hiệu quả công việc tổng thể của kernel.

    ---

    **Điểm chính:** Chương 12 dạy bạn cách song song hóa các thuật toán nơi **ranh giới khối lượng công việc phụ thuộc vào dữ liệu.** Bài học cốt lõi là **hàm Co-rank**, sử dụng tìm kiếm nhị phân để các luồng độc lập "xác nhận" phần việc của mình trong một nhiệm vụ toàn cục, trong khi **Circular Buffer** giải quyết các vấn đề hiệu quả bộ nhớ duy nhất do hành vi động này tạo ra.
