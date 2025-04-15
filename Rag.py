import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain.chains import RetrievalQA
import os
# Load the document
def load_document(file_path):
    print(f"Attempting to load file: {file_path}")
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    return documents
# Initialize embeddings and vector store
def create_vector_store(documents):
    embedding = OllamaEmbeddings(model="llama3.2:1b")
    vector_store = FAISS.from_documents(documents, embedding)
    return vector_store

# Build the QA chain
def create_qa_chain(vector_store):
    llm = Ollama(model="llama3.2:1b")  # Change model if needed
    retriever = vector_store.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

# Streamlit UI
def main():
    st.title("Simple RAG Application")
    uploaded_file = st.file_uploader("Upload your text file", type=["txt"])

    if uploaded_file is not None:
        # Create a temporary file path
        temp_file_path = f"./temp_{uploaded_file.name}"

        # Save the uploaded file to the temporary path
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully!")

        documents = load_document(temp_file_path)
        vector_store = create_vector_store(documents)
        qa_chain = create_qa_chain(vector_store)

        query = st.text_input("Ask a question about the document:")
        if query:
            response = qa_chain.run(query)
            st.write("### Answer:")
            st.write(response)

        # Cleanup: Remove the temporary file
        import os
        os.remove(temp_file_path)

if __name__ == "__main__":
    main()