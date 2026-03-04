from src.loaders.pdf_loader import load_pdf
from src.chunking.text_splitter import split_documents
from src.embeddings.embedding_model import load_embedding_model
from src.vectordb.faiss_store import create_vector_store
from src.retrieval.retriever import get_retriever
from src.llm.llm_model import load_llm
from src.utils.prompt_template import build_prompt


def run_rag_pipeline(pdf_path, query):

    documents = load_pdf(pdf_path)

    chunks = split_documents(documents)

    embeddings = load_embedding_model()

    vector_db = create_vector_store(chunks, embeddings)

    retriever = get_retriever(vector_db)

    results = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in results])

    llm = load_llm()

    prompt = build_prompt(context, query)

    response = llm.invoke(prompt)

    return response
