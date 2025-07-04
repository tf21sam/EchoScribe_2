import yt_dlp
import os
from pydub import AudioSegment
from app.config import DATA_DIR


def download_youtube_audio(url: str, output_path="downloads/audio.mp3"):
    # Remove .mp3 if already present to avoid .mp3.mp3
    base_output = output_path.replace(".mp3", "")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': base_output,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    final_output = base_output + ".mp3"
    return final_output


def convert_to_wav(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Audio file not found: {input_path}")
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path
