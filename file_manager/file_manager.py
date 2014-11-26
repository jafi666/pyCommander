'''
Created on Nov 24, 2014

@author: Scarlen Quinsamolle
'''

from PyQt4 import QtGui

class FileManager(QtGui.QWidget):

    def __init__(self, commander_window):
        super(FileManager, self).__init__()
        self.commander_window = commander_window

    def enter_file_name(self):
        filename, ok = QtGui.QInputDialog.getText(self, 'Create new file', 'Enter a file name')
        if ok:
            return str(filename)

    def add_new_file(self):
        if (self.commander_window.tab_left.active):
            print self.commander_window.tab_left.current_folder_path + "L"
            self.enter_file_name()

        elif (self.commander_window.tab_right.active):
            print self.commander_window.tab_right.current_folder_path + "R"
            self.enter_file_name()
        else:
            print "Panel is not selected"

    