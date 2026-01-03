# Chapter 1: Introduction

=== "English"

    ## 1.1 The GPU Revolution {#en-revolution}
    The shift from multicore (latency-oriented) CPU computing to many-thread (throughput-oriented) GPU computing marks a "concurrency revolution."
    
    *   **CPU**: Optimized for sequential logic and low latency (few complex cores).
    *   **GPU**: Optimized for massive data parallelism and high throughput (thousands of simple cores).

    ## 1.2 The Performance Gap {#en-gap}
    *   **TFLOPS (Tera Floating-Point Operations Per Second)**: 
        *   GPUs significantly outperform CPUs in raw calculation power, especially in **FP32** (Single Precision) and **FP16** (Half Precision).
        *   **AI Needs**: AI models thrive on matrix multiplications, which require massive batch processing rather than complex control logic.

    ## 1.3 Amdahl's Law & Speedup {#en-amdahl}
    *   **Speedup** = Sequential Time / Parallel Time.
    *   The total speedup is limited by the sequential portion of the program. To achieve a 100x speedup, more than 99.9% of the work must be parallelized.

    ## 1.4 Challenges of Parallel Programming {#en-challenges}
    *   **Algorithm Complexity**: Some parallel algorithms do more work than sequential ones.
    *   **Data Characteristics**: Regular data is easy to parallelize; erratic data causes load imbalance.
    *   **Synchronization**: Barriers and atomic operations introduce overhead.

=== "Tiếng Việt"

    ## 1.1 Cuộc cách mạng GPU {#vi-revolution}
    Sự chuyển dịch từ tính toán CPU đa lõi (hướng tới độ trễ) sang tính toán GPU hàng nghìn luồng (hướng tới thông lượng) đánh dấu một "cuộc cách mạng đồng thời."

    *   **CPU**: Tối ưu cho logic tuần tự và độ trễ thấp (ít lõi nhưng phức tạp).
    *   **GPU**: Tối ưu cho song song dữ liệu khổng lồ và thông lượng cao (hàng nghìn lõi đơn giản).

    ## 1.2 Khoảng cách hiệu năng {#vi-gap}
    *   **TFLOPS (Tera Floating-Point Operations Per Second)**: 
        *   GPU vượt xa CPU về sức mạnh tính toán thô, đặc biệt là ở định dạng **FP32** (độ chính xác đơn) và **FP16** (độ chính xác nửa).
        *   **Nhu cầu của AI**: Các mô hình AI phát triển dựa trên phép nhân ma trận, đòi hỏi xử lý hàng loạt thay vì các logic điều khiển phức tạp.

    ## 1.3 Định luật Amdahl & Gia tốc (Speedup) {#vi-amdahl}
    *   **Speedup** = Thời gian tuần tự / Thời gian song song.
    *   Tổng tốc độ tăng trưởng bị giới hạn bởi phần tuần tự của chương trình. Để đạt được tốc độ tăng 100 lần, hơn 99,9% công việc phải được song song hóa.

    ## 1.4 Thách thức của lập trình song song {#vi-challenges}
    *   **Độ phức tạp thuật toán**: Một số thuật toán song song thực hiện nhiều công việc hơn bản tuần tự.
    *   **Đặc tính dữ liệu**: Dữ liệu đều đặn dễ song song hóa; dữ liệu bất thường gây mất cân bằng tải.
    *   **Đồng bộ hóa**: Barrier và các thao tác nguyên tử (atomic) gây ra chi phí quản lý (overhead).

    ---

    > **Key Concept**: CPU is good at "thinking" (logic), GPU is good at "calculating" (math). AI needs massive math.
