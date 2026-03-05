def get_retriever(vector_db, k=5):

    retriever = vector_db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": k,
            "score_threshold": 0.15  # low enough to capture relevant chunks with MiniLM
        }
    )

    return retriever