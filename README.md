# Tuan's Blog

A technical blog and research garden dedicated to **Machine Learning**, **Generative AI**, **AI Systems**, **Efficient AI**, **Trustworthy AI**, and **Research Notes**.

Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Key Features

- **Math-first writing** with LaTeX, Mermaid, code highlighting, and long-form technical notes.
- **Evergreen section hubs** that grow from foundations to advanced research.
- **Research-note workflow** for paper reviews, roundups, and reading maps.
- **Automated deployment** through GitHub Actions.

## Project Structure

```bash
mtuann.blog/
├── docs/                   # Published content source
│   ├── index.md            # Landing page
│   ├── ml/                 # Foundations, theory, and practical ML
│   ├── genai/              # LLMs, multimodal systems, and agents
│   ├── ai-systems/         # Distributed training, serving, and GPU systems
│   ├── cuda/               # GPU systems and PMPP study notes
│   ├── efficient-ai/       # Compression, sparsity, and efficient inference
│   ├── trustworthy-ai/     # Evaluation, robustness, and interpretability
│   ├── research-notes/     # Roundups, reading maps, and note hubs
│   ├── paper-reviews/      # Individual paper deep dives
│   ├── stylesheets/        # Custom CSS
│   └── snippets/           # Reusable code blocks
├── drafts/                 # Unpublished capture notes and scratch work
├── playbooks/              # Internal research and authoring workflows
├── templates/              # Reusable post templates
├── scripts/                # Local authoring helpers
├── mkdocs.yml              # Main configuration
├── requirements.txt        # Python dependencies
└── .github/workflows/      # Deployment pipelines
```

## Getting Started

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) or pip

### Installation

```bash
git clone https://github.com/mtuann/blog.git
cd blog
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Local Development

```bash
mkdocs serve
```

Visit `http://127.0.0.1:8000` in your browser.

## Writing Content

This blog uses extended Markdown features.

### Math

```latex
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$
```

### Admonitions

```markdown
!!! tip "Optimization Tip"
    Use FlashAttention-2 to reduce memory footprint by reducing HBM traffic.
```

### Authoring Workflow

- Keep unfinished ideas in `drafts/` so they never publish accidentally.
- Use `playbooks/topic-backlog-enrichment.md` when turning a backlog item into a current, research-first topic page.
- Use `templates/` for consistent post structure.
- Add research-note pages without touching the top navigation.
- Link every new note back into the relevant section hub.

### Post Scaffolding

Use the local helper to create new posts from templates:

```bash
python scripts/new_post.py --kind paper-review --title "My Paper Review"
python scripts/new_post.py --kind roundup --title "KV Cache Notes"
python scripts/new_post.py --kind reading-map --title "Long Context LLMs"
python scripts/new_post.py --kind evergreen --section ml --title "Optimization Notes"
```

Use `--dry-run` first if you want to preview the target path.

## Deployment

**Automated**

1. Push changes to `main`.
2. GitHub Actions builds and deploys to `gh-pages`.

**Manual**

```bash
mkdocs gh-deploy
```

## License

[MIT](LICENSE) © 2026 Tuan Nguyen
