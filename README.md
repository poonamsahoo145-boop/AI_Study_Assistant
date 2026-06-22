AI Study Assistant

Introduction

AI Study Assistant is an intelligent learning application developed using Python, Streamlit, and Google Gemini API. The application helps students learn more effectively by automatically generating summaries, flashcards, multiple-choice questions (MCQs), and answers from uploaded PDF documents.

Problem Statement

Students often spend a significant amount of time reading lengthy study materials and preparing notes. This project aims to simplify the learning process by automatically extracting important information from PDF documents and presenting it in an easy-to-understand format.

Objectives

- Automate study material analysis.
- Generate concise summaries from PDF content.
- Create MCQs for self-assessment.
- Generate flashcards for quick revision.
- Answer user questions based on PDF content.

Features

1. PDF Upload

Users can upload PDF documents containing study material.

2. Text Extraction

The system extracts text from the uploaded PDF for further processing.

3. Summary Generation

The Gemini API generates a concise summary of the uploaded document.

4. MCQ Generation

The system generates multiple-choice questions from the PDF content to support exam preparation.

5. Flashcard Generation

Important concepts and definitions are converted into flashcards for quick learning.

6. Question Answering

Users can ask questions related to the uploaded document, and the application provides answers based on the PDF content.

Technology Stack

Frontend

- Streamlit

Backend

- Python

AI Model

- Google Gemini API

Development Tools

- VS Code
- GitHub

Project Architecture

1. User uploads PDF.
2. PDF text is extracted.
3. Extracted content is sent to Gemini API.
4. Gemini generates summaries, MCQs, flashcards, and answers.
5. Results are displayed through the Streamlit interface.

Installation

Clone Repository

git clone YOUR_GITHUB_REPOSITORY_LINK

Install Dependencies

pip install -r requirements.txt

Run Application

streamlit run app.py

Project Workflow

1. Launch the application.
2. Upload a PDF document.
3. Generate summary.
4. Generate MCQs.
5. Generate flashcards.
6. Ask questions related to the PDF.

Challenges Faced

- API quota limitations during testing.
- Handling PDF text extraction.
- Designing effective prompts for Gemini API.
- Debugging Streamlit integration issues.

Learning Outcomes

- Python programming.
- Streamlit application development.
- AI application development using Gemini SDK.
- Prompt engineering.
- GitHub repository management.

Future Scope

- Multi-language support.
- Voice-based interaction.
- User authentication.
- Export summaries and notes as PDF.
- Advanced analytics for learning performance.

Author

Poonam Sahoo

License

This project is created for educational and academic purposes.
