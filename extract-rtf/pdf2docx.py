import streamlit as st
import PyPDF2
from io import BytesIO
from docx import Document
import base64

def convert_pdf_to_rtf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    doc = Document()
    for page in reader.pages:
        text = page.extract_text() + "\n"
        doc.add_paragraph(text)
    return doc

def get_rtf_file_download_link(doc, filename):
    """Generates a link to download the RTF file."""
    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
    b64 = base64.b64encode(file_stream.read()).decode()
    href = f'<a href="data:file/rtf;base64,{b64}" download="{filename}">Download RTF File</a>'
    return href

st.title('PDF to RTF Converter')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    doc = convert_pdf_to_rtf(uploaded_file)
    filename = uploaded_file.name + ".rtf"
    st.markdown(get_rtf_file_download_link(doc, filename), unsafe_allow_html=True)
