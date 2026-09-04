from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()
embedd = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-0.6B"

)

docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

vector_store = FAISS.from_documents(
    documents=docs, 
    embedding=embedd
)

res = vector_store.as_retriever(
    search_type='mmr',
    k=2,
    lambda_mult=0.4 
)

print(res)