import os
import time
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub
import gradio as gr

huggingface_api_token = "*************************"

LLM_MODEL = "mistralai/Mistral-7B-Instruct-v0.1"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def extract_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text.strip() if text else "No text found. It might be a scanned document."

def process_text(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_text(text)

def initialize_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return FAISS.from_texts(chunks, embeddings)

def setup_retrieval_chain(vectorstore):
    llm = HuggingFaceHub(
        repo_id=LLM_MODEL,
        model_kwargs={"temperature": 0.3, "max_length": 512},
        huggingfacehub_api_token=huggingface_api_token
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

doc_store = {}

def chat_with_pdf(pdf_file, query):
    
    if not pdf_file:
        return "Please upload a PDF."
    if not query:
        return "Please enter a question."
    
    file_id = pdf_file.name
    if file_id not in doc_store:
        pdf_text = extract_text(pdf_file)
        if pdf_text.startswith("No text found"):
            return pdf_text
        chunks = process_text(pdf_text)
        vectorstore = initialize_vectorstore(chunks)
        qa_chain = setup_retrieval_chain(vectorstore)
        doc_store[file_id] = qa_chain
    else:
        qa_chain = doc_store[file_id]
    
    response = qa_chain.run(query)
    return response.split("Helpful Answer:")[-1].strip() 

def chat_ui(query, history, pdf):
    response = chat_with_pdf(pdf, query)
    history.append((query, response))
    return history, ""

with gr.Blocks() as ui:
    gr.Markdown("# Chat with PDF - Simple AI Chatbot")
    pdf_input = gr.File(label="Upload PDF")
    chatbot = gr.Chatbot()
    query_input = gr.Textbox(label="Ask a question", placeholder="Type your question...")
    submit_button = gr.Button("Ask")
    
    submit_button.click(chat_ui, [query_input, chatbot, pdf_input], [chatbot, query_input])

ui.launch()
