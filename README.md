🧠 Step 1 – Input the YouTube Link
You give my app a YouTube URL like:
https://www.youtube.com/watch?v=cgOPg5cCr2g

🎧 Step 2 – It downloads the audio
Behind the scenes, a ninja tool called yt_dlp grabs just the audio part (like a quiet audio thief).

🎵 Step 3 – Converts it to WAV
Because Whisper prefers WAV like it's 2010, we use pydub to convert the MP3 into a WAV. Think of it like… giving Whisper its favorite snack.

🗣️ Step 4 – Whisper Transcribes it
Now Whisper (the ASR model, not your nosy neighbor) listens to the audio and writes it all down in plain text.

📚 Step 5 – We chunk it like Netflix subtitles
The text is split into small 500-word pieces, so our memory doesn’t explode later.

🧠 Step 6 – We store it smartly using ChromaDB
Chroma stores all those chunks in vector format (basically, numerical magic).

🤖 Step 7 – Ask it anything
You ask a question like “What is GitHub?” and boom! It finds the most relevant parts of the transcript and gives you an answer like a very focused intern who actually watched the video.



🛠️ What Tech Is Used?

    FastAPI — Our backend boss.

    Streamlit — For the smooth user interface.

    Whisper — The transcription hero.

    ChromaDB + SentenceTransformers — For embeddings & search.

    yt_dlp + ffmpeg + pydub — The media mafia.
