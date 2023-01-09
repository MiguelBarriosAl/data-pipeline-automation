import json
import os
from src.app.checkers import check_allowed_file
from src.config import CHUNKS_SIZE


def read_files(path: str) -> list:
    files = os.listdir(path)
    # sorted_files = sorted(files, key=lambda x: int(x.split('-')[-2]))
    allowed_files = [file for file in files[:2] if check_allowed_file(file)]
    files_chunks = process_files_chunks(path, allowed_files)
    return files_chunks


def process_files_chunks(path, filenames: list[str]) -> list:
    all_data = []
    for filename in filenames:
        with open(path + filename, "r") as f:
            data = [filename]
            counter = 0
            while True:
                line = f.readline()
                if not line:
                    break
                data.append(json.loads(line))
                counter += 1
                if counter >= CHUNKS_SIZE:
                    all_data.append(data)
                    data = []
                    counter = 0
            all_data.append(data)
    return all_data

