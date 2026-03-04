def build_prompt(context, query):

    prompt = (
        "<|im_start|>system\n"
        "You are a helpful assistant. Answer the question using only the context provided below. "
        "Be concise and accurate.<|im_end|>\n"
        "<|im_start|>user\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    return prompt
