import os
import asyncio
import yt_dlp

BASE_OUTPUT_DIR = "./videos/"

async def download_video(url: str, output_dir: str, format_choice: str) -> str:
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s' + format_choice),
        'format': 'best'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        return filename
    except Exception as e:
        raise Exception(f"Failed to download video from {url}: {e}")


async def download_videos(links: list, output_dir: str, format_choice: str, progress_callback) -> list:
    downloaded_files = []
    for link in links:
        try:
            filename = await download_video(link, output_dir, format_choice)
            downloaded_files.append(filename)
            progress_callback(len(downloaded_files))  # Atualiza a barra de progresso
        except Exception as e:
            print(f"Failed to download video from {link}: {e}")
    return downloaded_files
