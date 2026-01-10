import os
import gdown
import re

def convert_share_link(link):

    match = re.search(r'/d/([a-zA-Z0-9_-]+)', link)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?id={file_id}"
    else:
        raise ValueError("Invalid Google Drive link")

def crash_safe_gdown(url, output_file):
    gdown.download(url, output_file, quiet=False, resume=True)
    print("\nDownload complete!")


if __name__ == "__main__":
    sharing_link = "PASTE YOUR SHARE LINK HERE" 

    file_url = convert_share_link(sharing_link)

    output_file = "ENTER YOUR FILENAME"

    crash_safe_gdown(file_url, output_file)
