import unittest
from src.app.utils import filter_files_by_date_json, split_into_batches


class TestFilterFilesByDateJson(unittest.TestCase):
    def test_filter_files_by_date_json(self):
        test_list = ['file1_2021-01-01.json', 'file2_2021-02-01.json', 'file3_2022-01-01.json', 'file4_2022-02-01.json']
        date = '2021'
        result = filter_files_by_date_json(test_list, date)
        self.assertEqual(result, ['file1_2021-01-01.json', 'file2_2021-02-01.json'])

    def test_filter_files_by_date_json_empty_list(self):
        test_list = []
        date = '2021'
        result = filter_files_by_date_json(test_list, date)
        self.assertEqual(result, [])

    def test_filter_files_by_date_json_no_match(self):
        test_list = ['file1_2021-01-01.json', 'file2_2021-02-01.json', 'file3_2022-01-01.json', 'file4_2022-02-01.json']
        date = '2023'
        result = filter_files_by_date_json(test_list, date)
        self.assertEqual(result, [])


class TestSplitIntoBatches(unittest.TestCase):
    def test_split_into_batches(self):
        test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        batch_size = 3
        result = list(split_into_batches(test_data, batch_size))
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])

    def test_split_into_batches_batch_size_1(self):
        test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        batch_size = 1
        result = list(split_into_batches(test_data, batch_size))
        self.assertEqual(result, [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

    def test_split_into_batches_empty_list(self):
        test_data = []
        batch_size = 3
        result = list(split_into_batches(test_data, batch_size))
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
