#!/usr/bin/env python3
"""pdf_extractor.py - High-efficiency robust PDF text extraction utility.

Scans the local directory for PDF files, extracts raw text page-by-page with
progress tracking, handles image-only or empty pages gracefully, and outputs clean UTF-8 text.
"""
import os
import sys
import argparse
import PyPDF2

def list_pdf_files():
    """List all .pdf files in the current working directory and prompt user selection."""
    files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    if not files:
        print("[-] No PDF files found in the current directory.")
        return None, None

    print("\n--- Available PDF Files ---")
    for f in files:
        print(f"-> {f}")

    source = input("\nEnter the name of the PDF file to extract: ").strip()
    if source not in files:
        print(f"[-] Error: File '{source}' not found.")
        return None, None

    destination = input("Enter the destination text file name (.txt): ").strip()
    if not destination:
        destination = os.path.splitext(source)[0] + ".txt"
    elif not destination.lower().endswith('.txt'):
        destination += ".txt"

    return source, destination

def extract_pdf_text(source, destination):
    """Extract text content page by page from a source PDF to a destination text file."""
    print(f"\n[!] Initializing extraction: {source} -> {destination}")
    try:
        with open(source, 'rb') as file_obj:
            reader = PyPDF2.PdfReader(file_obj)
            total_pages = len(reader.pages)

            with open(destination, 'w', encoding='utf-8') as out:
                for i in range(total_pages):
                    page = reader.pages[i]
                    text = page.extract_text()

                    if text and text.strip():
                        out.write(text + "\n\n")
                    else:
                        out.write(f"\n--- [Page {i+1} empty or contains only images] ---\n\n")

                    print(f"Processing: {i+1}/{total_pages} pages...", end="\r", flush=True)

        print(f"\n[+] Success! Output successfully saved to '{destination}'.")

    except Exception as e:
        print(f"\n[-] Critical error during extraction: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="PDFToText - Efficient Raw Text Extraction Utility")
    parser.add_argument("--source", help="Path to the source PDF file")
    parser.add_argument("--output", help="Path to the destination text file (.txt)")
    args = parser.parse_args()

    source = args.source
    destination = args.output

    if not source or not destination:
        source, destination = list_pdf_files()

    if source and destination:
        extract_pdf_text(source, destination)

if __name__ == '__main__':
    main()
