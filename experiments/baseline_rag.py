import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pipeline.rag_pipeline import run_rag_pipeline

query = "What is transformer architecture?"

response = run_rag_pipeline(
    "data/raw/papers/transformer_paper.pdf",
    query
)

print(response)
