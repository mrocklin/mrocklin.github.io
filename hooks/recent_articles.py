"""MkDocs hook to populate recent articles for sidebar display."""
import os
import yaml
from datetime import date

def on_env(env, config, files):
    """Add recent_articles to Jinja environment."""
    docs_dir = config['docs_dir']
    articles = []

    for f in files:
        if not f.src_path.endswith('.md'):
            continue
        if f.src_path in ('index.md', 'articles.md'):
            continue

        filepath = os.path.join(docs_dir, f.src_path)
        try:
            with open(filepath, 'r') as fp:
                content = fp.read()
            if not content.startswith('---'):
                continue
            end = content.find('---', 3)
            if end == -1:
                continue
            front_matter = yaml.safe_load(content[3:end])
            if not front_matter or 'date' not in front_matter:
                continue
            d = front_matter['date']
            if isinstance(d, str):
                d = date.fromisoformat(d)
            articles.append({
                'title': front_matter.get('title', f.src_path),
                'url': f.src_path.replace('.md', '.html'),
                'date': d,
            })
        except Exception:
            continue

    articles.sort(key=lambda x: x['date'], reverse=True)
    env.globals['recent_articles'] = articles[:5]
    return env
