'''
Created on Dec 01, 2014

@author: Scarlen Quinsamolle
'''
import os


class FileOperation(object):

    def __init__(self):
        super(FileOperation, self).__init__()

    def create_file(self, path, filename):
        '''Create a file given a path and a filename

        :param path: String. It is an absolute Path where to create the file
        :param filename: It is a string. Name of the file with the extension
        '''
        try:
            filepath = os.path.join(path, filename)
            file_created = open(filepath, "a")
            return True
        except:
            return False

    def rename_file(self, old_filename, new_filename):
        try:
            os.rename(old_filename, new_filename)
            return True
        except:
            return False



