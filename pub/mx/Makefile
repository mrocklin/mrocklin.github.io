mx.tex: mx.rst
	pandoc mx.rst -o mx.tex --standalone

pdf: mx.tex
	pdflatex mx.tex

html: mx.rst
	pandoc --mathjax mx.rst -o mx.html --standalone


