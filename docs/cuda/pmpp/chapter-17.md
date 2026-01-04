# Chapter 17: MRI Reconstruction

=== "English"

    Magnetic Resonance Imaging (MRI) is a vital medical diagnostic tool. This chapter uses MRI reconstruction to demonstrate how to optimize kernels that involve complex mathematical formulas and high memory bandwidth requirements.

    ## 17.1 Background {#en-background}

    *   **MRI Process:** Consists of two phases: **Acquisition** (scanning) and **Reconstruction** (creating the image).
    *   **K-Space:** Data is sampled in the frequency domain (k-space).
    *   **Cartesian vs. Non-Cartesian:**
        *   **Cartesian scans** are on a uniform grid and can be solved quickly using Fast Fourier Transforms (FFT).
        *   **Non-Cartesian scans** (e.g., spirals) are better for imaging moving organs or patients but are much harder to solve. They require **Iterative Reconstruction**.
    *   **The Bottleneck:** On a high-end sequential CPU, a single 3D reconstruction can take **3 hours**, which is too slow for clinical use.

    ## 17.2 Iterative Reconstruction {#en-iterative}

    *   **Mathematical Model:** Uses a linear solver approach to estimate voxel values ($\rho$) from irregular samples.
    *   **Problem Scale:** Even a modest $128^3$ voxel reconstruction involves millions of calculations.
    *   **Objective:** Reduce reconstruction time from hours to **minutes** using the GPU.

    ## 17.3 Computing $F^H D$ (Step-by-Step Optimization) {#en-optimization}

    The core of the chapter involves optimizing the most expensive part of the solver, the calculation of the $F^H D$ vector.

    ### Step 1: Parallelism Structure (Scatter vs. Gather)
    *   **Scatter Approach:** Each thread takes one input (k-space sample) and updates all output voxels. This requires heavy use of **Atomic Operations**, making it very slow.
    *   **Gather Approach (Preferred):** Each thread is assigned to one output voxel and "gathers" the contributions from all input samples. This eliminates the need for atomics and is much faster.
    *   **Loop Fission:** To enable the gather approach, the authors use "loop fission" to split the calculation into two separate kernels, ensuring data is ready when the threads need to gather it.

    ### Step 2: Managing Memory Bandwidth
    *   **Register Usage:** In the original loop, the thread repeatedly reads voxel coordinates $(x, y, z)$ from global memory.
    *   **The Fix:** Load these coordinates into **Registers** once before the loop starts. This increases the compute-to-memory ratio from **0.23 to 0.46 OP/B**.

    ### Step 3: Hardware Trigonometry (SFUs)
    *   **Trigonometry Bottleneck:** The math requires constant `sin()` and `cos()` calls.
    *   **The Fix:** Use **Intrinsic Functions** (`__sin()`, `__cos()`). These are executed by the GPU's **Special Function Units (SFU)**.
    *   **Trade-off:** These are much faster but slightly less accurate. The authors use **PSNR** (Peak Signal-to-Noise Ratio) to prove the accuracy loss is negligible for medical diagnosis.

    ### Step 4: Constant Memory & Cache Efficiency
    *   **Chunking:** K-space data is too large for constant memory. The code breaks data into 64KB "chunks" and transfers them one by one.
    *   **AoS (Array of Structures):** Storing $k_x, k_y, k_z$ in three separate arrays is inefficient for the constant cache. By using an **Array of Structures**, all three values fit into a single cache line, drastically reducing DRAM requests.

    ## 17.4 Summary {#en-summary}

    *   **Performance Gain:** The final optimized version is roughly **10x faster** than the basic GPU version and orders of magnitude faster than the CPU.
    *   **Clinical Impact:** By reducing reconstruction time to approximately one minute, advanced non-Cartesian MRI becomes a viable tool for doctors to use in real-time.
    *   **Lesson:** Successful optimization requires understanding the math (Gather vs. Scatter) and the hardware (SFUs and Constant Cache).

    ---

    **Key Takeaway:** Chapter 17 teaches that "Porting" code isn't enough. You must **reformulate** the algorithm (using Loop Fission and the Gather approach) to match GPU hardware strengths like the Special Function Units and Constant Cache.

=== "Tiếng Việt"

    Chụp cộng hưởng từ (MRI) là một công cụ chẩn đoán y tế quan trọng. Chương này sử dụng quá trình tái tạo hình ảnh MRI để minh họa cách tối ưu hóa các kernel liên quan đến các công thức toán học phức tạp và yêu cầu băng thông bộ nhớ cao.

    ## 17.1 Bối cảnh {#vi-background}

    *   **Quy trình MRI:** Bao gồm hai giai đoạn: **Thu nhận (Acquisition)** (quét) và **Tái tạo (Reconstruction)** (tạo ra hình ảnh).
    *   **K-Space:** Dữ liệu được lấy mẫu trong miền tần số (k-space).
    *   **Cartesian vs. Non-Cartesian:**
        *   **Quét Cartesian** nằm trên một lưới đồng nhất và có thể được giải nhanh chóng bằng phép biến đổi Fourier nhanh (FFT).
        *   **Quét Non-Cartesian** (ví dụ: xoắn ốc) tốt hơn để chụp các cơ quan đang chuyển động hoặc bệnh nhân nhưng khó giải hơn nhiều. Chúng yêu cầu **Tái tạo lặp (Iterative Reconstruction)**.
    *   **Nút thắt cổ chai:** Trên một CPU tuần tự cao cấp, một lần tái tạo 3D duy nhất có thể mất **3 giờ**, hiệu suất này quá chậm để sử dụng trong lâm sàng.

    ## 17.2 Tái tạo lặp {#vi-iterative}

    *   **Mô hình toán học:** Sử dụng cách tiếp cận bộ giải tuyến tính để ước tính giá trị voxel ($\rho$) từ các mẫu không đều.
    *   **Quy mô vấn đề:** Ngay cả một bản tái tạo voxel $128^3$ khiêm tốn cũng liên quan đến hàng triệu phép tính.
    *   **Mục tiêu:** Giảm thời gian tái tạo từ hàng giờ xuống còn **vài phút** bằng cách sử dụng GPU.

    ## 17.3 Tính toán $F^H D$ (Tối ưu hóa từng bước) {#vi-optimization}

    Trọng tâm của chương liên quan đến việc tối ưu hóa phần tốn kém nhất của bộ giải, phép tính vector $F^H D$.

    ### Bước 1: Cấu trúc song song (Scatter vs. Gather)
    *   **Cách tiếp cận Scatter (Phân tán):** Mỗi luồng lấy một đầu vào (mẫu k-space) và cập nhật tất cả các voxel đầu ra. Điều này đòi hỏi sử dụng nhiều **Atomic Operations**, khiến nó rất chậm.
    *   **Cách tiếp cận Gather (Tập hợp - Được ưu tiên):** Mỗi luồng được gán cho một voxel đầu ra và "tập hợp" các đóng góp từ tất cả các mẫu đầu vào. Điều này loại bỏ nhu cầu về atomic và nhanh hơn nhiều.
    *   **Loop Fission (Phân tách vòng lặp):** Để kích hoạt cách tiếp cận Gather, các tác giả sử dụng "loop fission" để chia phép tính thành hai kernel riêng biệt, đảm bảo dữ liệu sẵn sàng khi các luồng cần tập hợp nó.

    ### Bước 2: Quản lý băng thông bộ nhớ
    *   **Sử dụng Register:** Trong vòng lặp ban đầu, luồng đọc đi đọc lại các tọa độ voxel $(x, y, z)$ từ bộ nhớ global.
    *   **Giải pháp:** Tải các tọa độ này vào **Registers** một lần trước khi vòng lặp bắt đầu. Điều này làm tăng tỷ lệ tính toán trên bộ nhớ từ **0.23 lên 0.46 OP/B**.

    ### Bước 3: Lượng giác phần cứng (SFUs)
    *   **Nút thắt lượng giác:** Các phép toán yêu cầu các lệnh gọi `sin()` và `cos()` liên tục.
    *   **Giải pháp:** Sử dụng các **Hàm nội tại (Intrinsic Functions)** (`__sin()`, `__cos()`). Các hàm này được thực thi bởi các **Đơn vị chức năng đặc biệt (SFU)** của GPU.
    *   **Đánh đổi:** Các hàm này nhanh hơn nhiều nhưng độ chính xác thấp hơn một chút. Các tác giả sử dụng **PSNR** (Peak Signal-to-Noise Ratio) để chứng minh tổn thất độ chính xác là không đáng kể đối với chẩn đoán y tế.

    ### Bước 4: Constant Memory & Hiệu quả Cache
    *   **Chia nhỏ (Chunking):** Dữ liệu k-space quá lớn đối với bộ nhớ constant. Mã nguồn chia dữ liệu thành các "khối" 64KB và chuyển chúng từng cái một.
    *   **AoS (Array of Structures):** Lưu trữ $k_x, k_y, k_z$ trong ba mảng riêng biệt là không hiệu quả cho bộ nhớ cache constant. Bằng cách sử dụng **Mảng các cấu trúc**, cả ba giá trị nằm gọn trong một dòng cache duy nhất, giảm đáng kể các yêu cầu DRAM.

    ## 17.4 Tóm tắt {#vi-summary}

    *   **Cải thiện hiệu suất:** Phiên bản tối ưu hóa cuối cùng nhanh hơn khoảng **10 lần** so với phiên bản GPU cơ bản và nhanh hơn nhiều bậc so với CPU.
    *   **Tác động lâm sàng:** Bằng cách giảm thời gian tái tạo xuống còn khoảng một phút, MRI non-Cartesian nâng cao trở thành một công cụ khả thi để các bác sĩ sử dụng trong thời gian thực.
    *   **Bài học:** Tối ưu hóa thành công đòi hỏi sự hiểu biết về toán học (Gather vs. Scatter) và phần cứng (SFUs và Constant Cache).

    ---

    **Điểm chính:** Chương 17 dạy rằng việc "chuyển đổi" mã nguồn là không đủ. Bạn phải **xây dựng lại** thuật toán (sử dụng Loop Fission và cách tiếp cận Gather) để phù hợp với thế mạnh phần cứng của GPU như các Đơn vị chức năng đặc biệt và Constant Cache.
