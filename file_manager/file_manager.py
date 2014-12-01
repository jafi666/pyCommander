'''
Created on Nov 24, 2014

@author: Scarlen Quinsamolle
'''

from PyQt4 import QtGui
import warnings
import logging
import ctypes
from models.create_file import CreateFile

class FileManager(QtGui.QWidget):

    def __init__(self, commander_window):
        super(FileManager, self).__init__()
        self.commander_window = commander_window
        self.create_file = CreateFile()

    def add_new_file(self):
        filename, ok = QtGui.QInputDialog.getText(self, 'Create new file', 'Enter a file name')
        if ok:
            if str(filename) != '':
                new_filename = str(filename)
                current_path = self.get_current_path_from_panel_selected()
                self.create_file.create_file(current_path, new_filename)
            else:
                self.show_empty_filename_warning()

        else:
            logging.debug("click cancel")


    def get_current_path_from_panel_selected(self):
        if (self.commander_window.tab_left.active):
            return self.commander_window.tab_left.current_folder_path

        elif (self.commander_window.tab_right.active):
            return self.commander_window.tab_right.current_folder_path
        else:
            ctypes.windll.user32.MessageBoxA(0, "You must select a panel", "Warning", 0)


    def show_empty_filename_warning(self):
        ctypes.windll.user32.MessageBoxA(0, "File name cannot be empty", "Create new file", 0)
        self.add_new_file()