.PHONY: compile

compile: 
	pdflatex vision.tex
	rm -f vision.aux vision.log vision.out texput.log
