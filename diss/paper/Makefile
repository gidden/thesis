manuscript = paper
references = refs simulators benchmarks cosi
latexopt   = -halt-on-error -file-line-error

for file in $(references); do \
   ref_handles = $(ref_handles) $(file).bib \
done

all: all-via-pdf

all-via-pdf: $(manuscript).tex $(ref_handles)
	pdflatex $(latexopt) $<
	bibtex $(manuscript).aux
	pdflatex $(latexopt) $<
	pdflatex $(latexopt) $<

all-via-dvi: 
	latex $(latexopt) $(manuscript)
	bibtex $(manuscript).aux
	latex $(latexopt) $(manuscript)
	latex $(latexopt) $(manuscript)
	dvipdf $(manuscript)

epub: 
	latex $(latexopt) $(manuscript)
	bibtex $(manuscript).aux
	mk4ht htlatex $(manuscript).tex 'xhtml,charset=utf-8,pmathml' ' -cunihtf -utf8 -cvalidate'
	ebook-convert $(manuscript).html $(manuscript).epub

clean:
	rm -f *.dvi *.toc *.aux *.out *.log *.bbl *.blg *.log *.spl *~ *.spl *.zip *.idx *.lof *.lot *.acn *.glo *.ist *.epub

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
