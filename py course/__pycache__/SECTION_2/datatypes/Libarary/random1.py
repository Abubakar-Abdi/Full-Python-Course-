from pypdf import PdfReader

def akhri(file):
    reader=PdfReader(file)
    print(f"number of pages {reader.pages[0].extract_text}")
akhri(r"C:\Users\hp\Downloads\modified resume.pdf")