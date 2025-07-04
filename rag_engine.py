import os
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from app.config import TRANSCRIPTS_DIR, EMBEDDING_MODEL

chroma_client = chromadb.Client()
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
collection = chroma_client.create_collection(name="echoscribe", embedding_function=embedding_func)


def load_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text: str, chunk_size=500):
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks


def index_transcript(chunks):
    for i, chunk in enumerate(chunks):
        collection.add(documents=[chunk], ids=[f"chunk_{i}"])


def query_rag(prompt):
    results = collection.query(query_texts=[prompt], n_results=3)
    context = "\n---\n".join(results["documents"][0])
    return context