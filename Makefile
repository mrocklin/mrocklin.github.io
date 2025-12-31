.PHONY: serve build clean

serve:
	uv run mkdocs serve --livereload

build:
	uv run mkdocs build

clean:
	rm -rf site/
