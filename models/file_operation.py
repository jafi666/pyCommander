'''
Created on Dec 01, 2014

@author: Scarlen Quinsamolle
'''

import os
import shutil

class FileOperation(object):

    def __init__(self):
        super(FileOperation, self).__init__()

    def create_file(self, path, filename):
        '''
        Create a file given a path and a filename
        path: String. It is an absolute Path where to create the file
        filename: It is a string. Name of the file with the extension
        '''
        try:
            filepath = os.path.join(path, filename)
            file_created = open(filepath, "a")
        except:
            print "File is not created"
    
    def copy_file(self, source, target_path):
        try:
            shutil.copy2(source, target_path)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)
                 
                
    def move_files(self, source, target_path):
        try:
            shutil.move(source, target_path)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)
    
    def delete_file(self, path, list_of_files):
        
        if os.path.isfile(path + list_of_files) is True:
            try:
                os.remove(path + list_of_files)
            except IOError as e:
                print('Error: %s' % e.strerror)
        else:
            try:
                self.delete_folder(path)
            except IOError as e:
                print('Error: %s' % e.strerror)
            
    
    def delete_folder(self, path):
        try:
            shutil.rmtree(path)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename,e.strerror))
    
    def create_folder(self, path, folder_name):
        if not os.path.isdir(path + folder_name):
            os.makedirs(path + folder_name)
        