'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QItemSelection
from PyQt4.Qt import QModelIndex


class PanelTreeView(QtGui.QTreeView):

    def __init__(self, window_file_panel):
        '''constructor
        initializes a widget with a TreeView to be put on WindowFilePanel.

        Keyword arguments:
        :param window_file_panel: an initialized instance (parent widget)
                                  of WindowFilePanel class
        '''
        super(PanelTreeView, self).__init__(window_file_panel.tab_widget)
        self.window_file_panel = window_file_panel
        self.model = QtGui.QFileSystemModel()

        self.setModel(self.model)
        self.setItemsExpandable(False)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtGui.QAbstractItemView.NoSelection)

        self.currentMouseEvent = None

        self.setup_connections()

    def setup_connections(self):
        '''setting up tree view connections
        used only from constructor
        '''
        self.doubleClicked.connect(self.double_clicked_connection)
        self.clicked.connect(self.clicked_connection)
        self.connect(self, QtCore.SIGNAL(
            "spacePressed"), self.toggle_row)

    def event(self, event):
        '''this method captures the events and control them to be handled properly
        override of native event method
        '''
        if (event.type() == QtCore.QEvent.KeyPress):
            if self.key_press_event(event):
                return True

        return super(PanelTreeView, self).event(event)

    def mousePressEvent(self, event):
        """
        """
        self.currentMouseEvent = event
        return super(PanelTreeView, self).mousePressEvent(event)

    def key_press_event(self, event):
        '''this method will create the tab pressed signal which will be listened by
        commander windows to switch between panels
        '''
        if event.key() == QtCore.Qt.Key_Tab:
            self.emit(QtCore.SIGNAL("tabPressed"), self.currentIndex())
            return True
        if event.key() == QtCore.Qt.Key_Space:
            self.emit(QtCore.SIGNAL("spacePressed"), self.currentIndex())
            return True
        if event.key() == QtCore.Qt.Key_Backspace:
            self.emit(QtCore.SIGNAL("backspacePressed"), self.currentIndex())
            return True

        return False

    def double_clicked_connection(self, index):
        '''this method visually goes deep when current item in the tree is a
        directory, if the item is not a folder it should try to open the file
        with OS basis
        '''
        if index.model().isDir(index):
            self.window_file_panel.goto_folder(index)

    def clicked_connection(self, index):
        """
        """
        if (self.currentMouseEvent.button() == QtCore.Qt.RightButton):
            self.toggle_row(index)

    def toggle_row(self, index):
        """
        """
        right_index = self.model.index(
            index.row(), self.model.columnCount() - 1,
            index.model().parent(index))
        left_index = self.model.index(
            index.row(), 0, index.model().parent(index))
        selected_row = QtGui.QItemSelection(left_index, right_index)
        self.selectionModel().select(
            selected_row, QtGui.QItemSelectionModel.Toggle)
