from fastapi import FastAPI, UploadFile, Form, Request
from app.utils import download_youtube_audio, convert_to_wav
from app.transcribe import transcribe_audio
from app.rag_engine import chunk_text, index_transcript, query_rag
import os
import uuid

app = FastAPI()

@app.post("/process/")
def process_audio(youtube_url: str = Form(...)):
    audio_path = download_youtube_audio(youtube_url)
    wav_path = convert_to_wav(audio_path, audio_path.replace(".mp3", ".wav"))

    transcript_path = os.path.join("data/transcripts", os.path.basename(wav_path).replace(".wav", ".txt"))
    os.makedirs(os.path.dirname(transcript_path), exist_ok=True)

    text = transcribe_audio(wav_path)

    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(text)

    chunks = chunk_text(text)
    index_transcript(chunks)

    return {"message": "Transcription complete.", "transcript": text[:500]}

@app.post("/query/")
async def query(request: Request):
    data = await request.json()
    question = data.get("question")

    if not question:
        return {"answer": "No question provided."}

    answer = query_rag(question)
    return {"answer": answer}
