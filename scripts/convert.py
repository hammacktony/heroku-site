""" Convert webp to png """
import subprocess
from pathlib import Path
from typing import List, Tuple


def get_webp_images(image_directory: str) -> List[Path]:
    """ Get all the webp images """
    img_directory = Path(image_directory)
    assert img_directory.is_dir()
    images = [image for image in img_directory.glob("*.webp")]
    assert len(images) > 0, "No Webp files to be found"
    return images


def get_output_file_name(image_path: Path) -> Path:
    """ Get new png file """
    output_path = Path(str(image_path).split(".")[0] + ".png")
    return output_path


def main(image_directory: str):
    """ Convert files from webp to png """
    images = get_webp_images(image_directory=image_directory)

    for image_path in images:
        output_path = get_output_file_name(image_path)
        bashCommand = f"dwebp {str(image_path)} -o {str(output_path)}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-d", "--image_directory", type=str, required=True, help="Image directory to convert from webp to png.")
    kwargs = vars(parser.parse_args())
    main(**kwargs)
