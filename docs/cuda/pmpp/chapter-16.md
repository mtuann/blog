# Chapter 16: Deep Learning

=== "English"

    This chapter acts as a major application case study, showing how the parallel patterns learned in previous chapters (specifically convolution and matrix multiplication) form the backbone of modern Artificial Intelligence.

    ## 16.1 Background {#en-background}

    **Machine Learning Definition:** A field of study where computers learn logic from data rather than being explicitly programmed.
    
    **The Perceptron:** The simplest linear classifier ($y = \text{sign}(W \cdot x + b)$). It uses weights ($W$) and a bias ($b$) to categorize data.
    
    **Activation Functions:** Functions like **Sigmoid** or **ReLU** (Rectified Linear Unit) that introduce nonlinearity, allowing the network to learn complex patterns.
    
    **Multilayer Perceptrons (MLP):** Stacking layers of neurons where the output of one layer is the input to the next.
    
    **Fully Connected (FC) Layers:** A layer where every input is connected to every output. Computationally, this is a **Matrix-Vector Multiplication**.
    
    **Training and Backpropagation:**
    
    *   **Loss/Error Function:** Measures the difference between the network's guess and the correct label.
    *   **Stochastic Gradient Descent (SGD):** The process of iteratively updating weights to minimize error.
    *   **Chain Rule:** Used in **Backpropagation** to calculate how much each weight contributed to the final error.

    ## 16.2 Convolutional Neural Networks (CNN) {#en-cnn}

    **Why CNNs?:** Fully connected layers are too expensive for high-resolution images. CNNs reduce cost by using **Convolutional Layers** that look at small patches of an image.
    
    **Structure:** Typically consists of Convolutional layers (feature extraction), Pooling/Subsampling layers (size reduction), and FC layers (final classification).
    
    **Feature Maps:** The input and output "images" of each layer.
    
    **3D Filter Banks:** In deep learning, convolution is 3D; a filter bank ($W$) is applied across multiple input channels ($C$) to produce an output feature map.

    ## 16.3 Convolutional Layer: A CUDA Inference Kernel {#en-inference}

    **Parallelism Levels:** CNNs offer massive parallelism across:
    
    1.  **Samples ($N$):** Different images in a minibatch.
    2.  **Feature Maps ($M$):** Different filters applied to the same image.
    3.  **Pixels ($h, w$):** Different locations in the output image.
    
    **Thread Mapping:** Assigning 2D thread blocks to output pixels and using the 3D grid dimensions to handle different feature maps and minibatch samples.

    ## 16.4 Formulating a Convolutional Layer as GEMM {#en-gemm}

    **The Problem:** Writing a custom kernel for every possible filter size is difficult and often less efficient than standard math libraries.
    
    **The Solution (im2col):** Unrolling and duplicating the input feature map pixels into a large matrix ($X_{\text{unrolled}}$).
    
    **Mechanism:** By rearranging the data, a 3D convolution can be performed as a single, massive **GEMM (General Matrix Multiply)** operation.
    
    **Trade-off:** This uses significantly more memory (due to pixel duplication) but allows the GPU to use highly optimized libraries like **cuBLAS**, which achieve near-peak hardware performance.

    ## 16.5 cuDNN Library {#en-cudnn}

    **Overview:** NVIDIA's library of highly optimized routines for deep learning.
    
    **Features:** It handles the complexity of "lazy" memory management (generating unrolled matrices on the fly in on-chip memory) to avoid the memory waste described in the im2col approach.
    
    **Utility:** Most frameworks (PyTorch, TensorFlow) use cuDNN under the hood to ensure maximum performance without requiring engineers to write their own CUDA kernels.

    ---

    **Key Takeaway:** Chapter 16 bridges theory and practice. It shows that while the "math" of AI involves complex neural structures, the "execution" on a GPU relies on transforming these structures into **Matrix Multiplications** and **Tiled Convolutions**, utilizing the exact performance optimizations (coalescing, tiling, and latency hiding) taught in Part I.

=== "Tiếng Việt"

    Chương này đóng vai trò như một nghiên cứu điển hình về ứng dụng quan trọng, chỉ ra cách các mẫu song song đã học ở các chương trước (cụ thể là phép tích chập và nhân ma trận) tạo nên khung xương cho Trí tuệ Nhân tạo hiện đại.

    ## 16.1 Bối cảnh {#vi-background}

    **Định nghĩa Học máy:** Một lĩnh vực nghiên cứu nơi máy tính học logic từ dữ liệu thay vì được lập trình một cách rõ ràng.
    
    **Perceptron:** Bộ phân loại tuyến tính đơn giản nhất ($y = \text{sign}(W \cdot x + b)$). Nó sử dụng các trọng số ($W$) và một độ lệch (bias - $b$) để phân loại dữ liệu.
    
    **Hàm kích hoạt:** Các hàm như **Sigmoid** hoặc **ReLU** (Rectified Linear Unit) giúp đưa tính phi tuyến tính vào, cho phép mạng học các mẫu phức tạp.
    
    **Multilayer Perceptrons (MLP):** Việc xếp chồng các lớp nơ-ron nơi đầu ra của lớp này là đầu vào của lớp tiếp theo.
    
    **Lớp kết nối đầy đủ (Fully Connected - FC):** Một lớp mà mọi đầu vào đều được kết nối với mọi đầu ra. Về mặt tính toán, đây là một phép **Nhân Ma trận - Vector**.
    
    **Huấn luyện và Lan truyền ngược (Backpropagation):**
    
    *   **Hàm mất mát/sai số (Loss/Error Function):** Đo lường sự khác biệt giữa dự đoán của mạng và nhãn chính xác.
    *   **Stochastic Gradient Descent (SGD):** Quá trình cập nhật các trọng số theo cách lặp lại để giảm thiểu sai số.
    *   **Quy tắc chuỗi (Chain Rule):** Được sử dụng trong **Lan truyền ngược** để tính toán xem mỗi trọng số đã đóng góp bao nhiêu vào sai số cuối cùng.

    ## 16.2 Mạng nơ-ron tích chập (CNN) {#vi-cnn}

    **Tại sao lại là CNN?:** Các lớp kết nối đầy đủ quá tốn kém đối với các hình ảnh có độ phân giải cao. CNN giảm chi phí bằng cách sử dụng các **Lớp tích chập** quét qua các vùng nhỏ của hình ảnh.
    
    **Cấu trúc:** Thường bao gồm các lớp Tích chập (trích xuất đặc trưng), các lớp Pooling/Subsampling (giảm kích thước), và các lớp FC (phân loại cuối cùng).
    
    **Bản đồ đặc trưng (Feature Maps):** "Hình ảnh" đầu vào và đầu ra của mỗi lớp.
    
    **Bộ lọc 3D (3D Filter Banks):** Trong học sâu, phép tích chập là 3D; một bộ lọc ($W$) được áp dụng trên nhiều kênh đầu vào ($C$) để tạo ra một bản đồ đặc trưng đầu ra.

    ## 16.3 Lớp tích chập: Một Kernel suy luận CUDA {#vi-inference}

    **Các cấp độ song song:** CNN cung cấp khả năng song song hóa khổng lồ trên:
    
    1.  **Mẫu ($N$):** Các hình ảnh khác nhau trong một minibatch.
    2.  **Bản đồ đặc trưng ($M$):** Các bộ lọc khác nhau được áp dụng cho cùng một hình ảnh.
    3.  **Pixel ($h, w$):** Các vị trí khác nhau trong hình ảnh đầu ra.
    
    **Ánh xạ luồng:** Gán các khối luồng (thread blocks) 2D cho các pixel đầu ra và sử dụng kích thước lưới (grid) 3D để xử lý các bản đồ đặc trưng và các mẫu minibatch khác nhau.

    ## 16.4 Xây dựng Lớp tích chập dưới dạng GEMM {#vi-gemm}

    **Vấn đề:** Việc viết một kernel tùy chỉnh cho mọi kích thước bộ lọc có thể là rất khó khăn và thường kém hiệu quả hơn các thư viện toán học tiêu chuẩn.
    
    **Giải pháp (im2col):** Trải phẳng và nhân bản các pixel của bản đồ đặc trưng đầu vào thành một ma trận lớn ($X_{\text{unrolled}}$).
    
    **Cơ chế:** Bằng cách sắp xếp lại dữ liệu, một phép tích chập 3D có thể được thực hiện như một phép toán **GEMM (General Matrix Multiply)** duy nhất và khổng lồ.
    
    **Đánh đổi:** Cách này sử dụng nhiều bộ nhớ hơn đáng kể (do nhân bản pixel) nhưng cho phép GPU sử dụng các thư viện tối ưu hóa cao như **cuBLAS**, đạt được hiệu suất phần cứng gần mức tối đa.

    ## 16.5 Thư viện cuDNN {#vi-cudnn}

    **Tổng quan:** Thư viện của NVIDIA chứa các quy trình được tối ưu hóa cao cho học sâu.
    
    **Tính năng:** Nó xử lý sự phức tạp của việc quản lý bộ nhớ "lazy" (tạo các ma trận trải phẳng ngay lập tức trong bộ nhớ trên chip) để tránh lãng phí bộ nhớ như mô tả trong cách tiếp cận im2col.
    
    **Tiện ích:** Hầu hết các khung (PyTorch, TensorFlow) đều sử dụng cuDNN bên dưới để đảm bảo hiệu suất tối đa mà không yêu cầu các kỹ sư phải tự viết các kernel CUDA.

    ---

    **Điểm chính:** Chương 16 kết nối lý thuyết và thực hành. Nó chỉ ra rằng mặc dù "toán học" của AI liên quan đến các cấu trúc nơ-ron phức tạp, việc "thực thi" trên GPU dựa trên việc chuyển đổi các cấu trúc này thành các phép **Nhân Ma trận** và **Tích chập Tiled**, sử dụng chính xác các tối ưu hóa hiệu suất (coalescing, tiling và che giấu độ trễ) đã được dạy ở Phần I.
