# Transformer & Attention Foundations

=== "English"

    The **Transformer** architecture, introduced in the seminal paper *[Attention Is All You Need](https://arxiv.org/abs/1706.03762)* (Vaswani et al., 2017), revolutionized natural language processing by dispensing with recurrence and convolutions entirely.

    This deep dive covers the mathematical and implementation foundations of the Transformer, focusing on the mechanism that powers it all: **Self-Attention**.

    ## 1. The Bottleneck of Recurrence {#en-bottleneck}

    Prior to Transformers, Sequence-to-Sequence (Seq2Seq) tasks were dominated by RNNS (LSTMs/GRUs). These suffered from a critical limitation: **Sequential Computation**.

    *   **Sequentiality**: $h_t$ depends on $h_{t-1}$, preventing parallelization across time steps.
    *   **Long-term Dependencies**: Information must flow through $O(N)$ steps to connect distant words.

    Transformers process the entire sequence **in parallel**, reducing path length between any two positions to $O(1)$.

    ## 2. Scaled Dot-Product Attention {#en-attention}

    The core engine of the Transformer is the attention mechanism. It allows the model to weigh the importance of different tokens in the input sequence when processing a specific token.

    ### The Query-Key-Value Abstraction {#en-qkv}

    We map the input vectors into three distinct spaces:

    *   **Query ($Q$)**: What I am looking for? (The question)
    *   **Key ($K$)**: What can I offer? (The index)
    *   **Value ($V$)**: What is my actual content? (The answer)

    ### Mathematical Formulation {#en-math}

    Given a query matrix $Q$, key matrix $K$, and value matrix $V$, the attention scores are calculated as:

    $$
    \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
    $$

    Where $d_k$ is the dimension of the key vectors.

    !!! note "Why Scale by $\sqrt{d_k}$?"
        As $d_k$ increases, the dot products $q \cdot k$ can grow large in magnitude. This pushes the softmax function into regions where gradients are extremely small (vanishing gradients). Scaling by $\frac{1}{\sqrt{d_k}}$ keeps the variance stable.

    ## 2.1 Intuition of Attention {#en-intuition}

    Attention can be viewed as a **soft, differentiable lookup mechanism**. For a given query, the model searches over all keys, determines their relevance, and aggregates the corresponding values.

    ## 2.2 Visualization of Attention {#en-visualization}

    Each token attends to all other tokens with different strengths, forming a weighted dependency graph.

    Example: In the sentence "The animal didn't cross the street because **it** was tired", the token "it" will assign a high attention weight to "animal" and low to "street", helping the model resolve coreference.

    ### Implementation (PyTorch) {#en-pytorch}

    ```python
    import torch
    import torch.nn.functional as F
    import math

    def scaled_dot_product_attention(query, key, value, mask=None):
        d_k = query.size(-1)
        scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        attn_weights = F.softmax(scores, dim=-1)
        output = torch.matmul(attn_weights, value)
        return output, attn_weights
    ```

    ## 3. Multi-Head Attention (MHA) {#en-mha}

    A single attention head might focus on a specific relationship (e.g., subject-verb). To capture multiple types of relationships simultaneously, we use **Multi-Head Attention**.

    $$
    \begin{aligned}
    \text{MultiHead}(Q, K, V) &= \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O \\
    \text{head}_i &= \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)
    \end{aligned}
    $$

    ## 4. Positional Encoding {#en-pos}

    Since the Transformer contains no recurrence and no convolution, it has no inherent sense of order. We inject **Positional Encodings** at the input embeddings.

    $$
    \begin{aligned}
    PE_{(pos, 2i)} &= \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right) \\
    PE_{(pos, 2i+1)} &= \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
    \end{aligned}
    $$

    ## 5. Architecture Components {#en-arch}

    A full Transformer block consists of:
    1. **Multi-Head Self-Attention**
    2. **Position-wise Feed-Forward Networks** (FFN)

    $$
    \text{LayerOutput}(x) = \text{LayerNorm}(x + \text{Sublayer}(x))
    $$

    ## 6. Summary {#en-summary}

    The Transformer shift enabled:
    
    1. **Massive Parallelism**
    2. **Global Receptive Field**
    3. **Foundation Models** (GPT, Claude, Gemini)

=== "Tiếng Việt"

    Kiến trúc **Transformer**, được giới thiệu trong bài báo mang tính nền tảng *Attention Is All You Need* (Vaswani et al., 2017), đã tạo ra một bước ngoặt quan trọng trong lĩnh vực xử lý ngôn ngữ tự nhiên khi **loại bỏ hoàn toàn** các cơ chế đệ quy (recurrence) và tích chập (convolution).

    Bài viết này trình bày có hệ thống các nền tảng **toán học**, **trực giác**, và **triển khai thực tế** của Transformer, tập trung vào cơ chế trung tâm quyết định hiệu năng của mô hình: **Self-Attention** (cơ chế tự chú ý).

    ## 1. Nút thắt của mô hình đệ quy {#vi-bottleneck}

    Trước khi Transformer ra đời, các bài toán Sequence-to-Sequence (Seq2Seq) chủ yếu sử dụng các mô hình dựa trên RNN (LSTM/GRU). Những mô hình này gặp một hạn chế mang tính cấu trúc: **tính toán tuần tự**.

    *   **Tính tuần tự (Sequentiality)**: Trạng thái ẩn $h_t$ phụ thuộc vào $h_{t-1}$, khiến việc song song hóa theo chiều thời gian là không khả thi.
    *   **Phụ thuộc dài hạn (Long-term dependencies)**: Thông tin phải đi qua $O(N)$ bước để liên kết các token ở xa nhau, làm suy giảm khả năng học quan hệ dài hạn.

    Transformer xử lý toàn bộ chuỗi **song song**, đồng thời rút ngắn độ dài đường truyền thông tin giữa hai vị trí bất kỳ xuống còn $O(1)$.

    ## 2. Cơ chế Scaled Dot-Product Attention {#vi-attention}

    Thành phần cốt lõi của Transformer là **cơ chế Attention**. Cơ chế này cho phép mô hình **đánh trọng số mức độ liên quan** giữa các token trong chuỗi khi biểu diễn một token cụ thể.

    ### Trừu tượng Query–Key–Value (QKV) {#vi-qkv}

    Các biểu diễn đầu vào được chiếu tuyến tính sang ba không gian vector khác nhau:

    *   **Query ($Q$)**: Biểu diễn thông tin mà token hiện tại đang truy vấn.
    *   **Key ($K$)**: Biểu diễn thông tin dùng để so khớp (matching) với query.
    *   **Value ($V$)**: Biểu diễn nội dung thông tin thực sự sẽ được tổng hợp.

    ### Công thức toán học {#vi-math}

    $$
    \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
    $$

    Trong đó $d_k$ là số chiều của vector key.

    !!! note "Vì sao cần chuẩn hóa theo $\sqrt{d_k}$?"
        Khi $d_k$ tăng, tích vô hướng $q \cdot k$ có xu hướng có độ lớn lớn hơn, khiến hàm softmax rơi vào vùng bão hòa và làm gradient trở nên rất nhỏ. Việc chia cho $\sqrt{d_k}$ giúp ổn định phương sai của điểm attention và cải thiện quá trình huấn luyện.

    ## 2.1 Trực giác về Attention {#vi-intuition}

    Attention có thể được hiểu như một **cơ chế tra cứu mềm (soft lookup)** và khả vi.  
    Với mỗi token đang xét (query), mô hình:

    1. So sánh query với **tất cả key** trong chuỗi.
    2. Đánh giá mức độ liên quan thông qua tích vô hướng.
    3. Chuẩn hóa các mức độ liên quan bằng softmax.
    4. Tổng hợp thông tin từ các value theo trọng số tương ứng.

    Nói cách khác, mỗi token **tự quyết định nên “chú ý” đến những token nào khác** khi xây dựng biểu diễn của chính nó.

    ## 2.2 Hình dung cơ chế Attention {#vi-visualization}

    Có thể hình dung Attention như một **đồ thị phụ thuộc đầy đủ**: mỗi token là một nút và trọng số attention là độ mạnh của cạnh nối.

    Ví dụ: Trong câu “The animal didn’t cross the street because **it** was tired”, từ “it” sẽ gán trọng số cao cho “animal” và thấp cho “street”, giúp mô hình hiểu được “it” đang ám chỉ đối tượng nào.

    ### Triển khai (PyTorch) {#vi-pytorch}

    ```python
    import torch
    import torch.nn.functional as F
    import math

    def scaled_dot_product_attention(query, key, value, mask=None):
        d_k = query.size(-1)
        scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        attn_weights = F.softmax(scores, dim=-1)
        output = torch.matmul(attn_weights, value)
        return output, attn_weights
    ```

    ## 3. Cơ chế chú ý đa đầu (MHA) {#vi-mha}

    Một đầu chú ý đơn lẻ thường chỉ học được một kiểu quan hệ nhất định. **Multi-Head Attention** cho phép mô hình học nhiều loại quan hệ song song từ nhiều góc nhìn khác nhau.

    $$
    \begin{aligned}
    \text{MultiHead}(Q, K, V) &= \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O \\
    \text{head}_i &= \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)
    \end{aligned}
    $$

    ## 4. Mã hóa vị trí (Positional Encoding) {#vi-pos}

    Do Transformer không có cơ chế đệ quy, thông tin vị trí phải được tiêm trực tiếp vào embedding thông qua các hàm sin và cos.

    $$
    \begin{aligned}
    PE_{(pos, 2i)} &= \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right) \\
    PE_{(pos, 2i+1)} &= \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
    \end{aligned}
    $$

    ## 5. Các thành phần kiến trúc {#vi-arch}

    Một khối Transformer chuẩn bao gồm hai lớp phụ: **Multi-Head Self-Attention** và **Feed-Forward Network (FFN)**, được bao bọc bởi kết nối dư và chuẩn hóa lớp (LayerNorm).

    $$
    \text{LayerOutput}(x) = \text{LayerNorm}(x + \text{Sublayer}(x))
    $$

    ## 6. Tổng kết {#vi-summary}

    Transformer thay thế hoàn toàn đệ quy bằng Attention, cho phép:

    1. **Song song hóa toàn diện**
    2. **Trường tiếp nhận toàn cục**
    3. **Khả năng mở rộng quy mô lớn** (nền tảng cho GPT, Claude, Gemini).
