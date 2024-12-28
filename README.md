# Youtube_Summarizer

This project allows users to summarize YouTube videos using an API built with **FastAPI**. The system downloads a video, extracts the audio, transcribes it using **Whisper**, and then summarizes the transcription with **OpenAI**.

## Requirements

To run this project, make sure you have the following dependencies installed:

- **Python 3.7+**
- **FFmpeg** (needed for audio extraction)

You can install the required Python dependencies using:

```bash
pip install -r requirements.txt
```
It also requires the command-line tool **ffmpeg** to be installed on your system, which is available from most package managers:
```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

Or you could just download FFmpeg from https://ffmpeg.org/download.html, and ensure the ffmpeg executable is in your system PATH. You can follow a guide [here](https://phoenixnap.com/kb/ffmpeg-windows ) for windows.

You can verify your installation by typing
```bash
ffmpeg -version
```
on your terminal.

## Usage

First you need to replace the line `api_key="YOUR-API-KEY"` in app.py with your own Novita API key.

Then, start the FastAPI server:

```bash
uvicorn main:app --reload
```
This will start the API server locally at http://127.0.0.1:8000.

Using the API:

Make a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the URL of the YouTube video you want to summarize:

Example request body:

```json
{
  "url": "https://www.youtube.com/watch?v=6vd3FMhX8UQ"
}
```

The API will return a summary of the transcription from the video in a JSON format.
Example response:

```json
{
  "summary": "This is a summary of the video's transcription."
}
```

You can see an example by opening **index.html** on your browser (you could drag and drop) after starting the Fastapi server.

<img width="952" alt="image" src="https://github.com/user-attachments/assets/b2272c5f-629c-402a-b197-f92e86938595" />
