.PHONY: serve build

serve:
	uv run mkdocs serve --livereload

build:
	uv run mkdocs build
