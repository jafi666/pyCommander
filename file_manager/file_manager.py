'''
Created on Nov 24, 2014

@author: Scarlen Quinsamolle
'''

from PyQt4 import QtGui
import ctypes
from models.file_operation import FileOperation

class FileManager(QtGui.QWidget):

    def __init__(self, commander_window):
        super(FileManager, self).__init__()
        self.commander_window = commander_window
        self.file_operation = FileOperation()

    def add_new_file(self):
        '''
        'Add new file' method displays an input dialog for the file name.
        It does not receive parameters.
        '''
        filename, ok = QtGui.QInputDialog.getText(self, 'Create new file', 'Enter a file name')
        if ok:
            if str(filename) != '':
                new_filename = str(filename)
                current_path = self.get_current_path_from_panel_selected()
                self.file_operation.create_file(current_path, new_filename)
            else:
                self.show_empty_filename_message()

        else:
            return None

    def get_current_path_from_panel_selected(self):
        '''
        'Get current path from panel' verifies if the right or left panel is selected
        It returns current path of the panel that is selected.
        '''
        if (self.commander_window.tab_left.active):
            return self.commander_window.tab_left.current_folder_path

        elif (self.commander_window.tab_right.active):
            return self.commander_window.tab_right.current_folder_path
        else:
            ctypes.windll.user32.MessageBoxA(0, "You must select a panel", "Warning", 0)

    def show_empty_filename_message(self):
        '''
        'Show empty filename warning' displays a message box related to the file name is empty
        '''
        ctypes.windll.user32.MessageBoxA(0, "File name cannot be empty", "Create new file", 0)
        self.add_new_file()