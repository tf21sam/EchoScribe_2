import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(ROOT_DIR, "data")
TRANSCRIPTS_DIR = os.path.join(DATA_DIR, "transcripts")
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
