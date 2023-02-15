from pytube import YouTube

from pytube import YouTube
import json


def lambda_handler(event, context):
    if body_content := event.get("body"):
        body_content = json.loads(body_content)
        if data := body_content.get("video_url"):
            print(data)
            yt = YouTube(data)
            return {
                "url": data,
                "duration": f"{yt.length} seconds",
                "thumbnail_url": yt.thumbnail_url
            }
    return {"message": "No url given"}


