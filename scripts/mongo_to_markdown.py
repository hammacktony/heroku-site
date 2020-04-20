import os
import shutil
from pathlib import Path
from typing import Any, Dict, List

from jinja2 import Template

import boto3
import pymongo
from dotenv import load_dotenv
from slugify import slugify
from tqdm import tqdm

load_dotenv()

TEMPLATE_PATH = Path("./template.txt")
S3_BUCKET = os.getenv("S3_BUCKET", "")
S3_BUCKET_URL = os.getenv("S3_BUCKET_URL", "")

s3 = boto3.client("s3")


def get_template(template_path: Path) -> Template:
    with open(template_path, "r") as f:
        data = f.read().strip()
    return Template(data)


def get_config():
    """ Get Mongo Config Information """

    return {
        "host": os.getenv("MONGO_HOST"),
        "port": int(os.getenv("MONGO_PORT")),
        "username": os.getenv("MONGO_USER"),
        "password": os.getenv("MONGO_PWD"),
        "db": os.getenv("MONGO_DB"),
    }


def extract_article(post: Dict[str, Any]):
    title = post["title"]
    body = post["body"]
    tags = post["category"].split(",")
    date = post["updated_at"].split(" ")[0]
    image = S3_BUCKET_URL + post["image"]
    return (title, tags, date, body, image)


def save_output(output: str, title: str, date: str, download_images: bool = False) -> Path:
    blog_path: Path = Path("../content") / (date + "-" + (slugify(title)))

    try:
        if blog_path.is_dir() and download_images:
            shutil.rmtree(blog_path)
    except Exception:
        pass

    blog_path.mkdir(exist_ok=True, parents=True)
    if (blog_path / "index.md").is_file():
        os.remove(blog_path / "index.md")

    with open(blog_path / "index.md", "w") as f:
        f.write(output)

    return blog_path


def download_images_from_s3(blog_path: Path, cover: str):
    image_dir = blog_path / "images"
    image_dir.mkdir(exist_ok=True)
    s3.download_file(S3_BUCKET, cover.split("com")[1][1:], str(image_dir / cover.split("/")[-1]))


def main(blogs: List[str], download_images: bool = False):
    config = get_config()
    client = pymongo.MongoClient(
        config["host"],
        config["port"],
        username=config["username"],
        password=config["password"],
        authSource=config["db"],
    )
    db = client[config["db"]]

    for blog in blogs:
        posts: List[Dict[str, Any]] = [post for post in db[blog].find().sort("updated_at", -1)]
        print(f"Processing {len(posts)} posts in {blog} blog...")

        for post in posts:
            title, tags, date, body, image = extract_article(post)
            image_file = image.split("/")[-1]
            ext = image_file.split(".")[-1]
            new_image_file = image_file.replace(ext, "webp")
            cover_image = "./images/covers/" + new_image_file
            print(cover_image)
            template: Template = get_template(TEMPLATE_PATH)
            output = template.render(
                title=title,
                tags=[tag for tag in tags if tag.lower() != blog.lower()],
                date=date,
                category=blog.title(),
                body=body,
                cover=cover_image,
            )
            blog_path = save_output(output, title, date)

            if download_images:
                download_images_from_s3(blog_path, cover=image)

    return None


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-b", "--blogs", nargs="*", type=str, help="Blog in question to migrate")
    parser.add_argument("--download_images", action="store_true")
    kwargs = vars(parser.parse_args())
    main(**kwargs)
