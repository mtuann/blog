# Chapter 7: Convolution

=== "English"

    This chapter begins **Part II (Parallel Patterns)**. It uses the convolution operation—widely used in image processing and signal analysis—to introduce advanced memory management and the "halo cell" concept.

    ## 7.1 Background {#en-background}

    **Definition:** Convolution is an array operation where each output element is a weighted sum of a neighboring patch of input elements.
    
    **The Filter (Mask):** The weights are defined by a small array called a **convolution filter** (or mask).
    
    **The Radius ($r$):** The filter size is typically an odd number ($2r + 1$). The radius $r$ determines how many neighbors on each side contribute to the center element.
    
    **Dimensions:** While 1D convolution is common in audio, the chapter focuses on 2D convolution for images.

    ## 7.2 Parallel Convolution: A Basic Algorithm {#en-basic}

    **Mapping:** Each thread is assigned to calculate one output pixel.
    
    **Ghost Cells:** When calculating pixels near the edge of an image, the filter may "overhang" the data. These missing elements are called **ghost cells**.
    
    **Boundary Handling:** In the basic kernel, an `if` statement checks if a neighbor's coordinates are within the array bounds; if not, the value is typically treated as 0.0.
    
    **Efficiency Problem:** This basic approach has very low arithmetic intensity (**0.25 OP/B**) because every input pixel is loaded from global memory many times by different threads.

    ## 7.3 Constant Memory and Caching {#en-constant}

    **The Observation:** The convolution filter is small (usually < 64KB), stays constant during the kernel, and is accessed by all threads in a warp in the same order.
    
    **Keyword `__constant__`:** These properties make the filter a perfect fit for **Constant Memory**.
    
    **Constant Cache:** GPUs have a specialized "constant cache." Because all threads in a warp access the same filter element at the same time, the hardware "broadcasts" the value, essentially making the access as fast as a register.
    
    **API:** Data is moved to constant memory using `cudaMemcpyToSymbol()`.

    ## 7.4 Tiled Convolution with Halo Cells {#en-halo}

    **The Challenge:** Unlike matrix multiplication where input and output tiles are the same size, convolution requires an "Input Tile" that is larger than the "Output Tile."
    
    **Halo Cells:** To calculate an output tile, you need the internal pixels PLUS a surrounding border of pixels. These border pixels are the **Halo Cells**.
    
    **Thread Organization:** The chapter explores two ways to load tiles:
    
    1. **Block matches Input Tile:** Some threads load data but are "turned off" for the actual math because they map to the halo.
    2. **Block matches Output Tile:** All threads do math, but the loading logic is more complex because some threads must load multiple data points to cover the halo.
    
    **Performance Payoff:** Tiling can increase the compute-to-memory ratio significantly (e.g., from 0.5 to **9.57 OP/B** for a 5x5 filter).

    ## 7.5 Tiled Convolution using Caches for Halo Cells {#en-cache}

    **Simplification:** In modern GPUs, the L2 cache is quite effective.
    
    **The Strategy:** Instead of manually loading halo cells into shared memory, the programmer only loads the "internal" pixels into shared memory and lets the **L2 cache/Read-Only cache** handle the halo cells.
    
    **Benefit:** This makes the code much simpler and more readable while still capturing most of the performance benefits of tiling.

    ## 7.6 Summary of Concepts {#en-summary}

    **Stencil Pattern:** Introduces the idea that convolution is a form of the "stencil" pattern, which is used to solve differential equations (detailed further in Chapter 8).
    
    **Data Reuse:** Tiling for convolution is unique because it manages the overlap of input data needed by neighboring blocks.

    ---

    **Key Takeaway:** Chapter 7 teaches you that when data is accessed by many threads in a predictable way (like a filter), **Constant Memory** is the best tool. It also introduces the complexity of **Halo Cells**, which is essential for any algorithm that uses a "sliding window" over data.

=== "Tiếng Việt"

    Chương này bắt đầu **Phần II (Các mẫu song song)**. Nó sử dụng phép tích chập—được sử dụng rộng rãi trong xử lý ảnh và phân tích tín hiệu—để giới thiệu quản lý bộ nhớ nâng cao và khái niệm "halo cell".

    ## 7.1 Bối cảnh {#vi-background}

    **Định nghĩa:** Tích chập là phép toán mảng trong đó mỗi phần tử đầu ra là tổng có trọng số của vùng lân cận các phần tử đầu vào.
    
    **Bộ lọc (Mask):** Các trọng số được định nghĩa bởi một mảng nhỏ gọi là **bộ lọc tích chập** (hoặc mask).
    
    **Bán kính ($r$):** Kích thước bộ lọc thường là số lẻ ($2r + 1$). Bán kính $r$ xác định có bao nhiêu lân cận ở mỗi bên đóng góp vào phần tử trung tâm.
    
    **Chiều:** Trong khi tích chập 1D phổ biến trong âm thanh, chương này tập trung vào tích chập 2D cho ảnh.

    ## 7.2 Tích chập song song: Thuật toán cơ bản {#vi-basic}

    **Ánh xạ:** Mỗi luồng được gán để tính một pixel đầu ra.
    
    **Ghost Cell:** Khi tính các pixel gần cạnh ảnh, bộ lọc có thể "nhô ra" ngoài dữ liệu. Các phần tử thiếu này được gọi là **ghost cell**.
    
    **Xử lý biên:** Trong kernel cơ bản, câu lệnh `if` kiểm tra xem tọa độ của lân cận có nằm trong giới hạn mảng không; nếu không, giá trị thường được coi là 0.0.
    
    **Vấn đề hiệu quả:** Cách tiếp cận cơ bản này có cường độ số học rất thấp (**0.25 OP/B**) vì mỗi pixel đầu vào được tải từ bộ nhớ global nhiều lần bởi các luồng khác nhau.

    ## 7.3 Bộ nhớ Constant và Caching {#vi-constant}

    **Quan sát:** Bộ lọc tích chập nhỏ (thường < 64KB), giữ nguyên trong kernel và được truy cập bởi tất cả các luồng trong warp theo cùng thứ tự.
    
    **Từ khóa `__constant__`:** Các thuộc tính này làm cho bộ lọc phù hợp hoàn hảo với **Constant Memory**.
    
    **Constant Cache:** GPU có "constant cache" chuyên biệt. Vì tất cả các luồng trong warp truy cập cùng một phần tử bộ lọc cùng lúc, phần cứng "phát sóng" giá trị, về cơ bản làm cho truy cập nhanh như register.
    
    **API:** Dữ liệu được chuyển đến constant memory bằng `cudaMemcpyToSymbol()`.

    ## 7.4 Tích chập Tiled với Halo Cell {#vi-halo}

    **Thách thức:** Không giống như nhân ma trận nơi tile đầu vào và đầu ra có cùng kích thước, tích chập yêu cầu "Input Tile" lớn hơn "Output Tile".
    
    **Halo Cell:** Để tính tile đầu ra, bạn cần các pixel bên trong CỘNG với viền xung quanh các pixel. Các pixel viền này là **Halo Cell**.
    
    **Tổ chức luồng:** Chương khám phá hai cách tải tile:
    
    1. **Block khớp Input Tile:** Một số luồng tải dữ liệu nhưng bị "tắt" cho phép toán thực tế vì chúng ánh xạ đến halo.
    2. **Block khớp Output Tile:** Tất cả các luồng làm toán, nhưng logic tải phức tạp hơn vì một số luồng phải tải nhiều điểm dữ liệu để bao phủ halo.
    
    **Lợi ích hiệu năng:** Tiling có thể tăng tỷ lệ tính toán-bộ nhớ đáng kể (ví dụ: từ 0.5 đến **9.57 OP/B** cho bộ lọc 5x5).

    ## 7.5 Tích chập Tiled sử dụng Cache cho Halo Cell {#vi-cache}

    **Đơn giản hóa:** Trong GPU hiện đại, L2 cache khá hiệu quả.
    
    **Chiến lược:** Thay vì tải thủ công halo cell vào shared memory, lập trình viên chỉ tải các pixel "bên trong" vào shared memory và để **L2 cache/Read-Only cache** xử lý halo cell.
    
    **Lợi ích:** Điều này làm cho code đơn giản và dễ đọc hơn nhiều trong khi vẫn nắm bắt hầu hết lợi ích hiệu năng của tiling.

    ## 7.6 Tóm tắt khái niệm {#vi-summary}

    **Mẫu Stencil:** Giới thiệu ý tưởng rằng tích chập là một dạng của mẫu "stencil", được sử dụng để giải phương trình vi phân (chi tiết hơn trong Chương 8).
    
    **Tái sử dụng dữ liệu:** Tiling cho tích chập độc đáo vì nó quản lý sự chồng chéo của dữ liệu đầu vào cần thiết bởi các block lân cận.

    ---

    **Điểm chính:** Chương 7 dạy bạn rằng khi dữ liệu được truy cập bởi nhiều luồng theo cách có thể dự đoán (như bộ lọc), **Constant Memory** là công cụ tốt nhất. Nó cũng giới thiệu sự phức tạp của **Halo Cell**, điều cần thiết cho bất kỳ thuật toán nào sử dụng "cửa sổ trượt" trên dữ liệu.
