# Chapter 2: Heterogeneous Data Parallel Computing

=== "English"

    This chapter introduces the fundamental concepts of data parallelism and the basic structure of a CUDA C program using a simple "Vector Addition" example.

    ## 2.1 Data Parallelism {#en-data-parallelism}

    **Definition:** A programming phenomenon where computation is performed independently on different parts of a dataset.
    
    **Scalability:** Data parallelism is the primary source of scalability in parallel programs; as datasets grow, more threads can be used to handle the work.
    
    **Illustrative Example: Color-to-Grayscale Conversion**
    
    *   Each pixel in a color image $(r, g, b)$ is converted to a luminance value $(L)$ using the formula: 
        $$L = r \times 0.21 + g \times 0.72 + b \times 0.07$$
    *   Since the conversion of one pixel does not depend on any other pixel, this task is highly data-parallel.
    
    **Task Parallelism vs. Data Parallelism:** While task parallelism involves doing different functions at the same time, data parallelism focuses on doing the same function on many data elements simultaneously.

    ## 2.2 CUDA C Program Structure {#en-structure}

    **Heterogeneous Computing:** A CUDA C program consists of a **Host** (CPU) and one or more **Devices** (GPUs).
    
    **Kernels:** These are functions that are executed on the device in a data-parallel manner.
    
    **Execution Flow:** The program starts on the host. When a kernel is called, a large number of threads (a **Grid**) are launched on the device to execute the kernel. Once the grid finishes, control returns to the host.

    ## 2.3 A Vector Addition Kernel {#en-vector-add}

    **The Baseline:** In sequential C, vector addition uses a `for` loop to iterate through every element.
    
    **The GPU Approach:** In CUDA, the `for` loop is replaced by a grid of threads. Each thread is responsible for adding exactly one pair of elements.
    
    **Naming Conventions:** To avoid confusion, the book uses the suffix `_h` for variables residing in host memory and `_d` for those in device memory.

    ## 2.4 Device Global Memory and Data Transfer {#en-memory}

    **Global Memory:** The GPU has its own high-capacity DRAM (e.g., 16GB–80GB). The host cannot directly access this memory using standard pointers; specialized API functions are required.
    
    **Key API Functions:**
    
    *   `cudaMalloc()`: Allocates a piece of memory in the device global memory. It is modeled after the standard C `malloc()`.
    *   `cudaFree()`: Frees allocated memory on the device.
    *   `cudaMemcpy()`: Transfers data between host and device. It requires a "direction" parameter, such as `cudaMemcpyHostToDevice` or `cudaMemcpyDeviceToHost`.

    ## 2.5 Kernel Functions and Threading {#en-threading}

    **Function Declarations:**
    
    *   `__global__`: Marks a function as a kernel. It is called from the host and executed on the device. It must return `void`.
    *   `__device__`: A function called and executed only on the device.
    *   `__host__`: A traditional C function (the default).
    
    **Built-in Variables (Identifying Threads):**
    
    *   `threadIdx`: The unique coordinate of a thread within its block.
    *   `blockIdx`: The coordinate of a block within the grid.
    *   `blockDim`: The number of threads in each block.
    
    **Index Calculation:** To map a thread to a specific array element, threads calculate a unique global index:
    
    ```c
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    ```
    
    **Automatic Variables:** Variables declared inside a kernel are private to each thread (stored in registers).

    ## 2.6 Calling Kernel Functions {#en-calling}

    **Execution Configuration:** Kernels are launched using the `<<<...>>>` syntax.
    
    *   *First Parameter:* Number of blocks in the grid.
    *   *Second Parameter:* Number of threads per block.
    
    **Ceiling Division:** To ensure every data element is covered, the number of blocks is often calculated using a ceiling function: `ceil(n / 256.0)`.
    
    **Boundary Checks:** Because the number of threads launched is often a multiple of the block size, kernels must include an `if (i < n)` check to prevent threads from accessing memory outside the array bounds.

    ## 2.7 Compilation {#en-compilation}

    **NVCC:** The NVIDIA C Compiler. It separates the source file into host code (processed by standard compilers like `gcc` or `cl.exe`) and device code (compiled into PTX or binary object files for the GPU).

    ## 2.8 Summary of Keywords {#en-keywords}

    *   **Memory:** `cudaMalloc`, `cudaFree`, `cudaMemcpy`.
    *   **Declaration:** `__global__`, `__device__`, `__host__`.
    *   **Hierarchy:** Grid $\rightarrow$ Block $\rightarrow$ Thread.

    ---

    **Key Takeaway:** Chapter 2 shifts the programmer's focus from writing loops to defining a single thread's behavior and using a hierarchy of indices to map those threads to massive amounts of data.

=== "Tiếng Việt"

    Chương này giới thiệu các khái niệm cơ bản về tính song song dữ liệu và cấu trúc cơ bản của chương trình CUDA C sử dụng ví dụ đơn giản "Cộng Vector".

    ## 2.1 Tính song song dữ liệu {#vi-data-parallelism}

    **Định nghĩa:** Hiện tượng lập trình trong đó tính toán được thực hiện độc lập trên các phần khác nhau của tập dữ liệu.
    
    **Khả năng mở rộng:** Tính song song dữ liệu là nguồn chính của khả năng mở rộng trong các chương trình song song; khi tập dữ liệu tăng lên, có thể sử dụng nhiều luồng hơn để xử lý công việc.
    
    **Ví dụ minh họa: Chuyển đổi màu sang xám**
    
    *   Mỗi pixel trong ảnh màu $(r, g, b)$ được chuyển đổi thành giá trị độ sáng $(L)$ bằng công thức:
        $$L = r \times 0.21 + g \times 0.72 + b \times 0.07$$
    *   Vì việc chuyển đổi một pixel không phụ thuộc vào bất kỳ pixel nào khác, tác vụ này có tính song song dữ liệu cao.
    
    **Tính song song tác vụ vs. Tính song song dữ liệu:** Trong khi tính song song tác vụ liên quan đến việc thực hiện các hàm khác nhau cùng lúc, tính song song dữ liệu tập trung vào việc thực hiện cùng một hàm trên nhiều phần tử dữ liệu đồng thời.

    ## 2.2 Cấu trúc chương trình CUDA C {#vi-structure}

    **Tính toán không đồng nhất:** Chương trình CUDA C bao gồm **Host** (CPU) và một hoặc nhiều **Device** (GPU).
    
    **Kernel:** Đây là các hàm được thực thi trên device theo cách song song dữ liệu.
    
    **Luồng thực thi:** Chương trình bắt đầu trên host. Khi kernel được gọi, một số lượng lớn luồng (một **Grid**) được khởi chạy trên device để thực thi kernel. Khi grid kết thúc, điều khiển quay lại host.

    ## 2.3 Kernel cộng vector {#vi-vector-add}

    **Cơ sở:** Trong C tuần tự, phép cộng vector sử dụng vòng lặp `for` để lặp qua mọi phần tử.
    
    **Cách tiếp cận GPU:** Trong CUDA, vòng lặp `for` được thay thế bằng lưới các luồng. Mỗi luồng chịu trách nhiệm cộng chính xác một cặp phần tử.
    
    **Quy ước đặt tên:** Để tránh nhầm lẫn, cuốn sách sử dụng hậu tố `_h` cho các biến nằm trong bộ nhớ host và `_d` cho các biến trong bộ nhớ device.

    ## 2.4 Bộ nhớ Global của Device và Truyền dữ liệu {#vi-memory}

    **Bộ nhớ Global:** GPU có DRAM dung lượng cao riêng (ví dụ: 16GB–80GB). Host không thể truy cập trực tiếp bộ nhớ này bằng con trỏ tiêu chuẩn; cần các hàm API chuyên biệt.
    
    **Các hàm API chính:**
    
    *   `cudaMalloc()`: Cấp phát một phần bộ nhớ trong bộ nhớ global của device. Được mô hình hóa theo `malloc()` tiêu chuẩn của C.
    *   `cudaFree()`: Giải phóng bộ nhớ đã cấp phát trên device.
    *   `cudaMemcpy()`: Truyền dữ liệu giữa host và device. Yêu cầu tham số "hướng", chẳng hạn như `cudaMemcpyHostToDevice` hoặc `cudaMemcpyDeviceToHost`.

    ## 2.5 Hàm Kernel và Luồng {#vi-threading}

    **Khai báo hàm:**
    
    *   `__global__`: Đánh dấu hàm là kernel. Được gọi từ host và thực thi trên device. Phải trả về `void`.
    *   `__device__`: Hàm được gọi và thực thi chỉ trên device.
    *   `__host__`: Hàm C truyền thống (mặc định).
    
    **Biến dựng sẵn (Xác định luồng):**
    
    *   `threadIdx`: Tọa độ duy nhất của luồng trong block của nó.
    *   `blockIdx`: Tọa độ của block trong grid.
    *   `blockDim`: Số lượng luồng trong mỗi block.
    
    **Tính toán chỉ số:** Để ánh xạ luồng đến phần tử mảng cụ thể, các luồng tính toán chỉ số toàn cục duy nhất:
    
    ```c
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    ```
    
    **Biến tự động:** Các biến được khai báo bên trong kernel là riêng tư cho mỗi luồng (lưu trữ trong register).

    ## 2.6 Gọi hàm Kernel {#vi-calling}

    **Cấu hình thực thi:** Kernel được khởi chạy bằng cú pháp `<<<...>>>`.
    
    *   *Tham số đầu tiên:* Số lượng block trong grid.
    *   *Tham số thứ hai:* Số lượng luồng trên mỗi block.
    
    **Phép chia làm tròn lên:** Để đảm bảo mọi phần tử dữ liệu được bao phủ, số lượng block thường được tính bằng hàm làm tròn lên: `ceil(n / 256.0)`.
    
    **Kiểm tra biên:** Vì số lượng luồng được khởi chạy thường là bội số của kích thước block, kernel phải bao gồm kiểm tra `if (i < n)` để ngăn các luồng truy cập bộ nhớ ngoài giới hạn mảng.

    ## 2.7 Biên dịch {#vi-compilation}

    **NVCC:** Trình biên dịch NVIDIA C. Nó tách file nguồn thành code host (được xử lý bởi trình biên dịch tiêu chuẩn như `gcc` hoặc `cl.exe`) và code device (được biên dịch thành PTX hoặc file đối tượng nhị phân cho GPU).

    ## 2.8 Tóm tắt từ khóa {#vi-keywords}

    *   **Bộ nhớ:** `cudaMalloc`, `cudaFree`, `cudaMemcpy`.
    *   **Khai báo:** `__global__`, `__device__`, `__host__`.
    *   **Phân cấp:** Grid $\rightarrow$ Block $\rightarrow$ Thread.

    ---

    **Điểm chính:** Chương 2 chuyển trọng tâm của lập trình viên từ viết vòng lặp sang định nghĩa hành vi của một luồng đơn lẻ và sử dụng hệ phân cấp chỉ số để ánh xạ các luồng đó đến lượng dữ liệu lớn.
