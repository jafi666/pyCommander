'''
Created on Dec 01, 2014

@author: Scarlen Quinsamolle
'''

import os
class CreateFile(object):

    def __init__(self):
        super(CreateFile, self).__init__()

    '''
    Create a file given a path and filename
    path: Path where to create the file
    filename: Name of the file with the extension
    '''
    def create_file(self, path, filename):
        filepath = os.path.join(path,filename)
        file_created = open(filepath, "a")


