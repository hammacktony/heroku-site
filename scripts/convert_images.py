from webptools import webplib as webp

import cv2
import re

from pathlib import Path
from tqdm import tqdm
import os

CONTENT_DIRECTORY = Path("../content")

def main():
    paths = [path for path in CONTENT_DIRECTORY.glob("*/images/*")]

    for path in tqdm(paths):
        old_path = str(path)
        ext = old_path.split(".")[-1]
        new_path = "./images/" + path.stem + ".webp"
        webp.cwebp(old_path, new_path, "-q 80")


if __name__ == "__main__":
    main()
