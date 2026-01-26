# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Personal blog of Matthew Rocklin built with MkDocs Material.

## Quick Reference

```bash
make serve    # Local dev server at http://127.0.0.1:8000
make build    # Build to site/
make clean    # Remove site/ and .cache/
```

Note: `make serve` uses `--livereload` flag to work around a Python 3.14 + Click bug.

## Architecture

**Static site generator**: MkDocs with Material theme, heavily customized.

**Key directories**:
- `docs/` - All content (markdown articles, images, CSS)
- `overrides/` - Theme customizations (templates, partials)
- `hooks/` - MkDocs Python hooks
- `layouts/` - Social card layout configuration

**Customizations**: The site uses a minimal, reading-focused design. The Material theme's header is hidden; controls (search, theme toggle, RSS) are in the sidebar instead. See `overrides/partials/nav.html` and `docs/stylesheets/custom.css`.

**Hook system**: `hooks/recent_articles.py` parses front matter from all articles and exposes `recent_articles` and `all_articles` to Jinja templates for sidebar display.

## Adding Articles

1. Create `docs/article-name.md` with front matter:
   ```yaml
   ---
   title: Article Title
   date: 2025-01-15
   tagline: Short bold text for social cards
   description: Longer description for SEO and social sharing
   ---
   ```

2. Add to `docs/articles.md` (reverse chronological order)

3. Add to `mkdocs.yml` nav under appropriate category

## Common Patterns

**Images**: Store in `docs/images/`, reference as `![](images/file.png)`

**Internal links**: Use `.md` extension: `[link text](other-article.md)`

**RSS feed**: Generated as `feed_rss_created.xml`, CI copies to `feed.xml` and `atom.xml`

## Styling

CSS is in `docs/stylesheets/custom.css`. Key design choices:
- Amber accent color (#92400e light, #d97706 dark)
- 750px max content width
- Flat sidebar navigation (no indentation)

## Writing Style

When editing or reviewing Matthew's writing:

- **Concise but human** — cut filler, but keep personality and warmth
- **No repetition** — avoid repeating words in close proximity
- **Tight structure** — front-load value; don't meander
- **No redundancy** — headers and surrounding text shouldn't repeat each other
- **Clear antecedents** — ambiguous pronouns weaken prose
- **Honest early** — acknowledge limitations upfront

## Build/Deploy

GitHub Actions deploys to GitHub Pages on push to `main`. The workflow:
1. `uv sync` - install dependencies
2. `uv run mkdocs build` - generate site
3. Copy RSS feed to `feed.xml` and `atom.xml`
4. Deploy `site/` to gh-pages branch
