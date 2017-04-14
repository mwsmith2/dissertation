all:
	pdflatex -output-directory=doc thesis.tex
	mv doc/thesis.pdf .

clean:
	rm -rf doc/*