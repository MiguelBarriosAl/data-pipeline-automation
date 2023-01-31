import unittest
from unittest.mock import mock_open, Mock
from app.data_extract_files import process_files_chunks

mock = Mock()


class TestProcessFilesChunks(unittest.TestCase):
    @mock.patch('builtins.open', mock_open(read_data='{"line1": "data1"}\n{"line2": "data2"}\n'))
    def test_process_files_chunks(self, mock_file):
        path = './test_files/'
        filenames = ['file1.txt']
        expected_output = [['file1.txt', {'line1': 'data1'}, {'line2': 'data2'}]]
        result = process_files_chunks(path, filenames)
        mock_file.assert_called_once_with(path + 'file1.txt', 'r')
        self.assertEqual(result, expected_output)

    @mock.patch('builtins.open', mock_open(read_data=''))
    def test_process_files_chunks_empty_file(self, mock_file):
        path = './test_files/'
        filenames = ['file1.txt']
        result = process_files_chunks(path, filenames)
        mock_file.assert_called_once_with(path + 'file1.txt', 'r')
        self.assertEqual(result, [['file1.txt']])


if __name__ == '__main__':
    unittest.main()
