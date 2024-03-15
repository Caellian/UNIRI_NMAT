CODE_SRC := $(shell find ./code -type f ! -name "*.tex" ! -name ".gitignore")
CODE_EXT := $(suffix $(CODE_SRC))
CODE_OBJ := $(join $(basename $(CODE_SRC)),.tex)
CODE_STY := code/_style.tex

OUTPUT := build/numericka_matematika/numericka_matematika.pdf

.PHONY: build watch code_blocks code_style

build: $(OUTPUT)

src/interpolation.pdf: src/interpolation.dot
	dot src/interpolation.dot -Tpdf > src/interpolation.pdf

code_blocks: code_style $(CODE_OBJ)
code_style: $(CODE_STY)
$(CODE_STY):
	python ./make_codeblocks.py --style-defs > $(CODE_STY)

.SECONDEXPANSION:
$(CODE_OBJ): $$(addsuffix $$(CODE_EXT),$$(basename $$@))
	python ./make_codeblocks.py $<

watch: code_blocks src/interpolation.pdf
	tectonic -X watch & xdg-open $(OUTPUT)

$(OUTPUT): code_blocks src/interpolation.pdf
	tectonic -X build -p
