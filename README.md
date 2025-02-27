# YOUDOWNLOAD

## Purpose

* Make a youtube downloader

## Usage

### mp3/mp4

* First create a virtual environment

    * e.g. I create a name ```YoutubeDownload``` environment

* Second, create a directory, and create a file ```list.txt``` in the directory. The ```list.txt``` should be in the formate:

    ```
    website 1, name 1
    website 2, name 2
    .
    .
    .
    ```

* Finally, conduct the following command

    ```
    python main.py --list_path <the path of list.txt> --setting mp3 #mp3
    python main.py --list_path <the path of list.txt> --setting mp4 #mp4

    ```

## Notes

### Adjust ```pytube``` package

* referred to the website at https://github.com/pytube/pytube/issues/1954, we need to adjust **264th line** of ```cipher.py``` in the ```pytube``` package

    ```python
    function_patterns = [
    # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
    # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
    # var Bpa = [iha];
    # ...
    # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
    # Bpa.length || iha("")) }};
    # In the above case, `iha` is the relevant function name
    r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
    ]
    ```

