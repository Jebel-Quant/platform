.PHONY: compile

compile:
	pdflatex vision.tex
	pdflatex vision.tex
	rm -f vision.aux vision.log vision.out texput.log
