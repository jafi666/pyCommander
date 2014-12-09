'''
Created on 12/08/2014

@author: Scarlen Quinsamolle
'''
import unittest
from models.file_operation import FileOperation


class TestFileOperation(unittest.TestCase):

    def test_verify_that_it_returns_true_when_the_file_is_created_given_a_path_and_filename(self):
        filemanager = FileOperation()
        path = "C:/monitor/pyComander_1209/pyComander"
        filename = "test.txt"
        self.assertTrue(filemanager.create_file(path, filename))

    def test_verify_that_it_returns_false_when_the_file_is_not_created_given_a_path_and_an_empty_filename(self):
        filemanager = FileOperation()
        path = "C:/monitor/pyComander_1209/pyComander"
        filename = ""
        self.assertFalse(filemanager.create_file(path, filename))

    def test_verify_that_it_returns_false_when_the_file_is_not_created_given_an_wrong_path_and_a_filename(self):
        filemanager = FileOperation()
        path = "D:"
        filename = "test.txt"
        self.assertFalse(filemanager.create_file(path, filename))

if __name__ == "__main__":
    unittest.main()
