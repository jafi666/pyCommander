'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui
from views.window.filepanel.treeview.treeview_connection import TreeviewConnection


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

        self.current_mouse_event = None

        self.setup_connections()

    def setup_connections(self):
        '''setting up tree view connections
        used only from constructor
        '''
        self.connections = TreeviewConnection(self)

    def event(self, event):
        '''this method captures the events and control them to be handled properly
        override of native event method
        '''
        if (event.type() == QtCore.QEvent.KeyPress):
            if self.__key_press_event(event):
                return True

        return super(PanelTreeView, self).event(event)

    def __key_press_event(self, event):
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

    def mousePressEvent(self, event):
        """this method stores the event triggered for mouse pressed so that it
        can be used later from signals, regular behavior is still working
        """
        self.current_mouse_event = event
        return super(PanelTreeView, self).mousePressEvent(event)

    def keyPressEvent(self, event):
        """
        """
        return super(PanelTreeView, self).keyPressEvent(event)
