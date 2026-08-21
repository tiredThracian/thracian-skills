#!/usr/bin/env python3
"""
Markdown to PDF Converter
Converts GitHub-Flavored Markdown into publication-grade, beautifully styled PDFs.
Uses markdown-it-py, Pygments syntax highlighting, and Playwright (Edge/Chrome).
"""

import os
import re
import sys
import argparse
import asyncio
from datetime import datetime
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from markdown_it import MarkdownIt
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer, TextLexer
from pygments.formatters import HtmlFormatter

# CSS Themes and Styles
BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

@page {
    size: A4;
    margin: 20mm 18mm 22mm 18mm;
    @bottom-right {
        content: counter(page) " / " counter(pages);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 8.5pt;
        color: #94a3b8;
    }
}

:root {
    --primary: #2563eb;
    --primary-light: #eff6ff;
    --primary-border: #bfdbfe;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --bg-main: #ffffff;
    --bg-alt: #f8fafc;
    --border-color: #e2e8f0;
    --code-bg: #f1f5f9;
    --table-header-bg: #f8fafc;
    --table-zebra: #f8fafc;
}

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.65;
    color: var(--text-main);
    background-color: var(--bg-main);
    margin: 0;
    padding: 0;
}

/* Document Header / Cover Banner */
.doc-header {
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 18px;
    margin-bottom: 26px;
}

.doc-header .doc-category {
    display: inline-block;
    font-size: 8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--primary);
    background-color: var(--primary-light);
    border: 1px solid var(--primary-border);
    padding: 3px 10px;
    border-radius: 9999px;
    margin-bottom: 10px;
}

.doc-header h1.doc-title {
    font-size: 22pt;
    font-weight: 800;
    letter-spacing: -0.025em;
    color: var(--text-main);
    margin: 6px 0 10px 0;
    line-height: 1.25;
}

.doc-header .doc-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    font-size: 8.5pt;
    color: var(--text-muted);
}

.doc-header .doc-meta span strong {
    color: #475569;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    color: #0f172a;
    font-weight: 700;
    line-height: 1.3;
    margin-top: 1.6em;
    margin-bottom: 0.6em;
    page-break-after: avoid;
    break-after: avoid;
}

h1 {
    font-size: 18pt;
    border-bottom: 1.5px solid var(--border-color);
    padding-bottom: 6px;
    margin-top: 1.8em;
}

h2 {
    font-size: 14pt;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 4px;
}

h3 { font-size: 12pt; }
h4 { font-size: 10.5pt; }
h5 { font-size: 9.5pt; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); }
h6 { font-size: 9pt; color: var(--text-muted); }

p {
    margin-top: 0;
    margin-bottom: 0.9em;
}

strong, b {
    font-weight: 600;
    color: #0f172a;
}

a {
    color: var(--primary);
    text-decoration: none;
}

/* Lists */
ul, ol {
    margin-top: 0;
    margin-bottom: 0.9em;
    padding-left: 24px;
}

li {
    margin-bottom: 0.35em;
}

li > ul, li > ol {
    margin-top: 0.35em;
    margin-bottom: 0;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.4em 0;
    font-size: 9pt;
    page-break-inside: avoid;
    break-inside: avoid;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    overflow: hidden;
}

thead {
    background-color: var(--table-header-bg);
}

th {
    padding: 9px 12px;
    font-weight: 600;
    text-align: left;
    color: #334155;
    border-bottom: 2px solid var(--border-color);
    border-right: 1px solid var(--border-color);
}

th:last-child {
    border-right: none;
}

td {
    padding: 8px 12px;
    border-bottom: 1px solid var(--border-color);
    border-right: 1px solid var(--border-color);
    color: #334155;
}

td:last-child {
    border-right: none;
}

tbody tr:nth-child(even) {
    background-color: var(--table-zebra);
}

tbody tr:last-child td {
    border-bottom: none;
}

/* Code & Syntax Highlighting */
code {
    font-family: 'JetBrains Mono', 'Fira Code', Consolas, Monaco, monospace;
    font-size: 8.5pt;
    background-color: var(--code-bg);
    color: #0f172a;
    padding: 2px 5px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
}

pre {
    font-family: 'JetBrains Mono', 'Fira Code', Consolas, Monaco, monospace;
    font-size: 8pt;
    line-height: 1.5;
    background-color: #0f172a;
    color: #f8fafc;
    padding: 14px 16px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 1.2em 0;
    page-break-inside: avoid;
    break-inside: avoid;
    border: 1px solid #1e293b;
}

pre code {
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
}

/* Callouts / GitHub-style Alerts */
.callout {
    margin: 1.2em 0;
    padding: 12px 16px;
    border-left: 4px solid var(--primary);
    border-radius: 0 6px 6px 0;
    background-color: #f8fafc;
    page-break-inside: avoid;
    break-inside: avoid;
}

.callout-title {
    font-weight: 700;
    font-size: 9pt;
    margin-bottom: 5px;
    display: flex;
    align-items: center;
    gap: 6px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.callout.callout-note {
    border-left-color: #3b82f6;
    background-color: #eff6ff;
    color: #1e40af;
}
.callout.callout-note .callout-title { color: #1d4ed8; }

.callout.callout-tip {
    border-left-color: #10b981;
    background-color: #ecfdf5;
    color: #065f46;
}
.callout.callout-tip .callout-title { color: #047857; }

.callout.callout-important {
    border-left-color: #8b5cf6;
    background-color: #f5f3ff;
    color: #5b21b6;
}
.callout.callout-important .callout-title { color: #6d28d9; }

.callout.callout-warning {
    border-left-color: #f59e0b;
    background-color: #fffbeb;
    color: #92400e;
}
.callout.callout-warning .callout-title { color: #b45309; }

.callout.callout-caution {
    border-left-color: #ef4444;
    background-color: #fef2f2;
    color: #991b1b;
}
.callout.callout-caution .callout-title { color: #b91c1c; }

.callout p:last-child {
    margin-bottom: 0;
}

/* Blockquotes */
blockquote:not(.callout) {
    margin: 1.2em 0;
    padding: 8px 16px;
    border-left: 3.5px solid #cbd5e1;
    background-color: #f8fafc;
    color: #475569;
    font-style: italic;
}

/* Horizontal Rule & Page Breaks */
hr {
    border: none;
    border-top: 1px solid var(--border-color);
    margin: 1.8em 0;
}

.page-break {
    page-break-before: always;
    break-before: page;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    margin: 1em 0;
    page-break-inside: avoid;
}
"""

THEMES = {
    "modern": {
        "primary": "#2563eb",
        "primary_light": "#eff6ff",
        "primary_border": "#bfdbfe",
        "bg_main": "#ffffff",
        "text_main": "#0f172a"
    },
    "executive": {
        "primary": "#0f766e",
        "primary_light": "#f0fdfa",
        "primary_border": "#99f6e4",
        "bg_main": "#ffffff",
        "text_main": "#111827"
    },
    "academic": {
        "primary": "#4338ca",
        "primary_light": "#eef2ff",
        "primary_border": "#c7d2fe",
        "bg_main": "#ffffff",
        "text_main": "#1e293b"
    },
    "minimal": {
        "primary": "#18181b",
        "primary_light": "#f4f4f5",
        "primary_border": "#e4e4e7",
        "bg_main": "#ffffff",
        "text_main": "#18181b"
    }
}


def parse_callouts(text: str) -> str:
    """Converts GitHub-style [!NOTE], [!TIP], etc. into styled HTML callouts."""
    pattern = r'<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)(?:<\/p>)?\s*(.*?)<\/blockquote>'
    
    icons = {
        "NOTE": "ℹ️ Note",
        "TIP": "💡 Tip",
        "IMPORTANT": "📌 Important",
        "WARNING": "⚠️ Warning",
        "CAUTION": "🛑 Caution"
    }

    def replacer(match):
        kind = match.group(1).upper()
        first_line = match.group(2).strip()
        rest = match.group(3).strip()
        label = icons.get(kind, kind.title())
        content = f"<p>{first_line}</p>" if first_line else ""
        if rest:
            content += f"\n{rest}"
        return f'<div class="callout callout-{kind.lower()}"><div class="callout-title">{label}</div>{content}</div>'

    return re.sub(pattern, replacer, text, flags=re.DOTALL | re.IGNORECASE)


def highlight_code_blocks(text: str) -> str:
    """Uses Pygments to syntax highlight markdown code blocks in HTML."""
    code_pattern = r'<pre><code class="language-([a-zA-Z0-9_-]+)">(.*?)<\/code><\/pre>'

    def replacer(match):
        lang = match.group(1).strip()
        code = match.group(2)
        # Unescape basic HTML entities in raw code
        code = code.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"')
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except Exception:
            lexer = TextLexer(stripall=True)
        
        formatter = HtmlFormatter(style="monokai", nowrap=True)
        highlighted = highlight(code, lexer, formatter)
        return f'<pre><code class="language-{lang}">{highlighted}</code></pre>'

    return re.sub(code_pattern, replacer, text, flags=re.DOTALL)


def extract_frontmatter_and_title(md_text: str):
    """Extracts YAML frontmatter or first H1 title and metadata."""
    title = None
    category = "Document"
    date_str = datetime.now().strftime("%B %d, %Y")
    author = None

    # Check for frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', md_text, flags=re.DOTALL)
    if fm_match:
        fm_content = fm_match.group(1)
        md_text = md_text[fm_match.end():]
        for line in fm_content.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip().lower()
                v = v.strip().strip('"').strip("'")
                if k in ("title", "name"):
                    title = v
                elif k in ("category", "type", "tag"):
                    category = v
                elif k in ("author", "creator"):
                    author = v
                elif k in ("date", "timestamp"):
                    date_str = v

    # Fallback to first H1 in markdown
    if not title:
        h1_match = re.search(r'^#\s+(.+)$', md_text, flags=re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
            # Remove the first H1 from markdown so it doesn't duplicate with cover header
            md_text = md_text[:h1_match.start()] + md_text[h1_match.end():]

    if not title:
        title = "Executive Summary & Documentation"

    return title, category, author, date_str, md_text


def build_html(md_text: str, theme_name: str = "modern", custom_title: str = None, custom_author: str = None, include_header: bool = True) -> str:
    """Renders markdown to fully styled HTML."""
    title, category, author, date_str, clean_md = extract_frontmatter_and_title(md_text)
    if custom_title:
        title = custom_title
    if custom_author:
        author = custom_author

    # Markdown parsing
    md_parser = MarkdownIt("commonmark").enable("table").enable("strikethrough")
    rendered_html = md_parser.render(clean_md)

    # Process callouts & syntax highlighting
    rendered_html = parse_callouts(rendered_html)
    rendered_html = highlight_code_blocks(rendered_html)

    # Replace [page-break] or <!-- pagebreak --> with div
    rendered_html = re.sub(r'<!--\s*(pagebreak|page-break)\s*-->', '<div class="page-break"></div>', rendered_html, flags=re.IGNORECASE)

    # Theme CSS overrides
    theme = THEMES.get(theme_name, THEMES["modern"])
    theme_vars = f"""
    :root {{
        --primary: {theme['primary']};
        --primary-light: {theme['primary_light']};
        --primary-border: {theme['primary_border']};
        --bg-main: {theme['bg_main']};
        --text-main: {theme['text_main']};
    }}
    """

    header_html = ""
    if include_header:
        meta_items = [f"<span><strong>Date:</strong> {date_str}</span>"]
        if author:
            meta_items.append(f"<span><strong>Author:</strong> {author}</span>")
        meta_items.append("<span><strong>Format:</strong> Markdown & PDF Dual Release</span>")

        header_html = f"""
        <div class="doc-header">
            <span class="doc-category">{category}</span>
            <h1 class="doc-title">{title}</h1>
            <div class="doc-meta">
                {' '.join(meta_items)}
            </div>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        {BASE_CSS}
        {theme_vars}
    </style>
</head>
<body>
    {header_html}
    <main>
        {rendered_html}
    </main>
</body>
</html>
"""
    return full_html


async def convert_to_pdf(html_content: str, output_pdf_path: str, landscape: bool = False):
    """Converts HTML content to PDF using Playwright (Edge/Chrome)."""
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        # Launch with system browser channel (msedge or chrome)
        browser = None
        for channel in ["msedge", "chrome"]:
            try:
                browser = await p.chromium.launch(channel=channel, headless=True)
                break
            except Exception:
                continue

        if not browser:
            # Fallback to default chromium
            browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()
        await page.set_content(html_content, wait_until="networkidle")

        pdf_options = {
            "path": output_pdf_path,
            "format": "A4",
            "landscape": landscape,
            "print_background": True,
            "display_header_footer": True,
            "header_template": '<div></div>',
            "footer_template": '''
                <div style="font-family: 'Segoe UI', Inter, sans-serif; font-size: 8pt; color: #94a3b8; width: 100%; padding: 0 18mm; display: flex; justify-content: space-between;">
                    <span>Generated with md-pdf</span>
                    <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
                </div>
            ''',
            "margin": {
                "top": "20mm",
                "bottom": "22mm",
                "left": "18mm",
                "right": "18mm"
            }
        }

        await page.pdf(**pdf_options)
        await browser.close()


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to publication-grade PDF and styled HTML.")
    parser.add_argument("input_md", help="Path to input Markdown (.md) file")
    parser.add_argument("output_pdf", nargs="?", default=None, help="Path to output PDF (.pdf) file (optional, defaults to same basename)")
    parser.add_argument("--theme", choices=["modern", "executive", "academic", "minimal"], default="modern", help="Visual styling theme")
    parser.add_argument("--title", default=None, help="Custom document title")
    parser.add_argument("--author", default=None, help="Custom author name")
    parser.add_argument("--no-header", action="store_true", help="Omit top cover banner")
    parser.add_argument("--landscape", action="store_true", help="Generate landscape PDF")
    parser.add_argument("--save-html", default=None, help="Optional path to save intermediate HTML")

    args = parser.parse_args()

    input_path = Path(args.input_md).resolve()
    if not input_path.exists():
        print(f"Error: Input markdown file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if args.output_pdf:
        output_pdf_path = Path(args.output_pdf).resolve()
    else:
        output_pdf_path = input_path.with_suffix(".pdf")

    # Ensure output directory exists
    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)

    md_content = input_path.read_text(encoding="utf-8")
    html_content = build_html(
        md_text=md_content,
        theme_name=args.theme,
        custom_title=args.title,
        custom_author=args.author,
        include_header=not args.no_header
    )

    if args.save_html:
        Path(args.save_html).write_text(html_content, encoding="utf-8")

    print(f"Converting '{input_path.name}' -> '{output_pdf_path.name}' (Theme: {args.theme})...")
    asyncio.run(convert_to_pdf(html_content, str(output_pdf_path), landscape=args.landscape))

    if output_pdf_path.exists():
        size_kb = output_pdf_path.stat().st_size / 1024
        print(f"✅ Successfully generated PDF: {output_pdf_path} ({size_kb:.1f} KB)")
    else:
        print(f"❌ Failed to generate PDF at: {output_pdf_path}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
