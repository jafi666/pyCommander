'''
Created on Dec 01, 2014

@author: Scarlen Quinsamolle, Ivar Fuentes
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
        '''
        Copy a file given a Source and a Target Path
        source: String. It is a Path that can contain the absolute path and also the specific file name plus his extension
        target_path: String. Name of the target path to copy a file
        '''
        try:
            shutil.copy2(source, target_path)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)

    def move_files(self, source, target_path):
        '''
        Move a file given a Source and a Target Path
        source: String. It is a Path that can contain the absolute path and also the specific file name plus his extension
        target_path: String. Name of the target path to move a file
        '''
        try:
            shutil.move(source, target_path)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)

    def delete_file(self, path, file_name):
        
        '''
        Delete a file given a path and the file name, if this is not a file it will delete a folder
        path: String. It is an Path that can contains the absolute path
        file_name: String. Name of the file to delete
        '''

        if os.path.isfile(path + file_name) is True:
            try:
                os.remove(path + file_name)
            except IOError as e:
                print('Error: %s' % e.strerror)
        else:
            try:
                self.delete_folder(path)
            except IOError as e:
                print('Error: %s' % e.strerror)

    def delete_folder(self, path):
        '''
        Delete a folder given a path
        path: String. It is an Path that can contains the absolute path
        '''
        try:
            shutil.rmtree(path)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

    def create_folder(self, path, folder_name):
        '''
        Create a folder given a path
        path: String. It is an Path that can contains the absolute path
        folder_name: String. Name of the folder to create
        '''
        if not os.path.isdir(path + folder_name):
            os.makedirs(path + folder_name)
