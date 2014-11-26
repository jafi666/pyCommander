'''
Created on 25/11/2014

@author: jabber
'''
from PyQt4 import QtGui

class PanelStatusLabel(QtGui.QWidget):
    '''
    classdocs
    '''
    def __init__(self, window_file_panel):
        super(PanelStatusLabel, self).__init__(window_file_panel.tab_widget)
        self.window_file_panel = window_file_panel
        
        self.setup_statu_label_ui()
    '''
    setup the panel status label ui elements
    '''
    def setup_statu_label_ui(self):
        self.status_layout = QtGui.QHBoxLayout(self)
        self.status_layout.setMargin(0)
        self.status_layout.setSpacing(0)
        
        self.status_line_edit = QtGui.QLabel(self)
        self.status_line_edit.setText(str(self.window_file_panel.tree_view.model.rowCount(self.window_file_panel.tree_view.model.index(self.window_file_panel.current_folder_path))) + " / global folder data here")
        self.status_layout.addWidget(self.status_line_edit)
    