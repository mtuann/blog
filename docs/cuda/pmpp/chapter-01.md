# Chapter 1: Introduction

=== "English"

    This chapter sets the stage for the book by explaining the shift in the computing industry from sequential to parallel processing.

    ## 1.1 Heterogeneous Parallel Computing {#en-heterogeneous}

    **The Shift (2003):** Before 2003, performance increased by raising clock frequencies. Due to energy and heat limits, the industry shifted to two main trajectories:
    
    *   **Multicore Trajectory:** (CPUs like Intel/AMD) Focuses on **latency-oriented design**. They use large caches and sophisticated branch prediction to make a single sequence of instructions (a thread) run as fast as possible.
    *   **Many-thread Trajectory:** (GPUs like NVIDIA A100) Focuses on **throughput-oriented design**. They use thousands of smaller, simpler cores to execute massive numbers of threads simultaneously.
    
    **Performance Gap:** In 2021, a high-end GPU (A100) offered significantly higher peak floating-point throughput (TFLOPS) compared to a high-end CPU, particularly in single and half-precision (essential for AI).
    
    **The CUDA Model:** Introduced in 2007, it moved away from the "GPGPU" era (where programmers had to "trick" the GPU by treating data as pixels) to a general-purpose programming model where the CPU (**host**) and GPU (**device**) work together.

    ## 1.2 Why More Speed or Parallelism? {#en-why-speed}

    **Superapplications:** The need for speed is driven by "superapplications" in science and consumer tech:
    
    *   **Molecular Biology:** Simulating interactions between billions of atoms.
    *   **Video/Imaging:** Real-time view synthesis for high-definition TV and better smartphone interfaces.
    *   **Gaming & Digital Twins:** Moving from pre-rendered scenes to dynamic simulations and "digital twins" for stress-testing physical objects.

    ## 1.3 Speeding Up Real Applications {#en-speedup}

    **Defining Speedup:** The ratio of time taken on System B (serial) vs. System A (parallel).
    
    **Amdahl's Law:** A critical concept stating that the total speedup of an application is limited by its sequential portion.
    
    *   *Example:* If only 30% of a program is parallelized, even an infinite speedup of that part only results in a 1.43x total improvement.
    *   To get a 100x speedup, more than 99.9% of the work must be parallelized.
    
    **The "Peach" Analogy:** Real-world applications are like a peach. The **"pit"** is the sequential part (hard to bite into/parallelize), while the **"flesh"** is the parallel part (large and easy to process).
    
    **Memory Bandwidth:** Simply running threads isn't enough; memory (DRAM) speed often becomes the bottleneck (Memory-bound). The book focuses on using on-chip memory to bypass these limits.

    ## 1.4 Challenges in Parallel Programming {#en-challenges}

    *   **Algorithmic Complexity:** Some parallel algorithms do more total work than sequential ones; if the data isn't large enough, they can be slower.
    *   **Data Characteristics:** Performance can vary based on whether data is "regular" or "erratic" (leading to load imbalance).
    *   **Synchronization:** Coordination between threads (barriers or atomics) adds overhead.
    *   **The Goal:** The book aims to teach "Parallel Patterns" that solve these common challenges across different domains.

    ## 1.5 Related Parallel Programming Interfaces {#en-interfaces}

    *   **OpenMP:** A high-level, directive-based model for multicore CPUs. It is easier to use but offers less explicit control than CUDA.
    *   **MPI (Message Passing Interface):** The standard for cluster computing (multiple nodes that don't share memory). CUDA is often used *within* a node, while MPI handles communication *between* nodes.
    *   **OpenCL:** A cross-vendor standard similar to CUDA. Skills learned in CUDA are directly transferable to OpenCL.

    ## 1.6 Overarching Goals {#en-goals}

    *   **Computational Thinking:** Learning to formulate problems in a way that is amenable to massive parallelism.
    *   **Scalability:** Writing code that scales naturally as GPUs get more cores in the future.
    *   **Reliability:** Ensuring code is not just fast, but functionally correct and debuggable.

    ## 1.7 Organization of the Book {#en-organization}

    The chapter concludes with a roadmap of the book's four parts:
    
    1. **Foundations:** CUDA basics and architecture.
    2. **Parallel Patterns:** Fundamental algorithms (Convolution, Stencil, Reduction, etc.).
    3. **Advanced Patterns:** Complex applications like Deep Learning and Graph Traversal.
    4. **Advanced Practices:** Clusters, Dynamic Parallelism, and the future.

    ---

    **Summary:** Chapter 1 transitions the reader from "thinking sequentially" to "thinking in throughput," emphasizing that the most important skill in modern computing is the ability to manage thousands of threads and the memory traffic they generate.

=== "Tiếng Việt"

    Chương này đặt nền móng cho cuốn sách bằng cách giải thích sự chuyển dịch trong ngành công nghiệp máy tính từ xử lý tuần tự sang xử lý song song.

    ## 1.1 Tính toán song song không đồng nhất {#vi-heterogeneous}

    **Sự chuyển dịch (2003):** Trước năm 2003, hiệu năng tăng bằng cách tăng tần số xung nhịp. Do giới hạn về năng lượng và nhiệt, ngành công nghiệp chuyển sang hai hướng chính:
    
    *   **Hướng đa lõi:** (CPU như Intel/AMD) Tập trung vào **thiết kế hướng độ trễ**. Sử dụng cache lớn và dự đoán nhánh tinh vi để làm cho một chuỗi lệnh đơn (một luồng) chạy nhanh nhất có thể.
    *   **Hướng đa luồng:** (GPU như NVIDIA A100) Tập trung vào **thiết kế hướng thông lượng**. Sử dụng hàng nghìn lõi nhỏ hơn, đơn giản hơn để thực thi số lượng lớn luồng đồng thời.
    
    **Khoảng cách hiệu năng:** Năm 2021, GPU cao cấp (A100) cung cấp thông lượng tính toán dấu phẩy động đỉnh (TFLOPS) cao hơn đáng kể so với CPU cao cấp, đặc biệt ở độ chính xác đơn và nửa (quan trọng cho AI).
    
    **Mô hình CUDA:** Được giới thiệu năm 2007, chuyển từ kỷ nguyên "GPGPU" (lập trình viên phải "lừa" GPU bằng cách coi dữ liệu như pixel) sang mô hình lập trình đa mục đích nơi CPU (**host**) và GPU (**device**) làm việc cùng nhau.

    ## 1.2 Tại sao cần tốc độ hoặc tính song song cao hơn? {#vi-why-speed}

    **Siêu ứng dụng:** Nhu cầu về tốc độ được thúc đẩy bởi "siêu ứng dụng" trong khoa học và công nghệ tiêu dùng:
    
    *   **Sinh học phân tử:** Mô phỏng tương tác giữa hàng tỷ nguyên tử.
    *   **Video/Hình ảnh:** Tổng hợp khung hình thời gian thực cho TV độ nét cao và giao diện smartphone tốt hơn.
    *   **Game & Bản sao số:** Chuyển từ cảnh được render trước sang mô phỏng động và "bản sao số" để kiểm tra độ bền của vật thể vật lý.

    ## 1.3 Tăng tốc ứng dụng thực tế {#vi-speedup}

    **Định nghĩa Speedup:** Tỷ lệ thời gian thực thi trên Hệ thống B (tuần tự) so với Hệ thống A (song song).
    
    **Định luật Amdahl:** Khái niệm quan trọng cho rằng tổng tốc độ tăng của ứng dụng bị giới hạn bởi phần tuần tự của nó.
    
    *   *Ví dụ:* Nếu chỉ 30% chương trình được song song hóa, ngay cả khi phần đó tăng tốc vô hạn cũng chỉ dẫn đến cải thiện tổng thể 1.43 lần.
    *   Để đạt tốc độ tăng 100 lần, hơn 99.9% công việc phải được song song hóa.
    
    **Phép ẩn dụ "Quả đào":** Ứng dụng thực tế giống như quả đào. **"Hạt"** là phần tuần tự (khó song song hóa), trong khi **"thịt"** là phần song song (lớn và dễ xử lý).
    
    **Băng thông bộ nhớ:** Chỉ chạy nhiều luồng là chưa đủ; tốc độ bộ nhớ (DRAM) thường trở thành nút thắt cổ chai (Memory-bound). Cuốn sách tập trung vào việc sử dụng bộ nhớ trên chip để vượt qua giới hạn này.

    ## 1.4 Thách thức trong lập trình song song {#vi-challenges}

    *   **Độ phức tạp thuật toán:** Một số thuật toán song song thực hiện nhiều công việc hơn so với phiên bản tuần tự; nếu dữ liệu không đủ lớn, chúng có thể chậm hơn.
    *   **Đặc tính dữ liệu:** Hiệu năng có thể thay đổi tùy thuộc vào dữ liệu "đều đặn" hay "bất thường" (dẫn đến mất cân bằng tải).
    *   **Đồng bộ hóa:** Điều phối giữa các luồng (barrier hoặc atomic) tạo ra chi phí quản lý.
    *   **Mục tiêu:** Cuốn sách hướng đến việc dạy "Các mẫu song song" giải quyết những thách thức phổ biến này trong nhiều lĩnh vực khác nhau.

    ## 1.5 Các giao diện lập trình song song liên quan {#vi-interfaces}

    *   **OpenMP:** Mô hình cấp cao, dựa trên chỉ thị cho CPU đa lõi. Dễ sử dụng hơn nhưng kiểm soát ít rõ ràng hơn CUDA.
    *   **MPI (Message Passing Interface):** Tiêu chuẩn cho tính toán cụm (nhiều node không chia sẻ bộ nhớ). CUDA thường được sử dụng *trong* một node, trong khi MPI xử lý giao tiếp *giữa* các node.
    *   **OpenCL:** Tiêu chuẩn đa nhà cung cấp tương tự CUDA. Kỹ năng học được từ CUDA có thể chuyển đổi trực tiếp sang OpenCL.

    ## 1.6 Mục tiêu tổng quát {#vi-goals}

    *   **Tư duy tính toán:** Học cách xây dựng bài toán theo cách phù hợp với tính song song lớn.
    *   **Khả năng mở rộng:** Viết code mở rộng tự nhiên khi GPU có thêm lõi trong tương lai.
    *   **Độ tin cậy:** Đảm bảo code không chỉ nhanh mà còn đúng về mặt chức năng và có thể debug được.

    ## 1.7 Cấu trúc cuốn sách {#vi-organization}

    Chương kết thúc với lộ trình bốn phần của cuốn sách:
    
    1. **Nền tảng:** Cơ bản CUDA và kiến trúc.
    2. **Các mẫu song song:** Thuật toán cơ bản (Convolution, Stencil, Reduction, v.v.).
    3. **Các mẫu nâng cao:** Ứng dụng phức tạp như Deep Learning và Graph Traversal.
    4. **Thực hành nâng cao:** Cụm, Dynamic Parallelism và tương lai.

    ---

    **Tóm tắt:** Chương 1 chuyển đổi người đọc từ "tư duy tuần tự" sang "tư duy thông lượng," nhấn mạnh rằng kỹ năng quan trọng nhất trong tính toán hiện đại là khả năng quản lý hàng nghìn luồng và lưu lượng bộ nhớ mà chúng tạo ra.
