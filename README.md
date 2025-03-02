# PDFGenie - AI Chatbot for PDF File

<div style="border: 5px solid #4CAF50; padding: 15px; text-align: center; width: fit-content; margin: 20px auto;">
    <img src="botImage.png" alt="PDFGenie Bot" style="max-width: 100%; height: auto; border-radius: 10px;">
</div>




PDFGenie is an AI-powered chatbot that allows users to interact with the contents of PDF documents by asking questions. It utilizes advanced natural language processing (NLP) and machine learning models from Hugging Face to understand and respond to queries based on the content of uploaded PDF files. PDFGenie uses LangChain, FAISS, and Hugging Face transformers to process and retrieve information from PDFs in real-time.

## Features

- **PDF Text Extraction**: Extracts text from PDF files, including scanned documents.
- **Text Chunking**: Splits the extracted text into smaller, digestible chunks for efficient processing.
- **Vector Store**: Uses FAISS to index and search the text chunks quickly.
- **Question-Answering (QA)**: Uses the Mistral-7B LLM from Hugging Face to answer questions based on the PDF content.
- **Interactive Chatbot**: Users can ask questions, and the chatbot will provide answers based on the content of the uploaded PDF.

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

Additionally, you need a Hugging Face account and an API token to access the pre-trained models.
