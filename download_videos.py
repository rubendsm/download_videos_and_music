import os
import asyncio
from pytube import YouTube
import yt_dlp
from moviepy.editor import VideoFileClip, concatenate_videoclips

DOWNLOAD_DIR = "./downloads/"
OUTPUT_VIDEO = "./output/merged_video.mp4"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

if not os.path.exists(os.path.dirname(OUTPUT_VIDEO)):
    os.makedirs(os.path.dirname(OUTPUT_VIDEO))

async def download_video(url: str, output_dir: str) -> str:
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename

async def download_and_merge_videos(links: list) -> str:
    video_files = []
    for link in links:
        video_file = await download_video(link, DOWNLOAD_DIR)
        video_files.append(video_file)
    
    clips = [VideoFileClip(video) for video in video_files]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(OUTPUT_VIDEO)
    
    for clip in clips:
        clip.close()
    
    return OUTPUT_VIDEO
