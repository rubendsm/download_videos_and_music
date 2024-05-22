from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import List
import uvicorn
from download_videos import download_and_merge_videos

app = FastAPI()

class VideoLinks(BaseModel):
    user_id: str = Field(..., example="user123")
    meeting_id: str = Field(..., example="12345")
    links: List[str] = Field(
        ...,
        example=[
            "https://www.youtube.com/watch?v=_31KzvrMDm8",
            "https://www.facebook.com/rubendsmoficial/videos/622660968312566"
        ]
    )

async def process_videos(user_id: str, meeting_id: str, links: List[str]):
    try:
        print(f"Processing videos for user ID: {user_id}, meeting ID: {meeting_id}")
        await download_and_merge_videos(meeting_id, links)
        print(f"Completed processing videos for user ID: {user_id}, meeting ID: {meeting_id}")
    except Exception as e:
        print(f"Error processing videos for user ID {user_id}, meeting ID {meeting_id}: {e}")

@app.post("/merge_videos/")
async def merge_videos(video_links: VideoLinks, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_videos, video_links.user_id, video_links.meeting_id, video_links.links)
    return {"message": "The videos are being downloaded and merged in the background."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
