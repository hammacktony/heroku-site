import os
from pathlib import Path

from tqdm import tqdm
from webptools import webplib as webp

CONTENT_DIRECTORY = Path("../content.backup")


def main():
    paths = [path for path in CONTENT_DIRECTORY.glob("*/images/*")]

    for path in tqdm(paths):
        old_path = str(path)
        ext = old_path.split(".")[-1]
        new_path = "../static/images/covers/" + path.stem + ".webp"
        webp.cwebp(old_path, new_path, "-q 80")


if __name__ == "__main__":
    main()
