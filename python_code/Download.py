from pytube import YouTube
import argparse

def download_mp4(url:str, downloadpath:str) -> None:
    pass

def download_mp3(url:str, downloadpath:str) -> None:
    yt = YouTube(url)
    yt.streams.filter().get_audio_only().download(filename=downloadpath)

def main(url:str, downloadpath:str, type:str) -> None:
    yt = YouTube(url)
    if type == 'mp3':
        download_mp3(url, downloadpath)
    elif type == 'mp4':
        download_mp4(url, downloadpath)

def addParsers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--downloadpath', required=True) 
    return parser


if __name__ == '__main__':
    pars = addParsers().parse_args()
    download_mp3(pars.url, pars.downloadpath)





