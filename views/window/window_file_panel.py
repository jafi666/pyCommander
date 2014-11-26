'''
Created on Nov 25, 2014

@author: Jafeth Garcia
'''
import os

from PyQt4 import QtCore, QtGui
from views.window.filepanel.panel_tree_view import PanelTreeView
from views.window.filepanel.panel_file_path import PanelFilePath
from views.window.filepanel.panel_status_label import PanelStatusLabel

class WindowFilePanel(QtGui.QWidget):
    '''
    classdocs
    '''
    def __init__(self, commander_window):
        super(WindowFilePanel, self).__init__(commander_window.body_container)
        self.commander_window = commander_window
        
        self.set_current_folder()
        self.setup_file_panel_ui()
        
        self.goto_folder(self.tree_view.model.index(self.current_folder_path))
        commander_window.body_layout.addWidget(self)
        
        self.setup_connections()
    '''
    Initialize current folder path and name to be used as reference
    '''        
    def set_current_folder(self, current_folder_path = ""):
        if (current_folder_path == ""):
            current_folder_path = os.getcwd()
            current_folder_name = os.path.basename(os.getcwd())
        else:
            current_folder_name = os.path.basename(current_folder_path)
            
        self.current_folder_path = current_folder_path
        self.current_folder_name = current_folder_name
    '''
    setup window panel elements for ui
    '''
    def setup_file_panel_ui(self): 
        # setting up main layout       
        self.main_layout = QtGui.QVBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setMargin(0)
        # setting up tab
        self.tab = QtGui.QTabWidget(self)
        self.tab_widget = QtGui.QWidget()
        self.tab_layout = QtGui.QVBoxLayout(self.tab_widget)
        
        self.path_widget = PanelFilePath(self)
        self.tab_layout.addWidget(self.path_widget)
        # Setting up tree view widget it contains the file system model as attribute
        self.tree_view = PanelTreeView(self)
        self.tab_layout.addWidget(self.tree_view)
        
        self.status_widget = PanelStatusLabel(self)
        self.tab_layout.addWidget(self.status_widget)
        
        self.tab.addTab(self.tab_widget, "")
        self.main_layout.addWidget(self.tab)
    
    '''
    takes the file system model to an specific folder based on the index provided
    it will also visually update the tree view 
    '''
    def goto_folder(self, index):
        self.tree_view.setRootIndex(index)
        self.set_current_folder(str(self.tree_view.model.filePath(index)))
        self.tree_view.model.setRootPath(self.current_folder_path)
        self.path_widget.path_line_edit.setText(self.current_folder_path)
        if self.current_folder_name != "":
            self.tab.setTabText(self.tab.indexOf(self.tab_widget), self.current_folder_name)
        else:
            self.tab.setTabText(self.tab.indexOf(self.tab_widget), self.current_folder_path)
    '''
    setup the connections that will be handled by signals for this tree view
    '''
    def setup_connections(self):
        self.connect(self.tree_view, QtCore.SIGNAL("altEnterPressed"), self.open_properties_connection)
    
    '''
    should open the dialog with selected item(s) in the tree to show their properties
    '''    
    def open_properties_connection(self):
        print "enter pressed"
        