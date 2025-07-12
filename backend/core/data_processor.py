import pypdf

def load_and_chunk_pdf(file_path: str) -> list[str]:
    """
    Loads text from PDF and splits into chunks by page.
    """
    print(f"Loading PDF from: {file_path}")
    pdf_reader = pypdf.PdfReader(file_path)

    chunks = []
    for i, page in enumerate(pdf_reader.pages):
        page_text = page.extract_text()
        if page_text:
            chunks.append(f"Page {i+1}: {page_text}")

    print(f"Successfully loaded and chunked {len(chunks)} pages.")
    return chunks