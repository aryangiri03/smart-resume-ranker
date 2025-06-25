import PyPDF2
import io

def parse_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        return uploaded_file.read().decode("utf-8", errors="ignore") 