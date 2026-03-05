import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pipeline.rag_pipeline import run_rag_pipeline

PDF_PATH = "data/raw/papers/transformer_paper.pdf"
query = "What is transform?"

print("=" * 60)
print("  RAG PIPELINE — QUERY RESULT")
print("=" * 60)
print(f"  PDF    : {PDF_PATH}")
print(f"  Query  : {query}")
print("-" * 60)

response = run_rag_pipeline(PDF_PATH, query)

print(f"  Answer : {response}")
print("=" * 60)
