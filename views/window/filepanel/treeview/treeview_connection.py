'''
Created on Dec 5, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui


class TreeviewConnection(object):

    def __init__(self, panel_tree_view):
        '''constructor
        initializes an object with a PanelTreeView as main attribute passed by
        reference

        Keyword arguments:
        :param panel_tree_view: an initialized instance (parent TreeView)
                                of PanelTreeView class
        '''
        super(TreeviewConnection, self).__init__()
        self.panel_tree_view = panel_tree_view

        self.panel_tree_view.doubleClicked.connect(
            self.double_clicked_connection)
        self.panel_tree_view.clicked.connect(self.clicked_connection)
        self.panel_tree_view.connect(self.panel_tree_view, QtCore.SIGNAL(
            "spacePressed"), self.treeview_toggle_row)

    def double_clicked_connection(self, index):
        '''this method visually goes deep when current item in the tree is a
        directory, if the item is not a folder it should try to open the file
        with OS basis

        Keyword arguments:
        :param index: QModelIndex where double clicked event happened
        '''
        event_button = self.panel_tree_view.current_mouse_event.button()
        if index.model().isDir(index) and event_button == QtCore.Qt.LeftButton:
            self.panel_tree_view.window_file_panel.goto_folder(index)

    def clicked_connection(self, index):
        """this method is meant to identify a click event over a row into
        the main treeview so that it can be handled accordingly
        If the row is a file, then the File name will be editable

        Keyword arguments:
        :param index: QModelIndex where clicked event happened
        """
        event_button = self.panel_tree_view.current_mouse_event.button()
        if event_button == QtCore.Qt.RightButton:
            self.treeview_toggle_row(index)

        if not index.model().isDir(index) and event_button == QtCore.Qt.LeftButton and index.column() == 0:
           self.panel_tree_view.edit(index)

    def treeview_toggle_row(self, index):
        """This method selects and deselects a row into the treevieww main attribute

        Keyword arguments:
        :param index: QModelIndex from the entire row is going to be toggled
        """
        parent_index = index.model().parent(index)
        right_index = self.panel_tree_view.model.index(
            index.row(), self.panel_tree_view.model.columnCount() - 1,
            parent_index)
        left_index = self.panel_tree_view.model.index(
            index.row(), 0, parent_index)
        selected_row = QtGui.QItemSelection(left_index, right_index)
        self.panel_tree_view.selectionModel().select(
            selected_row, QtGui.QItemSelectionModel.Toggle)
