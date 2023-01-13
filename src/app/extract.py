import json
from src.app.checkers import check_allowed_file
from src.constant import JSON_CHUNKS_SIZE, PATH_DIR


def read_json(files: list) -> list:
    sorted_files = sorted(files, key=lambda x: int(x.split('-')[-2]))
    allowed_files = [file for file in sorted_files if check_allowed_file(file)]
    files_chunks = process_files_chunks(PATH_DIR, allowed_files)
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
                if counter >= JSON_CHUNKS_SIZE:
                    all_data.append(data)
                    data = []
                    counter = 0
            all_data.append(data)
    return all_data
