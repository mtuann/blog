# Chapter 14: Sparse Matrix Computation

=== "English"

    This chapter addresses the challenge of processing "Sparse" data—matrices where the vast majority of elements are zero. Processing these like dense matrices is wasteful; however, compacting them introduces irregularity that can slow down a GPU.

    ## 14.1 Background {#en-background}

    **Definition:** A sparse matrix is one in which most elements are zero. They occur frequently in engineering, physics, and financial modeling (e.g., linear systems like $Ax + y = z$).
    
    **The Goal:** Remove zeros from storage to save memory capacity and bandwidth.
    
    **Design Considerations for Formats:**
    
    1.  **Space Efficiency:** How much memory is saved?
    2.  **Flexibility:** How easy is it to add or remove non-zero elements?
    3.  **Accessibility:** How easy is it to find all elements in a specific row or column?
    4.  **Memory Access Efficiency:** Does the format support **coalesced** access?
    5.  **Load Balance:** Does it distribute work evenly across threads?

    ## 14.2 A Simple SpMV Kernel with the COO Format {#en-coo}

    **Format (Coordinate List):** Stores three arrays of equal length: `rowIdx`, `colIdx`, and `value`.
    
    **Parallel Strategy:** Assign one thread to **each non-zero element**.
    
    **Pros:** Perfectly load-balanced (every thread does one multiply-add) and memory accesses are coalesced.
    
    **Cons:** Requires **Atomic Operations** (`atomicAdd`) because multiple threads might belong to the same row and try to update the same output element simultaneously. Atomics significantly slow down execution.

    ## 14.3 Grouping Row Non-zeros with the CSR Format {#en-csr}

    **Format (Compressed Sparse Row):** Groups non-zeros by row. It uses `value`, `colIdx`, and a special `rowPtrs` array that acts as a map to where each row starts.
    
    **Parallel Strategy:** Assign one thread to **each row**.
    
    **Pros:** Eliminates the need for atomics because each thread "owns" its output row. It is more space-efficient than COO.
    
    **Cons:**
    
    *   **Uncoalesced Access:** Since threads in a warp work on different rows, their first elements are far apart in memory.
    *   **Load Imbalance:** A thread assigned to a row with 100 elements will work much longer than a thread assigned to a row with 2 elements, causing warp divergence.

    ## 14.4 Improving Memory Coalescing with the ELL Format {#en-ell}

    **Format (ELLPACK):** Pads all rows with zeros so they all match the length of the longest row, then **transposes** the matrix into column-major order.
    
    **Parallel Strategy:** Assign one thread to each row.
    
    **Pros:** Because of the transposition, threads in a warp access adjacent memory locations, enabling **full memory coalescing**.
    
    **Cons:** If one row is very long and others are short, ELL wastes massive amounts of memory on "padding" zeros.

    ## 14.5 Regulating Padding: The Hybrid ELL-COO Format {#en-hybrid}

    **The Strategy:** A "best of both worlds" approach.
    
    **Mechanism:** Determine a "typical" row length. Most data is stored in **ELL** format to that length. Any elements that exceed that length (the "extra-long" rows) are moved to a separate **COO** structure.
    
    **Benefit:** Reduces the memory waste of ELL while keeping the performance of coalesced access for the majority of the data.

    ## 14.6 Reducing Control Divergence with the JDS Format {#en-jds}

    **Format (Jagged Diagonal Storage):** Sorts the rows of the matrix by their number of non-zero elements (from longest to shortest) before storing them.
    
    **Benefit:** Threads in the same warp will now process rows of **similar lengths**. This significantly reduces control divergence and improves load balancing.
    
    **Trade-off:** Requires an extra step to reorder the results back to the original row indices after the math is done.

    ## 14.7 Summary: Regularization vs. Compaction {#en-summary}

    *   The chapter concludes that there is no "perfect" sparse format.
    *   **CSR** is the general standard for storage.
    *   **ELL/JDS** are better for performance but require "regularizing" the data.
    *   **SpMV (Sparse Matrix-Vector Multiplication)** usually has a low arithmetic intensity (0.25 OP/B), making memory bandwidth the ultimate bottleneck regardless of the format.

    ---

    **Key Takeaway:** Chapter 14 teaches that "irregularity is the enemy of performance." High-performance sparse computing on a GPU requires choosing a format that balances memory compaction (saving space) with regularization (ensuring threads work together and access memory contiguously).

=== "Tiếng Việt"

    Chương này giải quyết thách thức trong việc xử lý dữ liệu "Thưa (Sparse)"—các ma trận mà đại đa số các phần tử bằng không. Xử lý chúng như các ma trận đặc là một sự lãng phí; tuy nhiên, việc nén chúng lại tạo ra sự không đều (irregularity) có thể làm chậm GPU.

    ## 14.1 Bối cảnh {#vi-background}

    **Định nghĩa:** Một ma trận thưa là ma trận mà hầu hết các phần tử có giá trị bằng không. Chúng xuất hiện thường xuyên trong kỹ thuật, vật lý và mô hình tài chính (ví dụ: các hệ thống tuyến tính như $Ax + y = z$).
    
    **Mục tiêu:** Loại bỏ các số không khỏi lưu trữ để tiết kiệm dung lượng bộ nhớ và băng thông.
    
    **Xem xét thiết kế các định dạng:**
    
    1.  **Hiệu quả không gian:** Tiết kiệm được bao nhiêu bộ nhớ?
    2.  **Tính linh hoạt:** Việc thêm hoặc xóa các phần tử khác không dễ dàng như thế nào?
    3.  **Khả năng truy cập:** Việc tìm tất cả các phần tử trong một hàng hoặc cột cụ thể dễ dàng như thế nào?
    4.  **Hiệu quả truy cập bộ nhớ:** Định dạng có hỗ trợ truy cập **gộp (coalesced)** không?
    5.  **Cân bằng tải:** Nó có phân phối công việc đồng đều giữa các luồng không?

    ## 14.2 Kernel SpMV đơn giản với định dạng COO {#vi-coo}

    **Định dạng (Coordinate List):** Lưu trữ ba mảng có độ dài bằng nhau: `rowIdx`, `colIdx`, và `value`.
    
    **Chiến lược song song:** Gán một luồng cho **mỗi phần tử khác không**.
    
    **Ưu điểm:** Cân bằng tải hoàn hảo (mỗi luồng thực hiện một phép nhân-cộng) và các truy cập bộ nhớ được gộp lại.
    
    **Nhược điểm:** Yêu cầu **Atomic Operations** (`atomicAdd`) vì nhiều luồng có thể thuộc cùng một hàng và cố gắng cập nhật cùng một phần tử đầu ra đồng thời. Các thao tác Atomic làm chậm đáng kể quá trình thực thi.

    ## 14.3 Nhóm các phần tử khác không theo hàng với định dạng CSR {#vi-csr}

    **Định dạng (Compressed Sparse Row):** Nhóm các phần tử khác không theo hàng. Nó sử dụng `value`, `colIdx`, và một mảng `rowPtrs` đặc biệt đóng vai trò như một bản đồ cho biết mỗi hàng bắt đầu từ đâu.
    
    **Chiến lược song song:** Gán một luồng cho **mỗi hàng**.
    
    **Ưu điểm:** Loại bỏ nhu cầu sử dụng atomic vì mỗi luồng "sở hữu" hàng đầu ra của chính nó. Nó tiết kiệm không gian hơn COO.
    
    **Nhược điểm:**
    
    *   **Truy cập không gộp:** Vì các luồng trong cùng một warp làm việc trên các hàng khác nhau, các phần tử đầu tiên của chúng cách xa nhau trong bộ nhớ.
    *   **Mất cân bằng tải:** Một luồng được gán cho một hàng có 100 phần tử sẽ làm việc lâu hơn nhiều so với một luồng được gán cho hàng có 2 phần tử, gây ra hiện tượng phân kỳ warp (warp divergence).

    ## 14.4 Cải thiện Memory Coalescing với định dạng ELL {#vi-ell}

    **Định dạng (ELLPACK):** Đệm tất cả các hàng bằng số không để chúng khớp với độ dài của hàng dài nhất, sau đó **chuyển vị (transpose)** ma trận sang thứ tự column-major.
    
    **Chiến lược song song:** Gán một luồng cho mỗi hàng.
    
    **Ưu điểm:** Nhờ phép chuyển vị, các luồng trong cùng một warp truy cập các vị trí bộ nhớ liền kề, cho phép **gộp bộ nhớ hoàn toàn**.
    
    **Nhược điểm:** Nếu một hàng rất dài và các hàng khác ngắn, ELL lãng phí một lượng lớn bộ nhớ cho các số không "đệm".

    ## 14.5 Điều tiết việc đệm: Định dạng Hybrid ELL-COO {#vi-hybrid}

    **Chiến lược:** Cách tiếp cận "tốt nhất của cả hai thế giới".
    
    **Cơ chế:** Xác định một độ dài hàng "điển hình". Phần lớn dữ liệu được lưu trữ theo định dạng **ELL** tới độ dài đó. Bất kỳ phần tử nào vượt quá độ dài đó (các hàng "siêu dài") sẽ được chuyển sang cấu trúc **COO** riêng biệt.
    
    **Lợi ích:** Giảm sự lãng phí bộ nhớ của ELL trong khi vẫn giữ được hiệu suất truy cập gộp cho phần lớn dữ liệu.

    ## 14.6 Giảm phân kỳ điều khiển với định dạng JDS {#vi-jds}

    **Định dạng (Jagged Diagonal Storage):** Sắp xếp các hàng của ma trận theo số lượng phần tử khác không (từ dài nhất đến ngắn nhất) trước khi lưu trữ chúng.
    
    **Lợi ích:** Các luồng trong cùng một warp bây giờ sẽ xử lý các hàng có **độ dài tương tự nhau**. Điều này làm giảm đáng kể phân kỳ điều khiển và cải thiện cân bằng tải.
    
    **Đánh đổi:** Yêu cầu thêm một bước để sắp xếp lại kết quả về chỉ số hàng ban đầu sau khi tính toán xong.

    ## 14.7 Tóm tắt: Quy chuẩn hóa vs. Nén {#vi-summary}

    *   Chương kết luận rằng không có định dạng thưa nào là "hoàn hảo".
    *   **CSR** là tiêu chuẩn chung cho lưu trữ.
    *   **ELL/JDS** tốt hơn cho hiệu suất nhưng yêu cầu "quy chuẩn hóa" dữ liệu.
    *   **SpMV (Sparse Matrix-Vector Multiplication)** thường có cường độ số học thấp (0.25 OP/B), khiến băng thông bộ nhớ trở thành nút thắt cổ chai cuối cùng bất kể định dạng nào.

    ---

    **Điểm chính:** Chương 14 dạy rằng "sự không đồng đều là kẻ thù của hiệu suất." Tính toán ma trận thưa hiệu suất cao trên GPU yêu cầu chọn một định dạng cân bằng giữa việc nén bộ nhớ (tiết kiệm không gian) với việc quy chuẩn hóa (đảm bảo các luồng làm việc cùng nhau và truy cập bộ nhớ liên tục).
