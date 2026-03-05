def build_prompt(context, query):

    prompt = (
        "<|im_start|>system\n"
        "You are a strict question answering assistant.\n"
        "Rules you MUST follow:\n"
        "1. Answer ONLY from the provided context below.\n"
        "2. If the context does not contain the answer, you MUST reply with exactly: NOT FOUND IN CONTEXT\n"
        "3. Do NOT guess, infer, or use any outside knowledge.\n"
        "4. Do NOT make up names, facts, or details.<|im_end|>\n"

        "<|im_start|>user\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        "Remember: if the answer is not in the context, reply exactly: NOT FOUND IN CONTEXT<|im_end|>\n"

        "<|im_start|>assistant\n"
    )

    return prompt