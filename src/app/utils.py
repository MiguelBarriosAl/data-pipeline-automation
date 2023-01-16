import time
import random
import re


def filter_files_by_date_json(lst: list, date: str) -> list:
    filtered_list = [x for x in lst if re.search(date, x)]
    return filtered_list


def split_into_batches(data: list, batch_size: int) -> list:
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


def generate_id() -> str:
    timestamp = int(time.time())
    random_value = random.randint(0, 1000000)
    return f"{timestamp}{random_value}"
