import os
from app.data_extract_files import read_json
from app.data_transformer_db import transform_n_load
from app.utils import filter_files_by_date_json, split_into_batches


class Pipeline:
    def __init__(self, date: str, path: str, batch: int):
        self.data_batch = None
        self.json_files = [f for f in os.listdir(path)]
        self.files_json_by_date = filter_files_by_date_json(self.json_files, date)
        self.batch = batch

    def etl_json(self):
        for batch in split_into_batches(self.files_json_by_date, self.batch):
            self.data_batch = read_json(batch)
            transform_n_load(self.data_batch)
