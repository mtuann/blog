# Chapter 19: Programming Strategy and Goals

=== "English"

    This chapter acts as a high-level recap of the book's philosophy. It moves away from specific code and focuses on the mental frameworks required to solve complex problems using massive parallelism.

    ## 19.1 Goals of Parallel Computing {#en-goals}

    The authors identify three primary reasons to pursue parallel programming:

    1.  **Solve a problem in less time (Speed):** Meeting strict real-time deadlines (e.g., finishing a financial risk analysis in 4 hours instead of 200).
    2.  **Solve bigger problems (Scale):** Handling larger datasets (e.g., increasing the number of holdings in a portfolio) within the same time window.
    3.  **Achieve better solutions (Accuracy):** Using more complex, accurate models that would be too slow on a serial processor.
    
    **Amdahl's Law Revisited:** Reminds the reader that even a 100x speedup of a major module only helps if the remaining sequential modules don't become the new bottleneck.

    ## 19.2 Algorithm Selection {#en-selection}

    Choosing the right math is as important as writing the code.

    *   **Trade-offs:** Programmers must balance lower algorithmic complexity (work efficiency) with high degrees of parallel execution.
    *   **Examples from the Book:**
        *   **Scan (Ch 11):** Kogge-Stone (more work but fewer steps) vs. Brent-Kung (less work but more steps).
        *   **Sorting (Ch 13):** Radix Sort (fast but limited to specific keys) vs. Merge Sort (general but higher complexity).
        *   **Electrostatic Map (Ch 18):** Direct Summation ($O(N^2)$) vs. Cutoff Binning ($O(N)$).
    *   **The Lesson:** The "best" algorithm depends on the hardware's specific characteristics and the data size.

    ## 19.3 Problem Decomposition {#en-decomposition}

    How you break a problem into sub-problems dictates your performance:

    *   **Output-Centric (Gather):** Threads are assigned to output elements. This is usually preferred for GPUs (as seen in MRI and Matrix Multiplication) because it avoids **Atomic Operations**.
    *   **Input-Centric (Scatter):** Threads are assigned to input elements. This is necessary for patterns like **Histograms** (Ch 9) where inputs are massive but output bins are few.
    *   **Load Balance:** Decompositions must ensure that work is distributed evenly to avoid idling SMs.

    ## 19.4 Computational Thinking {#en-thinking}

    The authors define this as the art of formulating domain problems into computational steps. They categorize the approach to "computation-hungry" applications into three levels:

    1.  **The "Good" Approach:** Accelerating legacy code using libraries (cuBLAS, cuFFT) or directives (OpenACC). High reward for low effort, but doesn't reach full potential.
    2.  **The "Better" Approach:** Rewriting existing code for new architectures. Requires both domain knowledge and computer science skills.
    3.  **The "Best" Approach:** A holistic attempt to rethink the numerical methods entirely (e.g., moving from Direct Summation to Cutoff Binning). This interdisciplinary approach leads to the biggest performance breakthroughs.

    ## 19.5 Summary {#en-summary}

    *   High-performance programming is a **thought process**, not a "black art."
    *   Successful programmers must understand **Computer Architecture** (memory/latency), **Programming Interfaces** (synchronization), and **Domain Knowledge** (the actual math of the problem).

    ---

    **Key Takeaway:** Chapter 19 teaches that the "magic" happens when you stop just "porting" code and start **rethinking the problem** to fit the throughput-oriented nature of the GPU. It emphasizes the "best" approach: challenging established numerical methods to unlock massive speedups.

=== "Tiếng Việt"

    Chương này đóng vai trò là một bản tóm tắt cấp cao về triết lý của cuốn sách. Nó không đi sâu vào mã nguồn cụ thể mà tập trung vào các khung tư duy cần thiết để giải quyết các vấn đề phức tạp bằng cách sử dụng tính song song khổng lồ.

    ## 19.1 Mục tiêu của tính toán song song {#vi-goals}

    Các tác giả xác định ba lý do chính để theo đuổi lập trình song song:

    1.  **Giải quyết vấn đề trong thời gian ngắn hơn (Tốc độ):** Đáp ứng các thời hạn thực tế nghiêm ngặt (ví dụ: hoàn thành phân tích rủi ro tài chính trong 4 giờ thay vì 200).
    2.  **Giải quyết các vấn đề lớn hơn (Quy mô):** Xử lý các tập dữ liệu lớn hơn (ví dụ: tăng số lượng nắm giữ trong một danh mục đầu tư) trong cùng một khoảng thời gian.
    3.  **Đạt được các giải pháp tốt hơn (Độ chính xác):** Sử dụng các mô hình phức tạp hơn, chính xác hơn mà nếu chạy trên bộ xử lý tuần tự sẽ quá chậm.
    
    **Xem lại Định luật Amdahl:** Nhắc nhở người đọc rằng ngay cả khi tăng tốc 100 lần cho một mô-đun chính cũng chỉ có ích nếu các mô-đun tuần tự còn lại không trở thành nút thắt cổ chai mới.

    ## 19.2 Lựa chọn thuật toán {#vi-selection}

    Lựa chọn phương pháp toán học đúng cũng quan trọng như việc viết mã.

    *   **Đánh đổi:** Lập trình viên phải cân bằng giữa độ phức tạp thuật toán thấp (hiệu quả công việc) với mức độ thực thi song song cao.
    *   **Ví dụ từ cuốn sách:**
        *   **Scan (Chương 11):** Kogge-Stone (nhiều việc hơn nhưng ít bước hơn) so với Brent-Kung (ít việc hơn nhưng nhiều bước hơn).
        *   **Sắp xếp (Chương 13):** Radix Sort (nhanh nhưng giới hạn ở một số loại khóa cụ thể) so với Merge Sort (tổng quát nhưng độ phức tạp cao hơn).
        *   **Bản đồ tĩnh điện (Chương 18):** Direct Summation ($O(N^2)$) so với Cutoff Binning ($O(N)$).
    *   **Bài học:** Thuật toán "tốt nhất" phụ thuộc vào đặc điểm cụ thể của phần cứng và kích thước dữ liệu.

    ## 19.3 Phân rã vấn đề {#vi-decomposition}

    Cách bạn chia nhỏ một vấn đề thành các vấn đề nhỏ hơn sẽ quyết định hiệu suất của bạn:

    *   **Lấy đầu ra làm trung tâm (Gather):** Các luồng được gán cho các phần tử đầu ra. Điều này thường được ưu tiên cho GPU (như đã thấy trong MRI và Nhân ma trận) vì nó tránh được các **Atomic Operations**.
    *   **Lấy đầu vào làm trung tâm (Scatter):** Các luồng được gán cho các phần tử đầu vào. Điều này cần thiết cho các mẫu như **Histogram** (Chương 9) nơi đầu vào khổng lồ nhưng các thùng (bins) đầu ra lại ít.
    *   **Cân bằng tải:** Việc phân rã phải đảm bảo công việc được phân phối đồng đều để tránh các SM bị nhàn rỗi.

    ## 19.4 Tư duy tính toán (Computational Thinking) {#vi-thinking}

    Các tác giả định nghĩa đây là nghệ thuật xây dựng các bài toán chuyên môn thành các bước tính toán. Họ phân loại cách tiếp cận các ứng dụng "đói tính toán" thành ba cấp độ:

    1.  **Cách tiếp cận "Tốt":** Tăng tốc mã nguồn cũ bằng cách sử dụng các thư viện (cuBLAS, cuFFT) hoặc các chỉ thị (OpenACC). Phần thưởng cao cho nỗ lực thấp, nhưng không đạt được hết tiềm năng.
    2.  **Cách tiếp cận "Tốt hơn":** Viết lại mã hiện có cho các kiến trúc mới. Đòi hỏi cả kiến thức chuyên môn và kỹ năng khoa học máy tính.
    3.  **Cách tiếp cận "Tốt nhất":** Một nỗ lực toàn diện để suy nghĩ lại hoàn toàn về các phương pháp số (ví dụ: chuyển từ Direct Summation sang Cutoff Binning). Cách tiếp cận liên ngành này mang lại những đột phá lớn nhất về hiệu suất.

    ## 19.5 Tóm tắt {#vi-summary}

    *   Lập trình hiệu suất cao là một **quá trình tư duy**, không phải là một "ma thuật đen".
    *   Lập trình viên thành công phải hiểu về **Kiến trúc máy tính** (bộ nhớ/độ trễ), **Giao diện lập trình** (đồng bộ hóa) và **Kiến thức chuyên môn** (toán học thực tế của vấn đề).

    ---

    **Điểm chính:** Chương 19 dạy rằng "điều kỳ diệu" xảy ra khi bạn ngừng việc chỉ "chuyển đổi" mã và bắt đầu **suy nghĩ lại về vấn đề** để phù hợp với bản chất hướng tới thông lượng của GPU. Nó nhấn mạnh cách tiếp cận "tốt nhất": thách thức các phương pháp số đã được thiết lập để mở khóa khả năng tăng tốc khổng lồ.
