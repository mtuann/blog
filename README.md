# Tuan's Blog

A high-performance technical blog dedicated to the frontiers of **AI Systems**, **Generative AI**, **Efficient AI**, and **Machine Learning Theory**.

Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## 🌟 Key Features

*   **Responsive Technology**: Clean, modern UI with "Outfit" typography and glassmorphism headers.
*   **Engineering-Focused**: First-class support for LaTeX math ($$ E=mc^2 $$), Python code highlighting, and request/response examples.
*   **Automated Workflow**: Fully CI/CD integrated with GitHub Actions.
*   **Performance**: Lightning-fast static site generation.

## 📂 Project Structure

```bash
mtuann.blog/
├── docs/                   # Content Source
│   ├── index.md            # Landing Page
│   ├── ai-systems/         # System Engineering & Infrastructure
│   ├── genai/              # LLMs, Diffusion, & Reasoning
│   ├── efficient-ai/       # Quantization, Pruning, & Edge AI
│   ├── trustworthy-ai/     # Safety, Alignment, & Interpretability
│   ├── paper-reviews/      # Arxiv Analysis & Summaries
│   ├── ml/                 # Foundations & Theory
│   ├── stylesheets/        # Custom CSS (Glassmorphism, etc.)
│   └── snippets/           # Reusable code blocks
├── mkdocs.yml              # Main configuration
├── requirements.txt        # Python dependencies
└── .github/workflows/      # Deployment pipelines
```

## 🚀 Getting Started

### Prerequisites

*   Python 3.10+
*   [uv](https://github.com/astral-sh/uv) (Recommended) or pip

### Installation

We use **uv** for ultra-fast environment management.

```bash
# 1. Clone the repo
git clone https://github.com/mtuann/blog.git
cd blog

# 2. Create virtual env
uv venv

# 3. Activate
source .venv/bin/activate

# 4. Install dependencies
uv pip install -r requirements.txt
```

### Local Development

Start the hot-reloading development server:

```bash
mkdocs serve
```

Visit `http://127.0.0.1:8000` in your browser.

## ✍️ Writing Content

This blog uses extended Markdown features.

### Math (LaTeX)
```latex
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$
```

### Icons & Emojis
Use Material Design icons directly in text:
*   `:material-brain:` -> 🧠 (styled icon)
*   `:material-server-network:` -> 🖥️ (server icon)

### Admonitions
```markdown
!!! tip "Optimization Tip"
    Use FlashAttention-2 to reduce memory footprint by quadratic factors.
```

## 🚢 Deployment

**Automated (Recommended)**:
This requires no manual effort.
1.  Push changes to `main`.
2.  GitHub Actions (`.github/workflows/deploy.yml`) builds and deploys to `gh-pages` automatically.

**Manual**:
```bash
mkdocs gh-deploy
```

## 📜 License

[MIT](LICENSE) © 2026 Tuan Nguyen
