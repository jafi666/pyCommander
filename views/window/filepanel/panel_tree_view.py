'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui
from views.window.filepanel.treeview import TreeviewConnection
from views.window.filepanel.treeview import TreeviewFileSystemModel
from views.window.filepanel.treeview import TreeviewConfig
from views.dialog.dialog_file_properties import DialogFileProperties


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
        self.model = TreeviewFileSystemModel(self)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(250)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timeout)
        self.left_click_count = self.right_click_count = 0

        self.setModel(self.model)
        self.setItemsExpandable(False)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtGui.QAbstractItemView.NoSelection)

        self.keylist = []
        self.new_list = []

        self.current_mouse_event = None
        self.first_release = None

        self.setup_connections()
        self.config = TreeviewConfig(self)
        self.dialog_file_properties = DialogFileProperties()

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
        if event.key() == QtCore.Qt.Key_Enter:
            self.emit(QtCore.SIGNAL("altPressed"), self.currentIndex())

        return False

    def mousePressEvent(self, event):
        """this method stores the event triggered for mouse pressed so that it
        can be used later from signals, regular behavior is still working
        """
        self.current_mouse_event = event
        return super(PanelTreeView, self).mousePressEvent(event)

    def keyPressEvent(self, event):
        """this method is going to handle key sequence handling, in order to
        have key shortcuts over treeview
        """
        # print "KeyPressEventPanelTreeView"
        self.first_release = True
        key_pressed = str(event.key())
        self.keylist.append(key_pressed)

        return super(PanelTreeView, self).keyPressEvent(event)

    def keyReleaseEvent(self, event):

        if self.first_release == True:
            self.processmultikeys(self.keylist)

        self.first_release = False

        if len(self.keylist) >= 1:
            del self.keylist[-1]

    def processmultikeys(self, keyspressed):

        if(len(self.keylist) > 1):
            first_value = self.keylist[0]
            second_value = self.keylist[1]
            # print  first_value, type(first_value), second_value,
            # type(second_value)
            if first_value == '16777251' and second_value == '16777220':
                print "more than 2 keys with Alt + Enter:"
                # print  first_value, second_value
                # here calling to the dialog hat should have the properties
                self.dialog_file_properties.initUI()
