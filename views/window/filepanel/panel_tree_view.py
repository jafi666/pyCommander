'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui

class PanelTreeView(QtGui.QTreeView):
    '''
    constructor class, get a widget to be put on.
    '''
    def __init__(self, window_file_panel):
        super(PanelTreeView, self).__init__(window_file_panel.tab_widget)
        self.window_file_panel = window_file_panel
        self.model = QtGui.QFileSystemModel()
        
        self.setModel(self.model)
        self.setItemsExpandable(False)    
        self.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        
        self.setup_connections()
    '''
    setting up tree view connections 
    '''
    def setup_connections(self):
        self.doubleClicked.connect(self.double_clicked_connection)
        
    '''
    this method captures the events and controls then to be handled properly
    '''
    def event(self, event):
        if (event.type() == QtCore.QEvent.KeyPress) :
            if self.key_press_event(event):
                return True

        return super(PanelTreeView, self).event(event)
    
    '''
    this method will create the tab pressed signal which will be listened by commander windows
    to switch between panels
    '''
    def key_press_event(self, event):
        if event.key() == QtCore.Qt.Key_Tab :
            self.emit(QtCore.SIGNAL("tabPressed"))
            return True
        return False
    '''
    this method visually goes deep when current item in the tree is a directory, 
    if the item is not a folder it should try to open the file with OS basis
    '''
    def double_clicked_connection(self, index):
        if index.model().isDir(index):
            self.window_file_panel.goto_folder(index)
    