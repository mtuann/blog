# Chapter 15: Parallel Graph Algorithms

=== "English"

    This chapter focuses on processing graphs (networks of vertices and edges), which are the foundation of social networks, map services, and circuit design. It highlights how graph problems are essentially "dynamic sparse matrix problems."

    ## 15.1 Background {#en-background}

    **Definitions:** Entities are **Vertices** and their relationships are **Edges**.
    
    **Adjacency Matrix:** A grid where a "1" at `A[i][j]` indicates an edge from vertex $i$ to vertex $j$.
    
    **Sparsity:** Real-world graphs (like Facebook) are **sparsely connected**; most vertices have few neighbors.
    
    **Storage:** Graphs are stored using the sparse formats from Chapter 14:
    
    *   **CSR:** Best for finding all **outgoing** edges of a vertex.
    *   **CSC:** Best for finding all **incoming** edges to a vertex.
    *   **COO:** Simple list of edges; good for edge-centric processing.

    ## 15.2 Breadth-First Search (BFS) {#en-bfs}

    **The Goal:** Discover the shortest distance (in "hops") from a root vertex to all other vertices.
    
    **Wavefronts:** BFS proceeds in levels (Level 0 $\rightarrow$ Level 1 $\rightarrow$ ...). Each level forms a "wavefront" of newly discovered vertices.
    
    **Application (CAD):** Explains **Maze Routing**, where BFS finds the shortest path for a wire on a microchip while avoiding obstacles.

    ## 15.3 Vertex-Centric Parallelization (Push vs. Pull) {#en-push-pull}

    **Push (Top-Down):** Threads are assigned to vertices in the *current* level. They "push" their status to their neighbors.
    
    *   *Pros:* Efficient when the wavefront is small (early levels).
    *   *Cons:* High contention as many parents try to update the same child.
    
    **Pull (Bottom-Up):** Threads are assigned to *unvisited* vertices. They "pull" status from neighbors to see if any are in the previous level.
    
    *   *Pros:* Excellent for "Small World" graphs (like social networks) in later levels where most vertices are already visited.
    
    **Direction-Optimized BFS:** A key optimization that switches from Push to Pull mid-execution to maximize efficiency.

    ## 15.4 Edge-Centric Parallelization {#en-edge-centric}

    **The Approach:** Assign one thread to **every edge** in the graph.
    
    **Benefit:** Provides better load balancing for graphs with a massive variation in vertex degrees (e.g., a "celebrity" vertex with millions of edges vs. a "normal" vertex with ten).
    
    **Drawback:** Every single edge is checked in every level, which is wasteful for large, deep graphs.

    ## 15.5 Improving Efficiency with Frontiers {#en-frontiers}

    **The Problem:** Launching a thread for every vertex in the graph is wasteful if only 1% are active.
    
    **The Solution:** Use a **Frontier** (a list of only the currently active vertices).
    
    **Atomics:** Requires `atomicCAS` (Compare-And-Swap) to ensure a vertex is added to the frontier only once, even if multiple neighbors discover it at the same time.

    ## 15.6 Reducing Contention with Privatization {#en-privatization}

    **The Bottleneck:** Thousands of threads trying to `atomicAdd` to the global frontier causes a massive "hot spot" in memory.
    
    **The Strategy:** Each thread block builds a **Private Frontier** in **Shared Memory**. Once full, the block performs a single global atomic operation to merge its results.
    
    **Result:** Drastically reduces the number of global memory conflicts.

    ## 15.7 Other Optimizations {#en-other}

    *   **Reducing Launch Overhead:** For small frontiers, multiple levels can be processed within a single kernel launch using `__syncthreads()`, rather than returning to the CPU.
    *   **Improving Load Balance:** Vertices can be "bucketed" by their degree. "Celebrity" vertices are processed by entire blocks, while "low-degree" vertices are handled by single threads.

    ---

    **Key Takeaway:** Chapter 15 teaches that there is no "one-size-fits-all" algorithm for graphs. Performance depends on the **graph's topology**. You must use **Frontiers** to limit work, **Privatization** to handle contention, and **Direction-Optimization** to adapt to the growing wavefront of the search.

=== "Tiếng Việt"

    Chương này tập trung vào xử lý đồ thị (mạng lưới các đỉnh và cạnh), là nền tảng của các mạng xã hội, dịch vụ bản đồ và thiết kế mạch điện. Nó nhấn mạnh cách các bài toán đồ thị thực chất là các "bài toán ma trận thưa động".

    ## 15.1 Bối cảnh {#vi-background}

    **Định nghĩa:** Các thực thể là **Đỉnh (Vertices)** và mối quan hệ của chúng là **Cạnh (Edges)**.
    
    **Ma trận kề (Adjacency Matrix):** Một lưới nơi giá trị "1" tại `A[i][j]` cho biết có một cạnh từ đỉnh $i$ đến đỉnh $j$.
    
    **Độ thưa:** Các đồ thị thực tế (như Facebook) có **kết nối thưa thớt**; hầu hết các đỉnh có ít nút lân cận.
    
    **Lưu trữ:** Đồ thị được lưu trữ bằng các định dạng thưa từ Chương 14:
    
    *   **CSR:** Tốt nhất để tìm tất cả các cạnh **đi ra** từ một đỉnh.
    *   **CSC:** Tốt nhất để tìm tất cả các cạnh **đi vào** một đỉnh.
    *   **COO:** Danh sách đơn giản các cạnh; tốt cho xử lý tập trung vào cạnh.

    ## 15.2 Tìm kiếm theo chiều rộng (BFS) {#vi-bfs}

    **Mục tiêu:** Khám phá khoảng cách ngắn nhất (tính theo "số bước nhảy - hops") từ một đỉnh gốc đến tất cả các đỉnh khác.
    
    **Các mặt sóng (Wavefronts):** BFS tiến hành theo các cấp độ (Cấp 0 $\rightarrow$ Cấp 1 $\rightarrow$ ...). Mỗi cấp độ tạo thành một "mặt sóng" của các đỉnh mới được khám phá.
    
    **Ứng dụng (CAD):** Giải thích về **Maze Routing** (Định tuyến mê cung), nơi BFS tìm đường ngắn nhất cho một sợi dây trên vi mạch trong khi tránh các chướng ngại vật.

    ## 15.3 Song song hóa lấy đỉnh làm trung tâm (Push vs. Pull) {#vi-push-pull}

    **Push (Top-Down):** Các luồng được gán cho các đỉnh ở cấp độ *hiện tại*. Chúng "đẩy (push)" trạng thái của mình tới các nút lân cận.
    
    *   *Ưu điểm:* Hiệu quả khi mặt sóng nhỏ (các cấp độ đầu).
    *   *Nhược điểm:* Tranh chấp cao khi nhiều nút cha cố gắng cập nhật cùng một nút con.
    
    **Pull (Bottom-Up):** Các luồng được gán cho các đỉnh *chưa được thăm*. Chúng "kéo (pull)" trạng thái từ các nút lân cận để xem có nút nào thuộc cấp độ trước đó không.
    
    *   *Ưu điểm:* Tuyệt vời cho các đồ thị "Thế giới nhỏ" (như mạng xã hội) ở các cấp độ sau khi hầu hết các đỉnh đã được thăm.
    
    **Direction-Optimized BFS:** Một tối ưu hóa quan trọng giúp chuyển đổi từ Push sang Pull giữa quá trình thực thi để tối đa hóa hiệu quả.

    ## 15.4 Song song hóa lấy cạnh làm trung tâm {#vi-edge-centric}

    **Cách tiếp cận:** Gán một luồng cho **mọi cạnh** trong đồ thị.
    
    **Lợi ích:** Cung cấp khả năng cân bằng tải tốt hơn cho các đồ thị có sự thay đổi lớn về bậc của đỉnh (ví dụ: một đỉnh "người nổi tiếng" với hàng triệu cạnh và một đỉnh "bình thường" với mười cạnh).
    
    **Hạn chế:** Từng cạnh một đều bị kiểm tra ở mọi cấp độ, điều này gây lãng phí cho các đồ thị lớn và sâu.

    ## 15.5 Cải thiện hiệu quả với Frontiers (Biên) {#vi-frontiers}

    **Vấn đề:** Khởi chạy một luồng cho mọi đỉnh trong đồ thị là lãng phí nếu chỉ có 1% đang hoạt động.
    
    **Giải pháp:** Sử dụng một **Frontier** (một danh sách chỉ chứa các đỉnh hiện đang hoạt động).
    
    **Tranh chấp (Atomics):** Yêu cầu `atomicCAS` (Compare-And-Swap) để đảm bảo một đỉnh chỉ được thêm vào frontier một lần, ngay cả khi nhiều nút lân cận cùng lúc khám phá ra nó.

    ## 15.6 Giảm tranh chấp với Privatization {#vi-privatization}

    **Nút thắt cổ chai:** Hàng nghìn luồng cố gắng `atomicAdd` vào frontier toàn cục gây ra một "điểm nóng" lớn trong bộ nhớ.
    
    **Chiến lược:** Mỗi khối luồng (thread block) xây dựng một **Frontier riêng** trong **Shared Memory**. Sau khi đầy, khối thực hiện một thao tác atomic toàn cục duy nhất để hợp nhất các kết quả của nó.
    
    **Kết quả:** Giảm đáng kể số lượng xung đột bộ nhớ toàn cục.

    ## 15.7 Các tối ưu hóa khác {#vi-other}

    *   **Giảm chi phí khởi chạy:** Đối với các frontier nhỏ, nhiều cấp độ có thể được xử lý trong một lần khởi chạy kernel duy nhất bằng cách sử dụng `__syncthreads()`, thay vì quay lại CPU.
    *   **Cải thiện cân bằng tải:** Các đỉnh có thể được "phân nhóm" theo bậc của chúng. Các đỉnh "người nổi tiếng" được xử lý bởi toàn bộ các khối, trong khi các đỉnh "bậc thấp" được xử lý bởi các luồng đơn lẻ.

    ---

    **Điểm chính:** Chương 15 dạy rằng không có thuật toán "vạn năng" cho đồ thị. Hiệu suất phụ thuộc vào **cấu trúc (topology) của đồ thị**. Bạn phải sử dụng **Frontiers** để giới hạn công việc, **Privatization** để xử lý tranh chấp, và **Direction-Optimization** để thích ứng với mặt sóng ngày càng mở rộng của quá trình tìm kiếm.
