manuscript = pres
references = pres
latexopt   = --pdf --clean --verbose --batch

all: all-via-dvi

all-via-pdf: $(manuscript).tex $(references).bib
	pdflatex $(latexopt) $<
	bibtex $(manuscript $<).aux
	pdflatex $(latexopt) $<
	pdflatex $(latexopt) $<

all-via-dvi: $(manuscript).tex $(references).bib
	texi2dvi $(latexopt) $(manuscript).tex
	-bibtex $(manuscript)
	texi2dvi $(latexopt) $(manuscript).tex
	texi2dvi $(latexopt) $(manuscript).tex

clean:
	rm -f *.dvi *.toc *.aux *.out *.log *.bbl *.blg *.log *.spl *~ *.spl *.zip *.nav *.snm 

realclean: clean
	rm -rf $(manuscript).dvi
	rm -f $(manuscript).pdf

%.ps :%.eps
	convert $< $@

%.png :%.eps
	convert $< $@

zip:
	zip paper.zip *.tex *.eps *.bib

.PHONY: all clean
