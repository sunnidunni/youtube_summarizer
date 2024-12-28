from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import whisper
import os
from openai import OpenAI

app = FastAPI()

# Pydantic model for the input
app.add_middleware(
    CORSMiddleware,
    # Allows all origins (use specific URLs in production)
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


class VideoSummaryRequest(BaseModel):
    url: str

# Pydantic model for the response


class VideoSummaryResponse(BaseModel):
    summary: str


@app.post("/summarize", response_model=VideoSummaryResponse)
async def summarize_video(request: VideoSummaryRequest):
    url = request.url
    audio_output = 'audio.wav'

    # Download the video using yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }
        ],
    }

    try:
        # Download audio from the URL
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Transcribe the audio using Whisper
        model = whisper.load_model("base")
        transcription = model.transcribe(audio_output)['text']

        # Summarize the transcription using OpenAI
        client = OpenAI(
            base_url="https://api.novita.ai/v3/openai",
            api_key="YOUR-API-KEY",
        )

        model_name = "meta-llama/llama-3.1-8b-instruct"
        stream = False
        max_tokens = 512

        # Request summary from OpenAI
        chat_completion_res = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "Output responses without adding 'Here's a summary of the text:'",
                },
                {
                    "role": "user",
                    "content": f"Summarize this text within 300 words: {transcription}",
                }
            ],
            stream=stream,
            max_tokens=max_tokens,
        )

        if stream:
            summary = "".join(
                chunk.choices[0].delta.content or "" for chunk in chat_completion_res)
        else:
            summary = chat_completion_res.choices[0].message.content

        # Clean up temporary files
        os.remove(audio_output)

        # Return the summary
        return VideoSummaryResponse(summary=summary)

    except Exception as e:
        # Handle any errors and return a 500 status code with the error message
        raise HTTPException(status_code=500, detail=str(e))
