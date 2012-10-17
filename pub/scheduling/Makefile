sched.tex: sched.rst
	pandoc sched.rst -o sched.tex --standalone

pdf: sched.tex
	pdflatex sched.tex

html: sched.rst
	pandoc --mathjax sched.rst -o sched.html --standalone


