import os.path

from pypdf import PdfReader

reader = PdfReader("tmp/test_design.pdf")

print(reader.pages)
print(len(reader.pages))

print(reader.pages[0].extract_text())

print(os.path.getsize("tmp/test_design.pdf"))
assert os.path.getsize("tmp/test_design.pdf") == 174575
