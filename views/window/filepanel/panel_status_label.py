'''
Created on 25/11/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui


class PanelStatusLabel(QtGui.QWidget):

    def __init__(self, window_file_panel):
        '''constructor
        initialize all panel status elements

        Keyword arguments:
        :param window_file_panel: an initialized instance (parent widget)
                                  of WindowFilePanel class
        '''
        super(PanelStatusLabel, self).__init__(window_file_panel.tab_widget)
        self.window_file_panel = window_file_panel

        self.setup_status_label_ui()

    def setup_status_label_ui(self):
        '''setup the panel status label UI elements
        used only from constructor
        '''
        self.status_layout = QtGui.QHBoxLayout(self)
        self.status_layout.setMargin(0)
        self.status_layout.setSpacing(0)

        self.status_line_edit = QtGui.QLabel(self)
        self.status_line_edit.setText(" / global folder data here")
        self.status_layout.addWidget(self.status_line_edit)
