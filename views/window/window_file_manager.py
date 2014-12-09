'''
Created on Nov 24, 2014

@author: Scarlen Quinsamolle
'''

from PyQt4 import QtGui
from models.file_operation import FileOperation


class WindowFileManager(QtGui.QWidget):

    def __init__(self, commander_window):
        super(WindowFileManager, self).__init__()
        self.commander_window = commander_window
        self.file_operation = FileOperation()

    def add_new_file(self):
        '''
        'Add new file' method displays an input dialog for the file name.
        It does not receive parameters.
        None is returned when Click on Cancel button
        '''
        current_path = self.get_current_path_from_panel_selected()
        if current_path is None:
            QtGui.QMessageBox.warning(self, "Notice",
                                      "You must select a panel first")
            return None

        filename, ok = QtGui.QInputDialog.getText(
            self, 'Create new file', 'Enter a file name')
        if ok:
            if str(filename) != '':
                new_filename = str(filename)
                self.file_operation.create_file(current_path, new_filename)
            else:
                self.show_empty_filename_message()
        else:
            return None
    
    def delete_list_of_files(self):
        pass
    
    def move_list_of_files(self):
        pass
    
    def copy_list_of_files(self):
        pass
    
    def get_current_path_from_panel_selected(self):
        '''Get current path from panel' verifies if the right or left panel is selected
        It returns current path of the panel that is selected.
        '''
        if (self.commander_window.tab_left.active):
            return self.commander_window.tab_left.current_folder_path

        elif (self.commander_window.tab_right.active):
            return self.commander_window.tab_right.current_folder_path
        else:
            return None
    
    def get_list_of_files_selected(self):
        pass

    def show_empty_filename_message(self):
        '''Show empty filename warning' displays a message box related to the
        file name is empty
        '''
        QtGui.QMessageBox.critical(self, "ERROR",
                                   "File name cannot be empty")
        self.add_new_file()
