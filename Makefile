all: thesis

outline:
	python src/update_outline.py
	markdown-pdf doc/OUTLINE.md
	mv doc/OUTLINE.pdf outline.pdf

thesis:
	pdflatex -output-directory=doc thesis.tex
	cp thesis.bib doc/
	cd doc && bibtex thesis.aux
	pdflatex -output-directory=doc thesis.tex
	mv doc/thesis.pdf .

clean:
	rm -rf doc/*