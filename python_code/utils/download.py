from pytube import YouTube
import argparse
import os
from pytubefix import YouTube as YouTube_ver2
from pytubefix.cli import on_progress

def download_mp4(url:str, download_path:str) -> None:

    yt = YouTube_ver2(url, on_progress_callback = on_progress)
    ys = yt.streams.get_highest_resolution()
    
    try:
        ys.download(download_path)
    except:
        os.system(f'rm "{download_path}"')
        ys.download(download_path)
    original_path = os.path.join(download_path,os.path.basename(download_path))
    os.system(f'mv "{original_path}" "{download_path}"_temp')
    os.system(f'rm -r "{download_path}"')
    os.system(f'mv "{download_path}"_temp "{download_path}"')

def adjust_MPEG3(filepath:str) -> None:

    #move the file to the temp directory
    temp_folder_name = os.path.join(os.path.dirname(filepath), 'temp')
    temp_file_name = os.path.join(temp_folder_name, os.path.basename(filepath))
    
    cmd1 = f"mkdir '{temp_folder_name}'"
    cmd2 = f"mv '{filepath}' '{temp_file_name}'"
    cmd3 = f"ffmpeg -i '{temp_file_name}' -vn -ar 44100 -ac 2 -b:a 192k '{filepath}'"
    cmd4 = f"rm -r '{temp_folder_name}'"
    cmds = [cmd1, cmd2, cmd3, cmd4]
    for cmd in cmds:
        try:
            os.system(cmd)
        except Exception as e:
            print(e)
            break

def download_mp3(url:str, download_path:str) -> None:
    yt = YouTube(url)
    yt.streams.filter(file_extension='mp4').get_audio_only().download(filename=download_path)
    adjust_MPEG3(download_path)

def addParsers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--download_path', required=True) 
    return parser






