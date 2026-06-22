Development Log

Project Name

AI Study Assistant

Objective

Build an AI-powered study assistant that extracts text from PDF files and generates MCQs and flashcards using the Gemini API.

Technologies Used

Python

Streamlit

Google Gemini API

PyPDF2

Prompt Engineering

Prompt Version 1

From the following PDF content:
{text}
Generate 10 MCQs and 10 Flashcards.
Return both sections separately.

Prompt Version 2 (Final)

From the following PDF content:
{text}
Generate:

Ten multiple-choice questions (MCQs)

Four options per question

Include the correct answer

Cover important concepts from the content

Ten flashcards

Question and Answer format

Focus on key concepts and definitions

Return the MCQs and Flashcards in separate sections with clear headings.

Improvements Made

Added structured MCQs with answer keys.

Improved flashcard quality.

Enhanced prompt clarity.

Added error handling for Gemini API failures.

Current Status

Project uploaded to GitHub and ready for deployment.
