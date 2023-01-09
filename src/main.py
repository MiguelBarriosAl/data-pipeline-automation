import os
from pathlib import Path

from src.app.extract import read_files
from src.config import UPLOAD_FOLDER

BASE_DIR = Path(__file__).resolve(strict=True).parent
PATH_DIR = (str(BASE_DIR) + UPLOAD_FOLDER)



def main():
    """
    extract
    trasnform
    load
    """
    print(read_files(PATH_DIR))
    return ""


if __name__ == "__main__":
    main()
