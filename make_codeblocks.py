#!/usr/bin/env python3

import sys
from pathlib import Path
import argparse

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import LatexFormatter

DEFAULT_STYLE = "xcode"

def generate_latex_code(source, formatter):
    if Path(source).suffix == ".tex":
        return
    
    print(f'Processing: {source}')
    
    lexer = get_lexer_for_filename(source)

    with open(source, 'r', encoding='utf8') as file:
        code = file.read()

    highlighted_code = highlight(code, lexer, formatter)
    
    latex_file_path = Path(source).with_suffix(".tex")
    with open(latex_file_path, 'w', encoding='utf8') as latex_file:
        latex_file.write(highlighted_code)

def main():
    parser = argparse.ArgumentParser(description="Process files and display style definitions.")
    parser.add_argument("--style-defs", action="store_true", help="Display style definitions")
    parser.add_argument("--style", type=str, help="Specify a Pygments style")
    parser.add_argument("files", nargs="*", help="Files to process")

    args = parser.parse_args()

    if not args.style_defs and not args.files:
        print("required --style-defs or <FILE*> arguments")
        parser.print_help()
        sys.exit(1)

    formatter_args = {"style": args.style or DEFAULT_STYLE}
    formatter = LatexFormatter(**formatter_args)

    if args.style_defs:
        print(formatter.get_style_defs())
        sys.exit(0)

    for file in args.files:
        generate_latex_code(file, formatter)

if __name__ == "__main__":
    main()
