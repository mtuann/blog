# Chapter 3: Multidimensional Grids and Data

=== "English"

    This chapter expands on the CUDA programming model by moving from simple 1D vectors to multidimensional data structures (2D images and matrices) and explaining how threads are organized to process them.

    ## 3.1 Multidimensional Grid Organization {#en-grid-org}

    **Grid and Block Hierarchy:** Threads are organized into a two-level hierarchy (Grid $\rightarrow$ Block). Both can be defined in **1D, 2D, or 3D**.
    
    **Key Built-in Variables:**
    
    *   `gridDim`: The dimensions of the grid (number of blocks).
    *   `blockDim`: The dimensions of each block (number of threads).
    *   `blockIdx`: The coordinates of a block within the grid.
    *   `threadIdx`: The coordinates of a thread within its block.
    
    **Dimensionality Limits:** While threads can be 3D, the total number of threads in a single block cannot exceed **1024**.
    
    **Type `dim3`:** CUDA uses a special integer vector type `dim3` to specify these dimensions. For example:
    
    ```c
    dim3 grid(32, 1, 1);
    dim3 block(128, 1, 1);
    ```

    ## 3.2 Mapping Threads to Multidimensional Data {#en-mapping}

    **Concept:** To process a 2D image, it is most intuitive to use a 2D grid of 2D blocks.
    
    **Mapping Formula (2D):** To find the specific row and column a thread should work on:
    
    ```c
    row = blockIdx.y * blockDim.y + threadIdx.y;
    col = blockIdx.x * blockDim.x + threadIdx.x;
    ```
    
    **Memory Linearization (Row-Major Order):**
    
    *   In C and CUDA, multidimensional arrays are stored in a "flat" 1D memory space.
    *   **Row-Major Layout:** Elements of a row are placed in consecutive locations.
    *   **The Formula:** To access a 2D element at `(row, col)` in a 1D array of a certain `Width`:
        ```c
        index = row * Width + col;
        ```
    
    **Boundary Checks:** If the data size (e.g., a 62x76 image) is not a perfect multiple of the block size (e.g., 16x16), some threads will be "out of bounds." The kernel must use `if` statements to ensure these threads do not access invalid memory.

    ## 3.3 Image Blur: A More Complex Kernel {#en-blur}

    **Beyond Independence:** Unlike vector addition where each thread is totally isolated, image blurring requires a thread to access its neighbors.
    
    **The Process:** A blurred pixel is the average value of an $N \times N$ patch of pixels surrounding the target.
    
    **Inner Loops:** The kernel uses nested `for` loops to iterate through the neighborhood patch.
    
    **Ghost Cells/Edges:** The kernel includes logic to handle pixels at the edge of the image where a full $N \times N$ patch doesn't exist (using 0 or the nearest pixel as a filler).

    ## 3.4 Matrix Multiplication {#en-matmul}

    **The Pattern:** This is a core application of multidimensional mapping.
    
    **Algorithm:** To compute one element of the resulting matrix $P$, a thread must perform a dot product of a row from matrix $M$ and a column from matrix $N$.
    
    **Kernel Structure:**
    
    *   Each thread is assigned to one element of the output matrix $P$.
    *   The thread uses a loop to multiply and sum elements:
        ```c
        Pvalue += M[row * Width + k] * N[k * Width + col];
        ```
    
    **Efficiency Warning:** The book notes that this "simple" matrix multiplication is limited by global memory bandwidth (it is "memory-bound"). This sets the stage for the optimization techniques (like tiling) introduced in later chapters.

    ## 3.5 Summary of Skills {#en-summary}

    *   Understanding how to use `blockIdx` and `threadIdx` in 2D/3D.
    *   Mapping multidimensional data to the "flat" row-major memory of the GPU.
    *   Implementing kernels where threads must iterate over data subsets (like patches or matrix rows).

    ---

    **Key Takeaway:** Chapter 3 teaches the "arithmetic of mapping." The most critical skill here is learning how to calculate a 1D memory index from 2D or 3D thread coordinates so that thousands of threads can navigate complex data structures without crashing or overlapping.

=== "Tiếng Việt"

    Chương này mở rộng mô hình lập trình CUDA bằng cách chuyển từ vector 1D đơn giản sang cấu trúc dữ liệu đa chiều (ảnh 2D và ma trận) và giải thích cách tổ chức luồng để xử lý chúng.

    ## 3.1 Tổ chức Grid đa chiều {#vi-grid-org}

    **Phân cấp Grid và Block:** Các luồng được tổ chức thành phân cấp hai cấp (Grid $\rightarrow$ Block). Cả hai có thể được định nghĩa trong **1D, 2D, hoặc 3D**.
    
    **Các biến dựng sẵn chính:**
    
    *   `gridDim`: Kích thước của grid (số lượng block).
    *   `blockDim`: Kích thước của mỗi block (số lượng luồng).
    *   `blockIdx`: Tọa độ của block trong grid.
    *   `threadIdx`: Tọa độ của luồng trong block của nó.
    
    **Giới hạn chiều:** Mặc dù luồng có thể là 3D, tổng số luồng trong một block không được vượt quá **1024**.
    
    **Kiểu `dim3`:** CUDA sử dụng kiểu vector số nguyên đặc biệt `dim3` để chỉ định các chiều này. Ví dụ:
    
    ```c
    dim3 grid(32, 1, 1);
    dim3 block(128, 1, 1);
    ```

    ## 3.2 Ánh xạ luồng đến dữ liệu đa chiều {#vi-mapping}

    **Khái niệm:** Để xử lý ảnh 2D, trực quan nhất là sử dụng grid 2D của các block 2D.
    
    **Công thức ánh xạ (2D):** Để tìm hàng và cột cụ thể mà luồng nên làm việc:
    
    ```c
    row = blockIdx.y * blockDim.y + threadIdx.y;
    col = blockIdx.x * blockDim.x + threadIdx.x;
    ```
    
    **Tuyến tính hóa bộ nhớ (Thứ tự hàng-chính):**
    
    *   Trong C và CUDA, mảng đa chiều được lưu trữ trong không gian bộ nhớ 1D "phẳng".
    *   **Bố cục hàng-chính:** Các phần tử của một hàng được đặt ở các vị trí liên tiếp.
    *   **Công thức:** Để truy cập phần tử 2D tại `(row, col)` trong mảng 1D có `Width` nhất định:
        ```c
        index = row * Width + col;
        ```
    
    **Kiểm tra biên:** Nếu kích thước dữ liệu (ví dụ: ảnh 62x76) không phải là bội số hoàn hảo của kích thước block (ví dụ: 16x16), một số luồng sẽ "ngoài giới hạn". Kernel phải sử dụng câu lệnh `if` để đảm bảo các luồng này không truy cập bộ nhớ không hợp lệ.

    ## 3.3 Làm mờ ảnh: Kernel phức tạp hơn {#vi-blur}

    **Vượt ra ngoài tính độc lập:** Không giống như phép cộng vector nơi mỗi luồng hoàn toàn độc lập, làm mờ ảnh yêu cầu luồng truy cập các pixel lân cận.
    
    **Quy trình:** Một pixel mờ là giá trị trung bình của vùng $N \times N$ pixel xung quanh mục tiêu.
    
    **Vòng lặp bên trong:** Kernel sử dụng vòng lặp lồng nhau để lặp qua vùng lân cận.
    
    **Ô ma/Cạnh:** Kernel bao gồm logic để xử lý các pixel ở cạnh ảnh nơi không tồn tại vùng $N \times N$ đầy đủ (sử dụng 0 hoặc pixel gần nhất làm giá trị điền).

    ## 3.4 Nhân ma trận {#vi-matmul}

    **Mẫu:** Đây là ứng dụng cốt lõi của ánh xạ đa chiều.
    
    **Thuật toán:** Để tính một phần tử của ma trận kết quả $P$, luồng phải thực hiện tích vô hướng của một hàng từ ma trận $M$ và một cột từ ma trận $N$.
    
    **Cấu trúc Kernel:**
    
    *   Mỗi luồng được gán cho một phần tử của ma trận đầu ra $P$.
    *   Luồng sử dụng vòng lặp để nhân và cộng các phần tử:
        ```c
        Pvalue += M[row * Width + k] * N[k * Width + col];
        ```
    
    **Cảnh báo hiệu quả:** Cuốn sách lưu ý rằng phép nhân ma trận "đơn giản" này bị giới hạn bởi băng thông bộ nhớ global (nó là "memory-bound"). Điều này đặt nền tảng cho các kỹ thuật tối ưu hóa (như tiling) được giới thiệu trong các chương sau.

    ## 3.5 Tóm tắt kỹ năng {#vi-summary}

    *   Hiểu cách sử dụng `blockIdx` và `threadIdx` trong 2D/3D.
    *   Ánh xạ dữ liệu đa chiều đến bộ nhớ "phẳng" theo thứ tự hàng-chính của GPU.
    *   Triển khai kernel nơi các luồng phải lặp qua các tập con dữ liệu (như vùng hoặc hàng ma trận).

    ---

    **Điểm chính:** Chương 3 dạy "số học ánh xạ". Kỹ năng quan trọng nhất ở đây là học cách tính chỉ số bộ nhớ 1D từ tọa độ luồng 2D hoặc 3D để hàng nghìn luồng có thể điều hướng các cấu trúc dữ liệu phức tạp mà không bị lỗi hoặc chồng chéo.
