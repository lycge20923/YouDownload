# import from official packages
import argparse
import os

# import from self-created packages
from utils.download import download_mp3, download_mp4

def read_path_and_name(path:str, suffix:str) -> list:
    music_list = []
    with open(path, 'r') as f:
        for line in f.readlines():
            one_line = line.strip().split(", ")
            url, name = one_line[0], one_line[1]
            file_path = os.path.join(os.path.dirname(path), f"{name}.{suffix}")
            music_list.append([url, file_path])
    return music_list

def add_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list_path', required=True)
    parser.add_argument('--setting', help='Choose "mp3" or "mp4"', required=True)
    return parser

if __name__ == '__main__':
    args = add_argument().parse_args()
    music_list = read_path_and_name(args.list_path, args.setting)
    #print(music_list)
    if args.setting == "mp3":
        for url, path in music_list:
            download_mp3(url, path)
    elif args.setting == "mp4":
        for url, path in music_list:
            download_mp4(url, path)
    else:
        print("Please choose 'mp3' or 'mp4' for setting.")
    
