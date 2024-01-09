import streamlit as st
import PyPDF2
import base64
from io import BytesIO

def convert_pdf_to_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def get_text_file_download_link(text, filename, text_button="Download Text File"):
    """Generates a link to download the text file."""
    try:
        # Ensure text is properly encoded for base64
        b64 = base64.b64encode(text.encode('utf-8')).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text_button}</a>'
        return href
    except Exception as e:
        return f"Error in file encoding: {e}"

st.title('PDF to Text Converter')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    text = convert_pdf_to_text(uploaded_file)
    st.text_area("Text", text, height=300)
    filename = uploaded_file.name + ".txt"
    st.markdown(get_text_file_download_link(text, filename), unsafe_allow_html=True)