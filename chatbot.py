# === 1. Import all necessary libraries ===
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import gradio as gr
import os

# === 2. Load the PDF document ===
# Load your training document (PDF with company knowledge)
loader = PyPDFLoader("Umma_Insurance_Training_Document.pdf")  
documents = loader.load()

# === 3. Split document into smaller chunks ===
# This improves search and understanding for LLMs
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(documents)

# === 4. Create vector embeddings from the text chunks ===
# We'll use HuggingFace's all-MiniLM-L6-v2 which is accurate and lightweight
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create or load a Chroma vector store (persisted to disk)
vectordb = Chroma.from_documents(chunks, embedding_model, persist_directory="db")
vectordb.persist()

# === 5. Load a local LLM using Ollama ===
# Make sure you've already pulled the model using: ollama pull mistral
llm = Ollama(model="tinyllama")  # You can replace "mistral" with "llama3", "openchat", etc.

# === 6. Set up Retrieval-Augmented QA chain ===
# This links the LLM with your vector database for context-aware answers
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True  # Helpful for debugging or showing which doc was used
)

# === 7. Define chatbot logic ===
# If the user's query is not found in company docs, fallback to general model knowledge
def smart_chatbot(query):
    result = qa_chain(query)
    
    # If no relevant chunks were found in the company documents
    if not result['source_documents']:
        return llm(query)  # Use LLM's general knowledge (e.g., what is insurance)
    
    return result["result"]

# === 8. Create a web UI using Gradio ===
# This can be hosted locally or shared as a web app
gr.Interface(
    fn=smart_chatbot,
    inputs="text",
    outputs="text",
    title="Umma Insurance AI Chatbot",
    description="Ask any question related to Umma Insurance policies or general insurance topics."
).launch()

