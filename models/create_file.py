'''
Created on Dec 01, 2014

@author: Scarlen Quinsamolle
'''

import os
class CreateFile(object):

    def __init__(self):
        super(CreateFile, self).__init__()

    def create_file(self, path, filename):
        filepath = os.path.join(path,filename)
        file_created = open(filepath, "a")


