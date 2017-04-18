all:
	pdflatex -output-directory=doc thesis.tex
	cp thesis.bib doc/
	cd doc && bibtex thesis.aux
	pdflatex -output-directory=doc thesis.tex
	mv doc/thesis.pdf .

clean:
	rm -rf doc/*