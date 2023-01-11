import unittest
from unittest.mock import patch, mock_open
import json

from src.app.extract import process_files_chunks


class TestProcessFilesChunks(unittest.TestCase):
    def test_process_files_chunks(self):
        path = '/path/to/files/'
        filenames = ['file1.txt', 'file2.txt']
         # Create a mock file object
        m = mock_open(read_data='{"a": 1}\n{"b": 2}\n')

        # Create a patch for the built-in `open` function
        with patch('builtins.open', m, create=True):
            all_data = process_files_chunks(path, filenames)

        # Assert that the correct data was read from the files
        expected_all_data = [
            [filenames[0], json.loads('{"a": 1}'), json.loads('{"b": 2}')],
            [filenames[1], json.loads('{"a": 1}'), json.loads('{"b": 2}')],
        ]
        self.assertEqual(all_data, expected_all_data)
        m.assert_called_once_with(path + filenames[0], 'r')
        m().readline.assert_called_with()