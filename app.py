import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
genai.configure(api_key="AQ.Ab8RN6JdlhwLcm8aA64ZFffU0p_uEXJ5QpYNVBBXDtaugTE7tg")
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Study Assistant")

st.title("📚 AI Study Assistant")

st.write("Upload your study notes and generate summaries, MCQs, flashcards, and important questions.")
from PyPDF2 import PdfReader

uploaded_file = st.file_uploader(
    "Upload your PDF Notes",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Text")
    st.text_area("PDF Content", text, height=300)
    st.subheader("Summary")

sentences = text.split(".")
summary = ".".join(sentences[:5])

st.write(summary)
st.subheader("MCQ Generator")
prompt = f"""
You are an expert teacher.

Generate 10 multiple-choice questions from the following PDF text.

For each question:
- Give 4 options.
- Give the correct answer.
- Cover important concepts from the PDF.

PDF Text:
{text}
"""
prompt = f"""
From the following content:

{text}

1. Generate 10 MCQs.
2. Generate 10 Flashcards.

Return both sections separately.
"""
try:
    response = model.generate_content(prompt)
    st.write(response.text)

except Exception as e:
    st.error("Gemini API quota exceeded. Please try again later.")



