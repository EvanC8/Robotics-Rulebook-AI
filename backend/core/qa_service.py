import google.generativeai as genai
from .vector_database import search_vector_database
from dotenv import load_dotenv
import os

# Load .env api key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model (Gemini Pro)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_response(question):
    """
    Handles all processes for answering a question
    """
    # 1. Search vector database for relevant context
    context_chunks = search_vector_database(question)
    context_str = "\n---\n".join(context_chunks)

    # 2. Create LLM prompt
    prompt = f"""
    You are an expert Q&A assistant for the FIRST Tech Challenge (FTC), a robotics competition held by the FIRST robotics organization.
    Your task is to answer questions based ONLY on the provided context from the game manual.
    If the answer cannot be found in the context, say "I cannot find the answer in the provided manual excerpts."
    
    CONTEXT: 
    {context_str}
    
    QUESTION:
    {question}
    
    ANSWER:
    """

    # 3. Send prompt to Gemini and get response
    print("Getting answer from Gemini...")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Handle potential API errors
        print(f"Error generating response from Gemini: {e}")
        return "The AI service encountered an error."