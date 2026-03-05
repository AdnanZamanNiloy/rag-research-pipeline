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

    if not results:
        return "NOT FOUND IN CONTEXT"

    context = "\n".join([doc.page_content for doc in results])

    llm = load_llm()

    prompt = build_prompt(context, query)

    response = llm.invoke(prompt)

    # The model returns the full prompt + generated text; extract only the assistant's reply.
    assistant_tag = "<|im_start|>assistant\n"
    if assistant_tag in response:
        response = response.split(assistant_tag)[-1].strip()

    # Normalize any "not found" variant the model produces into the exact expected string.
    not_found_phrases = ["not found in context", "not in the context", "not mentioned in the context", "cannot be found in the context"]
    if any(phrase in response.lower() for phrase in not_found_phrases):
        return "NOT FOUND IN CONTEXT"

    return response
