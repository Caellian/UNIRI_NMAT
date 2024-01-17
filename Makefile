build: skripta.pdf

src/interpolation.pdf:
	dot src/interpolation.dot -Tpdf > src/interpolation.pdf
skripta.pdf: src/interpolation.pdf
	tectonic -X build
