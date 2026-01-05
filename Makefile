.PHONY: serve build clean

# Cairo library path for macOS (Homebrew)
export DYLD_FALLBACK_LIBRARY_PATH := /opt/homebrew/lib

serve:
	uv run mkdocs serve --livereload

build:
	uv run mkdocs build

clean:
	rm -rf site/
