import os
import shutil
from pathlib import Path
from typing import Any, Dict, List

from jinja2 import Template

import pymongo
from dotenv import load_dotenv
from slugify import slugify
from tqdm import tqdm

TEMPLATE_PATH = Path("./template.txt")
S3_BUCKET = "https://th-website.s3-website.us-east-2.amazonaws.com/"


def get_template(template_path: Path) -> Template:
    with open(template_path, "r") as f:
        data = f.read().strip()
    return Template(data)


def get_config():
    """ Get Mongo Config Information """

    load_dotenv()
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
    image = S3_BUCKET + post["image"]
    return (title, tags, date, body, image)


def save_output(output: str, title: str, date: str):
    base_path: Path = Path("../content") / date.split("-")[0]
    base_path.mkdir(exist_ok=True)

    blog_path = base_path / (slugify(title) + ".md")
    if blog_path.is_file():
        os.remove(blog_path)

    with open(blog_path, "w") as f:
        f.write(output)

    return None


def main(blogs: List[str]):
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
            template: Template = get_template(TEMPLATE_PATH)
            output = template.render(
                title=title,
                tags=[tag for tag in tags if tag.lower() != blog.lower()],
                date=date,
                category=blog.title(),
                body=body,
                image=image,
            )
            save_output(output, title, date)

    return None


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-b", "--blog", nargs="*", type=str, help="Blog in question to migrate")
    args = parser.parse_args()
    main(args.blog)
