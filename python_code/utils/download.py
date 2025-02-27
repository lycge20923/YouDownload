import argparse
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_mp4(url:str, download_path:str) -> None:

    yt = YouTube(url, on_progress_callback = on_progress)
    ys = yt.streams.get_highest_resolution()
    
    try:
        ys.download(download_path)
    except:
        os.system(f'rm "{download_path}"')
        ys.download(download_path)
    original_path = os.path.join(download_path, f"{yt.title}.mp4")
    os.system(f'mv "{original_path}" "{download_path}_temp"')
    os.system(f'rm -r "{download_path}"')
    os.system(f'mv "{download_path}"_temp "{download_path}"')

def download_mp3(url:str, download_path:str) -> None:
    yt = YouTube(url, on_progress_callback=on_progress, use_po_token=True)
    ys = yt.streams.get_audio_only()
    ys.download()
    os.system(f'mv "{yt.title}.m4a" "{download_path}"')

def addParsers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--download_path', required=True) 
    return parser






