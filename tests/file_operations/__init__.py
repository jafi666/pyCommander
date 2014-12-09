'''
Created on 12/9/2014

@author: Ivar Fuentes
'''
import unittest
import os.path
from models.file_operation import FileOperation


class TestCreateCopyMoveDeleteFiles(unittest.TestCase):
    
    def test_create_files(self):
        self.path = "../../testFolder/"
        self.filename = "Test001"
        
        self.file_operation.create_file(self.path, self.filename)
        self.assertTrue(os.path.isfile( self.path + self.filename))
        


if __name__ == "__main__":
    unittest.main()
    