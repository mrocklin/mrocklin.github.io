partial-orders.tex: partial-orders.md
	pandoc partial-orders.md -o partial-orders.tex --standalone

pdf: partial-orders.tex mpi-po.pdf comp-comm.pdf
	pdflatex partial-orders.tex

html: partial-orders.md mpi-po.png comp-comm.png
	cat partial-orders.md | \
		sed -e 's/\.pdf)/.png)/' | \
		pandoc --mathjax -o partial-orders.html --standalone

mpi-po.pdf: mpi-po.dot
	dot -Tpdf mpi-po.dot -o mpi-po.pdf
mpi-po.png: mpi-po.dot
	dot -Tpng mpi-po.dot -o mpi-po.png
comp-comm.pdf: comp-comm.dot
	dot -Tpdf comp-comm.dot -o comp-comm.pdf
comp-comm.png: comp-comm.dot
	dot -Tpng comp-comm.dot -o comp-comm.png
