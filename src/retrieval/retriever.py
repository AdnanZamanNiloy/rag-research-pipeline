def get_retriever(vector_db, k=3):

    retriever = vector_db.as_retriever(search_kwargs={"k": k})

    return retriever
