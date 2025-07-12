import chromadb
from chromadb.utils import embedding_functions

# Initialize local embedding model
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Initialize ChromaDB client
#client = chromadb.Client()
client = chromadb.HttpClient(host='localhost', port=8000)

# Create collection for FTC Competition Manual 2024-2025 INTO THE DEEP
ftc_collection = client.get_or_create_collection(
    name="ftc_manual_2024-2025",
    embedding_function=sentence_transformer_ef,
)

def populate_vector_database(chunks):
    """
    Stores chunks in ChromaDB
    """
    print("Storing chunks in vector database...")
    ftc_collection.add(
        documents=chunks,
        ids=[str(i) for i in range(len(chunks))]
    )
    print("Successfully stored chunks.")

def search_vector_database(query, n_results=5):
    """
    Searches database for most relevant chunks for a given query
    """
    print(f"Searching vector database for query: {query}...")
    results = ftc_collection.query(
        query_texts=[query],
        n_results=n_results
    )
    print("Received results.")
    return results['documents'][0]

