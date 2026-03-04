def build_prompt(context, query):

    prompt = (
        "<|system|>\n"
        "You are a helpful assistant. Answer the question using only the context provided below. "
        "Be concise and accurate.\n"
        "</s>\n"
        "<|user|>\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        "</s>\n"
        "<|assistant|>\n"
    )

    return prompt
