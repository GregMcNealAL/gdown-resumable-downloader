# Google Drive Downloader
Small python script I use to download large files google drive. Just paste a share link (must be accessible to anyone with link) and output file name.

## What script does
Converts a shareable Google Drive link and converts it to a direct download link
Downloads the file with a nice little progress bar
Wow!

## Setup
You only need gdown
```bash
pip install gdown
```

## Usage
Run script with 2 arguments:
```python
python downloader.py "https://drive.google.com/file/d/FILE_ID/view?usp=sharing" my_video.mp4
```

## Informal speed tests

These were run on the same machine and network, using the same Google Drive files.

- 2.5 GB `.mov` file  
  - Browser download: ~1 min 20 sec  
  - Script download: ~30 sec  

- 12.7 GB `.mov` file  
  - Browser download: ~6 min 45 sec  
  - Script download: ~3 min

This isn’t meant as a benchmark, just a rough comparison from real usage.