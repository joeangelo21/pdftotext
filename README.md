# PDFToText

A high-performance Python automation utility designed for efficient raw text extraction from PDF files.

This tool is engineered to streamline the ingestion of technical literature, documentation, and research papers, converting them rapidly into clean `.txt` files optimized for data analysis, natural language processing, and AI model ingestion.

---

## Features

* **Automatic File Discovery**: Detects and lists all available PDF files in the execution directory.
* **Real-Time Progress Tracking**: Displays extraction progress page-by-page for handling large documents.
* **Robust Exception & Layout Handling**: Detects empty or image-only pages gracefully without interrupting the extraction pipeline.
* **Structured UTF-8 Output**: Produces clean text files ready for downstream data pipelines.

---

## Prerequisites & Dependencies

* Python 3.x
* `PyPDF2` library

Install required dependencies:
```bash
pip install PyPDF2

Usage
Interactive Mode

Place the script in the directory containing your PDF files and run:
Bash

python3 pdf_extractor.py

The utility will list available PDFs and prompt you for the source filename and destination text file.
Command-Line Mode
Bash

python3 pdf_extractor.py --source document.pdf --output document.txt

Author

Joelson Angelo Systems Developer

    GitHub: github.com/joeangelo21

    Website: jocecil.com.br
