import os
import asyncio
import yt_dlp
from moviepy.editor import VideoFileClip, concatenate_videoclips

BASE_OUTPUT_DIR = "./videos/"

async def download_video(url: str, output_dir: str) -> str:
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'best'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        return filename
    except Exception as e:
        raise Exception(f"Failed to download video from {url}: {e}")

async def download_and_merge_videos(meeting_id: str, links: list) -> str:
    output_dir = os.path.join(BASE_OUTPUT_DIR, meeting_id)
    output_path = os.path.join(output_dir, 'video.mp4')

    # Create directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    video_files = []
    for link in links:
        video_file = await download_video(link, output_dir)
        video_files.append(video_file)
    
    clips = [VideoFileClip(video) for video in video_files]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path)
    
    for clip in clips:
        clip.close()
    
    # Remove the downloaded video files
    for video_file in video_files:
        os.remove(video_file)
    
    return output_path
