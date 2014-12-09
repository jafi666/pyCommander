'''
Created on 12/9/2014

@author: Ivar Fuentes
'''
import unittest
import os.path
from models.file_operation import FileOperation


class TestCreateCopyMoveDeleteFiles(unittest.TestCase):
    
    def test_create_file(self):
        self.operator = FileOperation()
        self.path = "../../testFolder/"
        self.filename = "Test001.txt"
        
        self.operator.create_file(self.path, self.filename)
        self.assertTrue(os.path.isfile( self.path + self.filename))
    
    def test_copy_file(self):
        self.operator2 = FileOperation()
        self.parent_path = "../../testFolder/"
        self.filename = "Test002.txt"
        self.source = self.parent_path + self.filename
        self.target_path = "../../testFolder/Target/"
        
        self.operator2.create_file(self.parent_path, self.filename)
        self.operator2.copy_file(self.source, self.target_path)
        self.assertTrue(os.path.isfile( self.target_path + self.filename))
    
    def test_move_file(self):
        self.operator3 = FileOperation()
        self.parent_path = "../../testFolder/"
        self.filename = "Test003.txt"
        self.source = self.parent_path + self.filename
        self.target_path = "../../testFolder/Target/"
        
        self.operator3.create_file(self.parent_path, self.filename)
        self.operator3.move_files(self.source, self.target_path)
        self.assertFalse(os.path.isfile( self.parent_path + self.filename))
        self.assertTrue(os.path.isfile( self.target_path + self.filename))
    
    def test_delete_file(self):
        self.operator4 = FileOperation()
        self.parent_path = "../../testFolder/"
        self.filename = "Test004.txt"
        self.source = self.parent_path + self.filename
                
        self.operator4.create_file(self.parent_path, self.filename)
        self.assertTrue(os.path.isfile( self.parent_path + self.filename))
        
        self.operator4.delete_file(self.parent_path, self.filename)
        self.assertFalse(os.path.isfile( self.parent_path + self.filename))
    
    def test_create_folder(self):
        self.operator5 = FileOperation()
        self.path = "../../testFolder/"
        self.folder_name = "NewFolder"
        
        self.operator5.create_folder(self.path, self.folder_name)
        self.assertTrue(os.path.isdir(self.path + self.folder_name))
    
    def test_delete_folder(self):
        self.operator5 = FileOperation()
        self.path = "../../testFolder/"
        self.folder_name = "NewFolder"
        
        self.operator5.delete_folder(self.path + self.folder_name)
        self.assertFalse(os.path.isdir(self.path + self.folder_name))
        
        
        
if __name__ == "__main__":
    unittest.main()
    