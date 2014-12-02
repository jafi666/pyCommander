'''
Created on Dec 01, 2014

@author: Scarlen Quinsamolle
'''

import os
class FileOperation(object):

    def __init__(self):
        super(FileOperation, self).__init__()

    def create_file(self, path, filename):
        '''
        Create a file given a path and a filename
        path: String. Path where to create the file
        filename: It is a string. Name of the file with the extension
        '''
        filepath = os.path.join(path,filename)
        file_created = open(filepath, "a")


