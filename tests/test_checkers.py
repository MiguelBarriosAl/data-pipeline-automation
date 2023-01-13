import unittest
from src.app.checkers import check_allowed_file, check_fields


class TestCheckAllowedFile(unittest.TestCase):

    def test_check_allowed_file(self):
        test_filename = 'file.json'
        result = check_allowed_file(test_filename)
        self.assertTrue(result)

    def test_check_allowed_file_disallowed(self):
        test_filename = 'file.txt'
        result = check_allowed_file(test_filename)
        self.assertFalse(result)


class TestCheckFields(unittest.TestCase):

    def test_check_fields(self):
        test_data = {'field1': 'value1', 'field2': 'value2'}
        fields = ['field1', 'field2']
        self.assertTrue(check_fields(test_data, fields))

    def test_check_fields_missing(self):
        test_data = {'field1': 'value1'}
        fields = ['field1', 'field2']
        self.assertRaises(AssertionError, check_fields, test_data, fields)

    def test_check_fields_empty_data(self):
        test_data = {}
        fields = ['field1', 'field2']
        self.assertRaises(AssertionError, check_fields, test_data, fields)


if __name__ == '__main__':
    unittest.main()




