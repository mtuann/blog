# Chapter 20: Programming a Heterogeneous Cluster

=== "English"

    This chapter marks the beginning of **Part IV: Advanced Practices**. It shifts from a single machine to **High-Performance Computing (HPC) clusters**, teaching how to combine CUDA with the **Message Passing Interface (MPI)** to scale applications across multiple nodes.

    ## 20.1 Background {#en-background}

    *   **HPC Clusters:** Modern supercomputers consist of thousands of "nodes." Each node has its own CPUs (Host) and GPUs (Devices).
    *   **The Challenge:** Nodes do not share memory. To work together on a single problem, they must "pass messages" over a network.
    *   **MPI:** The industry standard for distributed memory programming.

    ## 20.2 A Running Example: 3D Stencil {#en-stencil}

    *   **Application:** Modeling heat transfer in a 3D duct using a 25-point Jacobi iterative stencil.
    *   **Domain Partitioning:** The 3D grid is sliced along the $Z$-axis into several **Domain Partitions** (e.g., $D0, D1, D2, D3$). Each partition is assigned to a different MPI process (and therefore a different GPU).
    *   **Dependency:** Just like in Chapter 8, each slice needs data from its neighbors to calculate the next step. In a cluster, these neighbors live on different physical machines.

    ## 20.3 Message Passing Interface (MPI) Basics {#en-mpi-basics}

    *   **SPMD Model:** Like CUDA, MPI uses a "Single Program Multiple Data" approach where every node runs the exact same code but acts differently based on its ID.
    *   **MPI Rank:** Each process is assigned a unique ID called a **Rank** (analogous to a `threadIdx` for a whole machine).
    *   **Core Functions:**
        *   `MPI_Init` / `MPI_Finalize`: Start and stop the MPI environment.
        *   `MPI_Comm_rank`: Identify the current process Rank.
        *   `MPI_Comm_size`: Find the total number of processes in the cluster.

    ## 20.4 Point-to-Point Communication {#en-communication}

    *   **Send/Recv:** Uses `MPI_Send` and `MPI_Recv` to move data between specific nodes.
    *   **The Data Server:** The authors illustrate a model where one process acts as a data server, distributing initial grid slices to "Compute Nodes" and gathering results at the end.
    *   **Halo Exchange:** The process of nodes trading their boundary slices so they have the "ghost cells" needed for the next stencil calculation.

    ## 20.5 Overlapping Computation and Communication {#en-overlapping}

    *   **The Latency Problem:** Network communication is much slower than GPU math. If the GPU sits idle while the network moves data, performance is poor.
    *   **CUDA Streams:** A stream is a sequence of operations (kernels, memory copies) that execute in order. Different streams can execute **simultaneously**.
    *   **The Two-Stage Strategy:**
    
        1. **Stage 1 (Boundary):** The GPU calculates only the edge slices of the grid and immediately starts a `cudaMemcpyAsync` to the host.
        2. **Stage 2 (Internal):** While the edges are being sent over the network, the GPU calculates the massive "internal" part of the grid in a **separate stream**.
        
    *   **Pinned Memory (`cudaHostAlloc`):** Necessary for "Asynchronous" transfers. It prevents the operating system from moving data in RAM, allowing the GPU to copy data to the host without stopping the CPU.

    ## 20.6 Collective Communication {#en-collective}

    *   **Synchronization:** Introduces `MPI_Barrier`, which forces every node in the cluster to wait until all have reached that point.
    *   **Other Patterns:** Mentions broadcast, reduce, and gather—functions optimized by vendors to move data across all nodes efficiently.

    ## 20.7 CUDA-Aware MPI {#en-cuda-aware}

    *   **Modern Optimization:** Explains that newer MPI libraries (like OpenMPI or MVAPICH2) can point directly to **GPU memory addresses**.
    *   **Benefit:** The programmer no longer has to manually copy data from GPU to CPU before sending it over the network. This simplifies the code and allows the hardware to optimize the transfer path.

    ## 20.8 Summary {#en-summary}

    *   Scaling to a cluster requires a "Symbiotic Relationship" between MPI (inter-node) and CUDA (intra-node).
    *   The key to high performance in a cluster is using **Streams** and **Asynchronous Transfers** to hide the "Network Wall" behind the GPU's "Compute Power."

    ---

    **Key Takeaway:** Chapter 20 teaches you how to break the "single-node" limit. The essential lesson is **Communication-Hiding**: using CUDA Streams to ensure the GPU is always doing internal math while the network is busy trading boundary data.

=== "Tiếng Việt"

    Chương này đánh dấu sự bắt đầu của **Phần IV: Thực hành Nâng cao (Advanced Practices)**. Nó chuyển từ một máy đơn lẻ sang các **cụm tính toán hiệu năng cao (HPC clusters)**, dạy cách kết hợp CUDA với **Giao diện Truyền Thông báo (MPI)** để mở rộng các ứng dụng trên nhiều nút (node).

    ## 20.1 Bối cảnh {#vi-background}

    *   **Cụm HPC:** Các siêu máy tính hiện đại bao gồm hàng nghìn "nút". Mỗi nút có CPU (Host) và GPU (Device) riêng.
    *   **Thách thức:** Các nút không chia sẻ bộ nhớ. Để làm việc cùng nhau trong một vấn đề duy nhất, chúng phải "truyền thông báo" qua mạng.
    *   **MPI:** Tiểu chuẩn công nghiệp cho lập trình bộ nhớ phân tán.

    ## 20.2 Ví dụ thực tế: 3D Stencil {#vi-stencil}

    *   **Ứng dụng:** Mô phỏng sự truyền nhiệt trong một ống dẫn 3D bằng cách sử dụng stencil lặp Jacobi 25 điểm.
    *   **Phân vùng miền (Domain Partitioning):** Lưới 3D được cắt dọc theo trục $Z$ thành nhiều **Phân vùng miền** (ví dụ: $D0, D1, D2, D3$). Mỗi phân vùng được gán cho một tiến trình MPI khác nhau (và do đó là một GPU khác nhau).
    *   **Sự phụ thuộc:** Giống như trong Chương 8, mỗi lát cắt cần dữ liệu từ các nút lân cận để tính toán bước tiếp theo. Trong một cụm máy tính, những nút lân cận này nằm trên các máy vật lý khác nhau.

    ## 20.3 Cơ bản về Giao diện Truyền Thông báo (MPI) {#vi-mpi-basics}

    *   **Mô hình SPMD:** Giống như CUDA, MPI sử dụng cách tiếp cận "Single Program Multiple Data" trong đó mọi nút chạy cùng một mã nhưng hoạt động khác nhau dựa trên ID của nó.
    *   **Rank MPI:** Mỗi tiến trình được gán một ID duy nhất gọi là **Rank** (tương tự như `threadIdx` nhưng cho cả một máy).
    *   **Các hàm cốt lõi:**
        *   `MPI_Init` / `MPI_Finalize`: Bắt đầu và kết thúc môi trường MPI.
        *   `MPI_Comm_rank`: Xác định Rank của tiến trình hiện tại.
        *   `MPI_Comm_size`: Tìm tổng số tiến trình trong cụm.

    ## 20.4 Truyền thông Điểm-đến-Điểm (Point-to-Point) {#vi-communication}

    *   **Send/Recv:** Sử dụng `MPI_Send` và `MPI_Recv` để di chuyển dữ liệu giữa các nút cụ thể.
    *   **Máy chủ dữ liệu:** Các tác giả minh họa một mô hình trong đó một tiến trình hoạt động như máy chủ dữ liệu, phân phối các lát lưới ban đầu cho các "Nút tính toán (Compute Nodes)" và thu thập kết quả cuối cùng.
    *   **Trao đổi Halo:** Quá trình các nút trao đổi các lát ranh giới của chúng để chúng có các "ô ma (ghost cells)" cần thiết cho phép tính stencil tiếp theo.

    ## 20.5 Chồng lấp Tính toán và Truyền thông {#vi-overlapping}

    *   **Vấn đề độ trễ:** Truyền thông qua mạng chậm hơn nhiều so với tính toán trên GPU. Nếu GPU nhàn rỗi trong khi mạng di chuyển dữ liệu, hiệu suất sẽ rất kém.
    *   **CUDA Streams:** Một stream là một chuỗi các thao tác (kernel, sao chép bộ nhớ) thực thi theo thứ tự. Các stream khác nhau có thể thực thi **đồng thời**.
    *   **Chiến lược hai giai đoạn:**
    
        1. **Giai đoạn 1 (Ranh giới):** GPU chỉ tính toán các lát cạnh của lưới và bắt đầu ngay lập tức một lệnh `cudaMemcpyAsync` sang host.
        2. **Giai đoạn 2 (Bên trong):** Trong khi các cạnh đang được gửi qua mạng, GPU tính toán phần lớn "bên trong" của lưới trong một **stream riêng biệt**.
        
    *   **Pinned Memory (`cudaHostAlloc`):** Cần thiết cho các lần truyền "Bất đồng bộ". Nó ngăn hệ điều hành di chuyển dữ liệu trong RAM, cho phép GPU sao chép dữ liệu sang host mà không làm dừng CPU.

    ## 20.6 Truyền thông tập thể (Collective Communication) {#vi-collective}

    *   **Đồng bộ hóa:** Giới thiệu `MPI_Barrier`, buộc mọi nút trong cụm phải đợi cho đến khi tất cả đều đạt đến điểm đó.
    *   **Các mẫu khác:** Đề cập đến broadcast, reduce và gather—các hàm được các nhà cung cấp tối ưu hóa để di chuyển dữ liệu qua tất cả các nút một cách hiệu quả.

    ## 20.7 CUDA-Aware MPI {#vi-cuda-aware}

    *   **Tối ưu hóa hiện đại:** Giải thích rằng các thư viện MPI mới hơn (như OpenMPI hoặc MVAPICH2) có thể trỏ trực tiếp đến **địa chỉ bộ nhớ GPU**.
    *   **Lợi ích:** Lập trình viên không còn phải sao chép dữ liệu từ GPU sang CPU một cách thủ công trước khi gửi qua mạng. Điều này đơn giản hóa mã nguồn và cho phép phần cứng tối ưu hóa đường truyền.

    ## 20.8 Tóm tắt {#vi-summary}

    *   Mở rộng lên một cụm máy tính đòi hỏi một "Mối quan hệ cộng sinh" giữa MPI (giữa các nút) và CUDA (trong một nút).
    *   Chìa khóa để đạt hiệu năng cao trong một cụm là sử dụng **Streams** và **Truyền bất đồng bộ** để che giấu "Bức tường Mạng" đằng sau "Sức mạnh tính toán" của GPU.

    ---

    **Điểm chính:** Chương 20 dạy bạn cách phá vỡ giới hạn "nút đơn". Bài học thiết yếu là **Che giấu truyền thông (Communication-Hiding)**: sử dụng CUDA Streams để đảm bảo GPU luôn thực hiện tính toán bên trong trong khi mạng đang bận rộn trao đổi dữ liệu ranh giới.
