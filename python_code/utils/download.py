import argparse
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
import subprocess

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

def convert_m4a_to_mp3(m4a_file_path, mp3_file_path):
    
    # Adjusted command to ensure compatibility
    command = f'ffmpeg -i "{m4a_file_path}" -vn -ar 44100 -ac 2 -ab 192k -f mp3 "{mp3_file_path}"'
    try:
        subprocess.check_call(command, shell=True)
        print(f"Conversion complete: {mp3_file_path}")
    except subprocess.CalledProcessError:
        print("Failed to convert file. Ensure FFmpeg is installed and the input file path is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_mp3(url:str, download_path:str) -> None:
    yt = YouTube(url, on_progress_callback=on_progress, use_po_token=True)
    ys = yt.streams.get_audio_only()
    ys.download()
    if download_path.split('.')[-1] == "mp3":
        convert_m4a_to_mp3(f"{yt.title}.m4a", download_path)
        os.system(f'rm "{yt.title}.m4a"')
    elif download_path.split('.')[-1] == "m4a":
        os.system(f'mv "{yt.title}.m4a" "{download_path}"')
    else:
        raise ValueError("Unknown download file extention.")

def addParsers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--download_path', required=True) 
    return parser






