from openai import OpenAI
import moviepy as mp
import yt_dlp
import speech_recognition as sr


url = 'https://www.youtube.com/watch?v=6vd3FMhX8UQ&ab_channel=StevenBridges'


output = 'vid_cache.mp4'

ydl_opts = {
    'format': 'best',
    'outtmpl': output,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

video = mp.VideoFileClip(output)

audio = video.audio
audio.write_audiofile("audio.wav")

print(text)

# client = OpenAI(
#     base_url="https://api.novita.ai/v3/openai",
#     # Get the Novita AI API Key by referring to: https://novita.ai/docs/get-started/quickstart.html#_2-manage-api-key.
#     api_key="ee0ea824-15e9-4571-9084-4f6047b7948c",
# )

# model = "meta-llama/llama-3.1-8b-instruct"
# stream = True  # or False
# max_tokens = 512
# text = 'Climate change is a significant global issue affecting ecosystems, human populations, and economies worldwide. Rising temperatures, caused by increased greenhouse gas emissions, lead to phenomena such as melting polar ice caps, rising sea levels, and more frequent extreme weather events. These changes disrupt agriculture, threaten biodiversity, and pose risks to human health through heatwaves and the spread of diseases. Addressing climate change requires international cooperation, transitioning to renewable energy sources, improving energy efficiency, and implementing sustainable land use practices to reduce carbon footprints and adapt to changing conditions.'
# chat_completion_res = client.chat.completions.create(
#     model=model,
#     messages=[
#         {
#             "role": "system",
#             "content": "Output responses without adding 'Here's a summary of the text:'",
#         },
#         {
#             "role": "user",
#             "content": f"Summarize this text: {text}",
#         }
#     ],
#     stream=stream,
#     max_tokens=max_tokens,
# )

# if stream:
#     for chunk in chat_completion_res:
#         print(chunk.choices[0].delta.content or "", end="")
# else:
#     print(chat_completion_res.choices[0].message.content)
