import random
from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

# Free proxy list (update regularly)
PROXIES = [
    "http://103.216.82.43:6666",
    "http://45.77.201.167:3128",
    "http://94.130.9.54:3128",
    "http://176.9.75.42:3128",
    "http://128.199.202.122:8080"
]

@app.get("/transcript/{video_id}")
async def get_transcript(video_id: str):
    try:
        proxy = random.choice(PROXIES)  # Pick a random proxy
        transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies={"http": proxy, "https": proxy})
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        return {"error": str(e)}
