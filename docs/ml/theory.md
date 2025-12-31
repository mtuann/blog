# Machine Learning Theory

This section covers the mathematical foundations of modern machine learning algorithms.

## The Attention Mechanism

The core of the Transformer architecture is the Scaled Dot-Product Attention.

The attention function implies mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

### Mathematical Formulation

Given queries $Q$, keys $K$, and values $V$, the attention matrix is calculated as:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Where:

*   $Q \in \mathbb{R}^{n \times d_k}$
*   $K \in \mathbb{R}^{m \times d_k}$
*   $V \in \mathbb{R}^{m \times d_v}$
*   $d_k$ is the dimension of the keys (and queries).

!!! note "Why Scale by $\sqrt{d_k}$?"
    We divide by $\sqrt{d_k}$ to prevent the dot products from growing too large in magnitude. If the dot products are large, the gradient of the softmax function becomes extremely small ("vanishing gradients"), leading to hard training.

### Multi-Head Attention

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions.

$$
\begin{aligned}
\text{MultiHead}(Q, K, V) &= \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O \\
\text{where } \text{head}_i &= \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)
\end{aligned}
$$
