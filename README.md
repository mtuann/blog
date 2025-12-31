# Tuan's Blog

A technical blog dedicated to Machine Learning, Generative AI, and Trustworthy AI.
Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Project Structure

```
mtuann.blog/
├── docs/                   # Content source
│   ├── index.md            # Homepage
│   ├── ml/                 # Machine Learning Section
│   ├── genai/              # Generative AI Section
│   ├── efficient-ai/       # Efficient AI Section
│   ├── trustworthy-ai/     # Trustworthy AI Section
│   ├── snippets/           # Code snippets for inclusion
│   └── javascripts/        # Custom JS (MathJax)
├── mkdocs.yml              # Main configuration
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Getting Started

### Prerequisites

*   Python 3.x
*   [uv](https://github.com/astral-sh/uv) (Recommended for faster setup) or pip

### Installation

We recommend using **uv** for lightning-fast environment management.

1.  **Clone the repository** (if not already local).

2.  **Setup Environment**:

    === "Using uv (Recommended)"
    
        ```bash
        # Create virtual environment
        uv venv
        
        # Activate environment
        source .venv/bin/activate
        
        # Install dependencies
        uv pip install -r requirements.txt
        ```

    === "Using standard pip"

        ```bash
        # Create virtual environment (optional but recommended)
        python -m venv venv
        source venv/bin/activate

        # Install dependencies
        pip install -r requirements.txt
        ```

### Local Development

To preview the site locally with hot-reloading:

```bash
mkdocs serve
```

Open your browser to `http://127.0.0.1:8000`.

## Writing Content

1.  **Markdown**: All content is in `docs/`. Use standard Markdown.
2.  **Math**: Use LaTeX syntax.
    *   Inline: `\( x^2 \)`
    *   Block: `$$ E = mc^2 $$`
3.  **Code**: Use fences like normally.
    *   ```python ... ```
4.  **Admonitions**:
    ```markdown
    !!! tip "Pro Tip"
        This is a tip.
    ```

## Deployment

### GitHub Pages (Automated)

This project uses **GitHub Actions** to automatically build and deploy the site whenever you push to `main`.

1.  **Push your changes**:
    ```bash
    git add .
    git commit -m "New post"
    git push origin main
    ```
2.  **Wait**: The action will run (approx 30s) and update the `gh-pages` branch.
3.  **Config**: Ensure your repository Settings > Pages is serving from the `gh-pages` branch.

### Manual Deployment (Fallback)

If you ever need to deploy manually:

```bash
mkdocs gh-deploy
```

### Netlify / Vercel

1.  Connect your GitHub repository to Netlify/Vercel.
2.  **Build Command**: `mkdocs build`
3.  **Publish Directory**: `site`
4.  (Optional) Ensure `requirements.txt` is detected so dependencies install.

## Easter Egg

Check `docs/snippets/antigravity.py` for a classic Python nod. It is imported dynamically into the `ml/practice.md` page using the snippets extension.
