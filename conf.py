# -- Project information -----------------------------------------------------

project = 'Matthew Rocklin'
copyright = '2022, Matthew Rocklin'
author = 'Matthew Rocklin'

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    # "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*", "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md"]


# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/mrocklin/",
  "twitter_url": "https://twitter.com/mrocklin",
  "search_bar_text": "Search ...",
  "google_analytics_id": "",
  "navbar_end": ["search-field.html", "theme-switcher", "navbar-icon-links"],
  "page_sidebar_items": [],
  "footer_items": ["copyright"],
}

html_favicon = "_static/favicon.ico"
html_title = "Matthew Rocklin"
html_static_path = ['_static']
html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "publications": ["sidebar-nav-bs.html"],
    "projects": ["hello.html"],
    "talks": ["hello.html"],
    "posts/*": ['postcard.html', 'recentposts.html'],
    "blog": ['tagcloud.html'],
    "blog/**": ['postcard.html', 'recentposts.html']
}
blog_baseurl = "https://matthewrocklin.com"
blog_title = "Working Notes"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

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
# ogp_site_url = "https://predictablynoisy.com"
# ogp_image = "https://predictablynoisy.com/_static/profile-bw.png"

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = "off"

rediraffe_redirects = {
      # "blog/work/2022/07/25/startup-revenue": "posts/startup-revenue.md",
}
for k, v in list(rediraffe_redirects.items()):
    rediraffe_redirects[k + ".html"] = v

def setup(app):
    app.add_css_file("custom.css")
