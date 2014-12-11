'''
Created on 7/12/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui


class TreeviewFileSystemModel(QtGui.QFileSystemModel):

    def __init__(self, panel_tree_view):
        '''
        Constructor
        '''
        super(TreeviewFileSystemModel, self).__init__()
        self.panel_tree_view = panel_tree_view
        self.insertColumn(self.columnCount(self.index(0, 0)))
        self.setReadOnly(False)
