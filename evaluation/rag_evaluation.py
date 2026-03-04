from src.pipeline.rag_pipeline import run_rag_pipeline


def evaluate_rag(test_cases):
    """
    Evaluate the RAG pipeline on a list of test cases.

    Each test case is a dict with:
        - pdf_path: str
        - query: str
        - expected_keywords: list of str (used for simple keyword overlap scoring)
    """
    results = []

    for i, case in enumerate(test_cases):
        pdf_path = case["pdf_path"]
        query = case["query"]
        expected_keywords = case.get("expected_keywords", [])

        print(f"\n[Test {i + 1}] Query: {query}")

        response = run_rag_pipeline(pdf_path, query)

        # Simple keyword overlap score
        matched = [kw for kw in expected_keywords if kw.lower() in response.lower()]
        score = len(matched) / len(expected_keywords) if expected_keywords else 0.0

        print(f"Response: {response[:300]}...")
        print(f"Keyword Match Score: {score:.2f} ({len(matched)}/{len(expected_keywords)})")

        results.append({
            "query": query,
            "response": response,
            "score": score,
            "matched_keywords": matched,
        })

    return results


if __name__ == "__main__":
    test_cases = [
        {
            "pdf_path": "data/raw/papers/transformer_paper.pdf",
            "query": "What is the transformer architecture?",
            "expected_keywords": ["attention", "encoder", "decoder", "self-attention"],
        },
        {
            "pdf_path": "data/raw/papers/transformer_paper.pdf",
            "query": "What is multi-head attention?",
            "expected_keywords": ["heads", "attention", "parallel", "queries", "keys", "values"],
        },
    ]

    results = evaluate_rag(test_cases)

    avg_score = sum(r["score"] for r in results) / len(results)
    print(f"\nAverage Keyword Match Score: {avg_score:.2f}")
