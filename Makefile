SRC_DIR := src
CODE_DIR := code

CODE_SRC := $(shell find $(CODE_DIR) -type f ! -name "*.tex")
CODE_OBJ := $(foreach s,$(CODE_SRC),$(join $(basename $(s)),.tex))
CODE_STY := $(CODE_DIR)/_style.tex

DOT_FILES := $(wildcard $(SRC_DIR)/*.dot)
DOT_PDFS := $(patsubst %.dot,%.pdf,$(DOT_FILES))

OUTPUT := build/numericka_matematika/numericka_matematika.pdf

.PHONY: build watch code_blocks code_style pdfs

build: $(OUTPUT)

pdfs: $(DOT_PDFS)
$(DOT_PDFS): %.pdf: %.dot
	dot $< -Tpdf > $@

code_style: $(CODE_STY)
$(CODE_STY):
	python ./make_codeblocks.py --style-defs > $(CODE_STY)

define CODE_template
$(1): $(2)
	python ./make_codeblocks.py $$<
endef
code_blocks: code_style $(CODE_OBJ)
$(foreach i,$(shell seq 1 $(words $(CODE_OBJ))),$(eval $(call CODE_template,$(word $(i),$(CODE_OBJ)),$(word $(i),$(CODE_SRC)))))

watch: code_blocks pdfs
	$(MAKE) build
	xdg-open $(OUTPUT) & disown
	echo "Watching for changes..."
	while true; do \
	  inotifywait -qre close_write $(SRC_DIR) $(CODE_DIR); \
	  $(MAKE) build; \
	done

$(OUTPUT): code_blocks pdfs
	tectonic -X build -p
