# AI Rulebook Q&A Bot - FIRST Robotics
This is an AI-powered Question and Answer bot for the FIRST Tech Challenge 2024-2025 _Into the Deep_ Game Manual, turning a ~150-page competition rulebook into a real-time Q&A resource.

## Usage Setup

Before running the application, you need to install the required dependencies and set up your API key.

### 1. Install Dependencies

Navigate to the `backend` folder and install all necessary Python packages using this pip command:
```bash
pip install -r requirements.txt
```

### 2. Add Your API Key

The application requires a Google AI API key to communicate with the Gemini model.

#### How to Get Your API Key
1.  Visit the official **[Google AI Studio](https://aistudio.google.com/app/apikey)** website.
2.  Generate and copy your API key to your clipboard.

#### Add the Key to Your Project
1.  Create a new file named `.env` inside the `backend` directory.
2.  Open the `.env` file and add your key in the following format:

    ```
    GOOGLE_API_KEY="paste-your-api-key-here"
    ```
The `.gitignore` file is already configured to keep this file private and secure.

## How to Run

Open two seperate terminals.

### 1. Run the Database Server

In the first terminal, run the following command to start the ChromaDB server:

```bash
chroma run --path ./chroma_data
```
### 2. Run the Application Server

In the second terminal, navigate to the `backend` folder and run the FastAPI application:
```bash
uvicorn main:app --reload
```

### 3. Test the API

Once both servers are running, you can test the API by visiting [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## How it works
This project makes use of a Retrieval-Augmented Generation (RAG) architecture to retrieve accurate answers. Here's an overview of how it all works:
1. The text is extracted from the chosen game manual pdf and is chunked into more managable segments.
2. Each chunk is converted into an embedding (vector representation) using a sentence-transformer model, which are then stored into a ChromaDB vector database.
3. When a user posts a question, the query is recieved and converted to an embedding.
4. The application searches the vector database for chunks of text that align most with the user's question.
5. The Gemini model is prompted with the user's question and the relevant manual chunks found.
6. Gemini generates a solely context-based answer and refrains from answering questions it cannot deduce an answer to from the manual chunks.

## Next steps
* Create a React.js frontend and deploy the project.
