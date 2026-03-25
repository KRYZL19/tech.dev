#!/usr/bin/env python3
"""
Fix article styles to match homepage.
Updates all article HTML files to use the warm editorial CSS.
"""
import os
import re

STYLE_BLOCK = """<style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
        --bg: #f5f0e8;
        --surface: #fffdf9;
        --border: #ddd8cf;
        --text: #1a1a18;
        --text-muted: #6b6560;
        --accent: #b5451b;
        --accent-hover: #8c3415;
        --code-bg: #e8e2d9;
    }
    body { font-family: Georgia, 'Times New Roman', serif; background: var(--bg); color: var(--text); line-height: 1.75; font-size: 17px; }
    .container { max-width: 680px; margin: 0 auto; padding: 0 1.5rem; }
    header { padding: 2rem 0; border-bottom: 1px solid var(--border); }
    .site-name { font-size: 1.1rem; font-weight: 700; color: var(--text); text-decoration: none; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .site-name:hover { color: var(--accent); }
    .back-link { font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 0.8rem; color: var(--text-muted); text-decoration: none; margin-top: 0.4rem; display: inline-block; }
    .back-link:hover { color: var(--accent); }
    .back-link::before { content: '← '; }
    .article-header { padding: 2.5rem 0 2rem; border-bottom: 1px solid var(--border); }
    .article-header h1 { font-size: 1.75rem; font-weight: 700; line-height: 1.25; margin-bottom: 0.75rem; color: var(--text); }
    .article-header .meta { font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 0.8rem; color: var(--text-muted); }
    .article-header .meta span { margin-right: 1rem; }
    .article-body { padding: 2.5rem 0; }
    .article-body h2 { font-size: 1.3rem; font-weight: 700; margin: 2rem 0 0.75rem; color: var(--text); }
    .article-body h3 { font-size: 1.1rem; font-weight: 700; margin: 1.5rem 0 0.5rem; color: var(--text); }
    .article-body p { margin-bottom: 1.1rem; }
    .article-body ul, .article-body ol { margin: 0 0 1.1rem 1.5rem; }
    .article-body li { margin-bottom: 0.4rem; }
    .article-body a { color: var(--accent); text-decoration: underline; text-underline-offset: 3px; }
    .article-body a:hover { color: var(--accent-hover); }
    pre { background: var(--code-bg); padding: 1rem 1.25rem; border-radius: 4px; overflow-x: auto; font-size: 0.85rem; line-height: 1.6; font-family: 'Courier New', Courier, monospace; margin: 1.25rem 0; border: 1px solid var(--border); }
    code { background: var(--code-bg); padding: 0.15rem 0.4rem; border-radius: 3px; font-size: 0.85em; font-family: 'Courier New', Courier, monospace; border: 1px solid var(--border); }
    pre code { background: none; padding: 0; border: none; }
    table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.9rem; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    th { background: var(--text); color: var(--surface); padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; font-size: 0.8rem; }
    td { padding: 0.6rem 0.75rem; border-bottom: 1px solid var(--border); vertical-align: top; }
    tr:nth-child(even) td { background: rgba(0,0,0,0.02); }
    blockquote { border-left: 3px solid var(--accent); padding-left: 1rem; margin: 1.5rem 0; color: var(--text-muted); font-style: italic; }
    .disclaimer { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 1rem 1.25rem; margin: 2rem 0; font-size: 0.9rem; }
    .disclaimer strong { display: block; margin-bottom: 0.25rem; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); }
    footer { border-top: 1px solid var(--border); padding: 2rem 0; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 0.8rem; color: var(--text-muted); text-align: center; }
    footer a { color: var(--text-muted); text-decoration: underline; }
    @media (max-width: 600px) { body { font-size: 16px; } .article-header h1 { font-size: 1.5rem; } table { font-size: 0.8rem; } }
</style>"""

HEADER_HTML = """    <header>
        <div class="container">
            <a href="/" class="site-name">📡 Strd's Notebook</a>
            <br><a href="/" class="back-link">Back to all notes</a>
        </div>
    </header>"""

FOOTER_HTML = """    <footer>
        <div class="container">
            <p>© 2026 strd. No rights reserved.</p>
        </div>
    </footer>"""

def fix_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace entire <style> block
    content = re.sub(r'<style>.*?</style>', STYLE_BLOCK, content, flags=re.DOTALL)
    
    # Fix header
    content = re.sub(r'<header>.*?</header>', HEADER_HTML.strip(), content, flags=re.DOTALL)
    
    # Fix footer
    content = re.sub(r'<footer>.*?</footer>', FOOTER_HTML.strip(), content, flags=re.DOTALL)
    
    # Remove inline font/color styles on body if any
    content = re.sub(r'style="[^"]*font-family[^"]*"', '', content)
    content = re.sub(r'style="[^"]*background-colors[^"]*"', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filepath}")

articles_dir = '/home/tim/.openclaw/workspace/site/articles'
for fname in os.listdir(articles_dir):
    if fname.endswith('.html') and fname != 'article-template.html':
        fix_article(os.path.join(articles_dir, fname))

print("All articles fixed!")
