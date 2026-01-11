import sys
import gdown
import re

def convert_share_link(link):
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', link)
    if match:
        return f"https://drive.google.com/uc?id={match.group(1)}"
    raise ValueError("Invalid Google Drive link")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python downloader.py <share_link> <output_file>")
        sys.exit(1)

    sharing_link = sys.argv[1]
    output_file = sys.argv[2]

    file_url = convert_share_link(sharing_link)
    gdown.download(file_url, output_file, quiet=False, resume=True)
    print("\nDownload complete!")
