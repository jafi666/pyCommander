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
        self.window_file_panel = WindowFilePanel(self.comander_window)

    def add_new_file(self):
        '''
        Add new file: It displays an input dialog for the file name.
        If the file name is empty, then an error message is displayed to
        insert a file name.
        None is returned when Click on Cancel button
        '''
        current_path = self.get_current_path_after_a_panel_selected()
        if current_path is None:
            self.show_error_message("Notice", "You must select a panel first")
            return None

        filename, ok = QtGui.QInputDialog.getText(
            self, 'Create new file', 'Enter a file name')
        if ok:
            if str(filename) != '':
                new_filename = str(filename)
                self.file_operation.create_file(current_path, new_filename)
            else:
                self.show_error_message("ERROR", "File name cannot be empty")
                self.add_new_file()
        else:
            return None

    def get_current_path_after_a_panel_selected(self):
        '''Get current path after a panel is selected: First it verifies if the right
        or left panel is selected.
        It returns current path of the panel that is selected.
        If no panel is selected, then it returns None
        '''
        if (self.commander_window.tab_left.active):
            return self.commander_window.tab_left.current_folder_path

        elif (self.commander_window.tab_right.active):
            return self.commander_window.tab_right.current_folder_path
        else:
            return None

    def show_error_message(self, dialog_name, dialog_message):
        '''Show error message: It displays a message box.
        It receives two parameters:
        dialog_name : It is the name of the dialog
        dialog_message : It is the message that will be displayed in the dialog
        For example:
        self.show_error_message("ERROR", "File name cannot be empty")
        '''
        QtGui.QMessageBox.warning(self, dialog_name,
                                   dialog_message)

    def rename_file_dialog(self):
        '''
        '''
        filename, ok = QtGui.QInputDialog.getText(
            self, 'Create new file', 'Enter a file name')
        if ok:
            if str(filename) != '':
                new_filename = str(filename)
                self.file_operation.rename_file(old_filename, new_filename)
            else:
                self.show_error_message("ERROR", "File name cannot be empty")
                self.add_new_file()
        else:
            return None
