'''
Created on 7/12/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui


class TreeviewFileSystemModel(QtGui.QFileSystemModel):

    def __init__(self, panel_tree_view):
        '''Constructor
        initializes a QFileSystemModel object with a PanelTreeView as main
        attribute passed by reference

        Keyword arguments:
        :param panel_tree_view: an initialized instance (parent TreeView)
                                of PanelTreeView class
        '''
        super(TreeviewFileSystemModel, self).__init__()
        self.panel_tree_view = panel_tree_view
        self.insertColumn(self.columnCount(self.index(0, 4)))
