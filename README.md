# YOUDOWNLOAD

## Purpose

* Make a youtube downloader

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

