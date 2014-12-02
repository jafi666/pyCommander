'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui


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
        self.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)

        self.setup_connections()

    def setup_connections(self):
        '''setting up tree view connections
        used only from constructor
        '''
        self.doubleClicked.connect(self.double_clicked_connection)

    def event(self, event):
        '''this method captures the events and control them to be handled properly
        override of native event method
        '''
        if (event.type() == QtCore.QEvent.KeyPress):
            if self.key_press_event(event):
                return True

        return super(PanelTreeView, self).event(event)

    def key_press_event(self, event):
        '''this method will create the tab pressed signal which will be listened by
        commander windows to switch between panels
        '''
        if event.key() == QtCore.Qt.Key_Tab:
            self.emit(QtCore.SIGNAL("tabPressed"))
            return True
        return False

    def double_clicked_connection(self, index):
        '''this method visually goes deep when current item in the tree is a
        directory, if the item is not a folder it should try to open the file
        with OS basis
        '''
        if index.model().isDir(index):
            self.window_file_panel.goto_folder(index)
