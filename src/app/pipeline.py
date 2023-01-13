import os
from src.app.extract import read_json
from src.app.transform import transform_n_load
from src.app.utils import filter_files_by_date_json, split_into_batches


class Pipeline:
    def __init__(self, date, path, batch):
        self.data_batch = None
        self.json_files = [f for f in os.listdir(path)]
        self.files_json_by_date = filter_files_by_date_json(self.json_files, date)
        self.batch = batch

    def load_json(self):
        for batch in split_into_batches(self.files_json_by_date, self.batch):
            print(batch)
            self.data_batch = read_json(batch)
            transform_n_load(self.data_batch)





