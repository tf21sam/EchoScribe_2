import os
import uuid
from yt_dlp import YoutubeDL
import whisper  # Make sure whisper is installed: pip install openai-whisper

# Load model once
model = whisper.load_model("base")

def download_youtube_audio(youtube_url: str) -> str:
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    audio_id = str(uuid.uuid4())
    base_path = os.path.join(download_dir, audio_id)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": base_path + ".%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }],
        "quiet": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    return base_path + ".mp3"


def transcribe_audio(wav_path: str) -> str:
    result = model.transcribe(wav_path)
    return result["text"]
