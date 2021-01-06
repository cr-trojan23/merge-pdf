import argparse
from PyPDF2 import PdfFileMerger, merger


parser = argparse.ArgumentParser(description= "Merge and compress your PDFs into a single PDF")
parser.add_argument("--file", "-f", action="store", type=str, nargs="*", help="Location of your PDF files, in the order of their placement", required=True)
args = parser.parse_args()
merger = PdfFileMerger()

for pdf in args.file:
    merger.append(pdf)
merger.write("merged_file.pdf")
merger.close()