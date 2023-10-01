import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

main_placeholder = st.empty()
api_key = main_placeholder.text_input("Please insert your OpenAI API key please: ")
if api_key:

    os.environ['OPENAI_API_KEY']= api_key

    urls = []
    for i in range(3):
        url = st.sidebar.text_input(f"URL {i+1}")
        urls.append(url)

    process_url_clicked = st.sidebar.button("Process URLs")
    file_path = "faiss_store_openai.pkl"

    llm = OpenAI(temperature=0.9, max_tokens=500)

    if process_url_clicked:
        # load data
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("Data Loading...Started...✅✅✅")
        data = loader.load()
        # split data
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        docs = text_splitter.split_documents(data)
        # create embeddings and save it to FAISS index
        try:
            embeddings = OpenAIEmbeddings()
            vectorstore_openai = FAISS.from_documents(docs, embeddings)
            main_placeholder.text("Embedding Vector Started Building...✅✅✅")
            time.sleep(2)

            # Save the FAISS index to a pickle file
            with open(file_path, "wb") as f:
                pickle.dump(vectorstore_openai, f)

            query = main_placeholder.text_input("Question: ")
            if query:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f: #read binary file
                        vectorstore = pickle.load(f)
                        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
                        result = chain({"question": query}, return_only_outputs=True)
                        # result will be a dictionary of this format --> {"answer": "", "sources": [] }
                        st.header("Answer")
                        st.write(result["answer"])

                        # Display sources, if available
                        sources = result.get("sources", "")
                        if sources:
                            st.subheader("Sources:")
                            sources_list = sources.split("\n")  # Split the sources by newline
                            for source in sources_list:
                                st.write(source)
        except:
            main_placeholder.text("Incorrect API key provided.  You can find your API key at https://platform.openai.com/account/api-keys")


