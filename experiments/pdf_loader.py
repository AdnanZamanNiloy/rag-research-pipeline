"""
PDF Loader Module
Handles loading and extracting text from PDF documents using LangChain.
"""

from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """Loads PDF documents and extracts their text content via LangChain's PyPDFLoader."""

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"PDF file not found: {self.file_path}")
        self._loader = PyPDFLoader(str(self.file_path))

    def load(self) -> List[Document]:
        """
        Load PDF and return a list of LangChain Document objects (one per page).

        Returns:
            List of Document objects with page_content and metadata.
        """
        return self._loader.load()

    def load_as_single_document(self) -> Document:
        """
        Load all pages and merge into a single LangChain Document.

        Returns:
            Single Document with combined page_content.
        """
        pages = self.load()
        full_text = "\n\n".join(p.page_content for p in pages)
        return Document(
            page_content=full_text,
            metadata={
                "source": str(self.file_path),
                "total_pages": len(pages),
            },
        )


if __name__ == "__main__":
    loader = PDFLoader("data/raw/papers/transformer_paper.pdf")
    docs = loader.load()
    print(f"Loaded {len(docs)} pages.")
    print(docs[0].page_content[:500])
    print(docs[0].metadata)
