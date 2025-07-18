from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def format_docs(docs):
    if not docs:
        return "I don't know."
    return "\n\n".join(doc.page_content for doc in docs)


# Load vectorstore from chromadb from step 1
vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="demo.db",
    collection_name="demo_web"
)

query = "RAG คืออะไร"

# Re-ranking the documents
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import FlashrankRerank

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
compressor = FlashrankRerank(model="ms-marco-MiniLM-L-12-v2")
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)

print("2. Re-ranking the documents...")
compressed_docs = compression_retriever.invoke(query)
print("Compressed docs: ", len(compressed_docs))
for doc in compressed_docs:
    doc_details = doc.to_json()['kwargs']
    print("ID: ", doc_details['metadata']['id'])
    print("Source: ", doc_details['metadata']['source'])
    formatted_text = format_docs([doc])
    print("Text: ", formatted_text)
    print("================\n")