import streamlit as st
import pdf2txt

# Function to convert PDF to text
def convert_pdf_to_text(pdf_file):
    # Convert PDF to text using pdf2txt library
    text = pdf2txt.convert(pdf_file)
    return text

# Streamlit app
def main():
    st.title("PDF to Text Converter")

    # Prompt user for PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

    if pdf_file is not None:
        # Convert PDF to text
        text = convert_pdf_to_text(pdf_file)

        # Save text to a text file
        text_file = st.text_input("Enter the name of the text file")
        if st.button("Save as Text"):
            with open(text_file, "w") as file:
                file.write(text)
            st.success(f"Text file saved as {text_file}")

if __name__ == "__main__":
    main()
