'''
Created on 25/11/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui

class PanelFilePath(QtGui.QWidget):
    '''
    classdocs
    '''
    def __init__(self, window_file_panel):
        super(PanelFilePath, self).__init__(window_file_panel.tab_widget)
        self.window_file_panel = window_file_panel
        
        self.setup_file_path_ui()
        self.setup_connections()
    '''
    setup path file elements including go to parent button
    '''
    def setup_file_path_ui(self):
        self.path_layout = QtGui.QHBoxLayout(self)
        self.path_layout.setMargin(0)
        self.path_layout.setSpacing(0)
        
        self.path_line_edit = QtGui.QLineEdit(self)
        self.path_line_edit.setEnabled(False)
        self.path_layout.addWidget(self.path_line_edit)
        
        self.push_up_dir = QtGui.QPushButton(self)
        self.push_up_dir.setToolTip("Go up folder")
        self.push_up_dir.setIcon(QtGui.QIcon('resources/icon/cdtoparent.png'))
        self.push_up_dir.setIconSize(QtCore.QSize(24,24))
        
        self.path_layout.addWidget(self.push_up_dir)
    '''
    setup path and go to parent button connections
    '''
    def setup_connections(self):
        self.push_up_dir.clicked.connect(self.goto_parent_clicked_connection)
        
    '''
    this connection visually goes to parent folder from current folder
    '''    
    def goto_parent_clicked_connection(self):
        if self.window_file_panel.current_folder_name != "":
            parent_index = self.window_file_panel.tree_view.model.index(self.window_file_panel.current_folder_path)
            folder_index = self.window_file_panel.tree_view.model.parent(parent_index)
            self.window_file_panel.goto_folder(folder_index)
    
    