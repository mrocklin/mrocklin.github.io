# -- Project information -----------------------------------------------------

project = "Matthew Rocklin's Working Notes"
copyright = "2022, Matthew Rocklin"
author = "Matthew Rocklin"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    # "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    "README.md",
]


# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/mrocklin/",
    "twitter_url": "https://twitter.com/mrocklin",
    "search_bar_text": "Search ...",
    "navbar_end": ["search-field.html", "theme-switcher", "navbar-icon-links"],
    "page_sidebar_items": [],
    "footer_items": ["copyright"],
    "icon_links": [
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@mrocklin",
            "icon": "fa-brands fa-mastodon",
        },
        {
            "name": "Atom Feed",
            "url": "https://matthewrocklin.com/atom.xml",
            "icon": "fa-solid fa-rss"
        }
    ],
    "analytics": {"google_analytics_id": "G-ZCP1VCVST7"},
    "secondary_sidebar_items": [],

}

html_favicon = "_static/favicon.ico"
html_title = "Matthew Rocklin"
html_static_path = ["_static"]
html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html"],
    "*": ["sidebar.html"],
}
blog_baseurl = "https://matthewrocklin.com"
blog_title = "Matthew Rocklin's Working Notes"
blog_path = "."
fontawesome_included = True
blog_post_pattern = "posts/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 1
post_show_prev_next = True
blog_feed_fulltext = True
blog_authors = {
    "Matthew Rocklin": ("Matthew Rocklin", "https://matthewrocklin.com"),
}

html_extra_path = []


# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# Bibliography and citations
# bibtex_bibfiles = ["_static/works.bib"]

# OpenGraph config
ogp_site_url = "https://matthewrocklin.com"
ogp_image = "https://matthewrocklin.com/_static/profile.jpg"

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = "off"

rediraffe_redirects = {
    "startups/best-practices": "startup-best-practices",
}

def setup(app):
    app.add_css_file("custom.css")
