from fastapi import FastAPI
from pydantic import BaseModel

from core.data_processor import load_and_chunk_pdf
from core.vector_database import populate_vector_database
from core.qa_service import get_ai_response

# Run ChromaDB server: chroma run --path ./chroma_data
# Run FastAPI server: uvicorn main:app --reload
app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    """
    Load PDF and populate database on server start
    """
    pdf_path = "../data/ftc_manual_2024-2025.pdf"
    chunks = load_and_chunk_pdf(pdf_path)
    populate_vector_database(chunks)

@app.get("/")
def read_root():
    return {"status": "FTC Q&A Bot with Gemini is running!"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    """
    Main endpoint for asking a question
    """
    answer = get_ai_response(request.question)
    return {"question": request.question, "answer": answer}