'''
Created on 25/11/2014

@author: Alexander Apaza
'''
from PyQt4 import QtGui

class PanelDoubleClickPath(QtGui.QLineEdit):
    def __init__(self, parent=None):
        '''constructor
        initializes the double click event in order to enable the field path

        Keyword arguments:
        :param parent: initializes the parent with None
        '''
        super(QtGui.QLineEdit, self).__init__(parent)

    def mouseDoubleClickEvent(self, event):
        '''
        Enables the path to edit

        Keyword arguments:
        :param event: QLineEdit where double clicked event happened
        so the path can be edited
        '''
        self.setReadOnly(False)
