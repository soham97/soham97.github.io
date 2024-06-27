#!/bin/bash
python generate.py cv > cv/publication_list.tex
python generate.py html > publications-generated.html

cd cv/
pdflatex Fried-CV-web.tex
./to_html.sh
