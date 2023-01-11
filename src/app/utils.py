import time
import random
import re


def filter_files_by_date_json(file_list, date):
    date_pattern = date+'-\d{2}-\d{2}-\d{2}'
    json_pattern = re.compile(r'.*\.json$')
    filtered_files = list(filter(lambda x: re.search(date_pattern, x) and json_pattern.match(x), file_list))
    return filtered_files


def split_into_batches(data: list, batch_size: int) -> list:
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


def generate_id():
    timestamp = int(time.time())
    random_value = random.randint(0, 1000000)
    return f"{timestamp}{random_value}"