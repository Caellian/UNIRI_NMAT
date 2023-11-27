build: skripta.pdf

CODEBLOCKS := $(wildcard ./src/codeblocks/*)

src/_pygments.tex:
	./make_codeblocks.py --style-defs > src/_pygments.tex
src/codeblocks/*.tex:
	./make_codeblocks.py $(CODEBLOCKS)
src/interpolation.pdf:
	dot src/interpolation.dot -Tpdf > src/interpolation.pdf
skripta.pdf: src/interpolation.pdf src/_pygments.tex src/codeblocks/*.tex
	tectonic -X build
