# TechStack — SEO Content Site

A fast, minimal GitHub Pages site for AI tools, VPS hosting, and automation guides.

## 🚀 Quick Start

### Option 1: Use as Static HTML (Recommended for SEO)

Just upload the HTML files to GitHub Pages directly:

1. Create a new repository on GitHub
2. Push this folder's contents to the `main` branch
3. Go to repository **Settings → Pages → Source**: select `main` branch
4. Your site will be live at `https://yourusername.github.io/repo-name/`

**That's it.** No Jekyll build required. Static HTML loads fastest.

### Option 2: Use with Jekyll

For Jekyll features (collections, includes, blog posts):

```bash
# Install dependencies
bundle install

# Run locally
bundle exec jekyll serve

# Build for production
bundle exec jekyll build
```

## 📁 File Structure

```
site/
├── index.html              # Homepage
├── _config.yml             # Jekyll config
├── articles/
│   ├── best-vps-ai-agents-autonomous-bots-2026.html
│   └── host-openclaw-247-setup-guide.html
├── _layouts/               # Jekyll layouts (if using Jekyll)
├── _includes/              # Jekyll includes (if using Jekyll)
├── assets/                 # CSS, JS, images (add as needed)
└── README.md               # This file
```

## 🔍 SEO Features

Each page includes:

- **Meta tags**: title, description, keywords, canonical URL
- **Open Graph**: og:title, og:description, og:type, og:url
- **Twitter Card**: twitter:card, twitter:title, twitter:description
- **Schema.org markup**: Article JSON-LD for structured data
- **Mobile responsive**: CSS Grid/Flexbox, no framework bloat
- **Performance**: Pure HTML + CSS, no JavaScript required, inline SVG favicon

## ✏️ Adding New Articles

1. Copy an existing article template from `articles/`
2. Rename the file to match the URL slug (e.g., `my-new-guide.html`)
3. Update the following in the HTML:

   - `<title>` and `<meta name="description">`
   - `og:title` and `og:description`
   - `<link rel="canonical">`
   - `article:published_time` and `article:modified_time`
   - Schema.org JSON-LD `headline` and `datePublished`
   - All internal links (logo, nav, breadcrumb)

4. Add the article to the homepage `article-grid` section

## 🌐 Custom Domain (Optional)

1. In your GitHub repo: **Settings → Pages → Custom domain**: enter `techstack.dev`
2. Add a CNAME file to the repo root (or keep `_config.yml` updated with `domain: techstack.dev`)
3. Configure your DNS provider:
   - Add `CNAME www.techstack.dev → yourgithubusername.github.io`
   - Add `ALIAS techstack.dev → yourgithubusername.github.io` (or A record to GitHub's IPs)

## 📊 Publishing Workflow

For the main agent to publish new content:

1. Generate/write article HTML
2. Place in `articles/` directory
3. Update `index.html` to include the new article in the grid
4. Commit and push to GitHub
5. GitHub Pages rebuilds automatically (~30 seconds)

## 🔒 Affiliate Disclaimers

Each article template includes a placeholder disclaimer section. Keep these — they're required by FTC guidelines when using affiliate links.

---

_Built for operators who automate._
