# PDFGenie - AI Chatbot for PDF Files

<div style="border: 10px solid #4CAF50; padding: 20px; text-align: center; width: fit-content; margin: 20px auto; background: linear-gradient(to right, #f0f0f0, #e0e0e0); border-radius: 15px; box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);">
    <img src="botImage.png" alt="PDFGenie Bot" style="max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);">
</div>

PDFGenie is an AI-powered chatbot that allows users to interact with the contents of PDF documents by asking questions. It utilizes advanced natural language processing (NLP) and machine learning models from **Hugging Face** to understand and respond to queries based on the uploaded PDF. PDFGenie uses **LangChain**, **FAISS**, and **Hugging Face** transformers to process and retrieve information from PDFs in real-time.

---

## Features

- **PDF Text Extraction**: Extracts text from PDF files, including scanned documents.
- **Text Chunking**: Splits extracted text into smaller, digestible chunks for efficient processing.
- **Vector Store**: Uses **FAISS** for indexing and fast search of the text chunks.
- **Question-Answering**: Uses **Mistral-7B** from **Hugging Face** for providing answers to user queries based on the PDF content.
- **Interactive Chatbot**: Users can ask any questions related to the PDF, and the bot will respond with contextually relevant answers.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.7 or higher**
- **pip** (Python package manager)

Additionally, you will need a **Hugging Face** account and an API token to access the pre-trained models.

---
