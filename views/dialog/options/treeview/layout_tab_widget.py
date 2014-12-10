'''
Created on Dec 9, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui


class LayoutTabWidget(QtGui.QTabWidget):

    def __init__(self, dialog_options):
        '''Constructor
        initialize all QTabWidget elements, meant for configuration panel

        Keyword arguments:
        :param dialog_options: an initialized instance (parent Dialog)
                               of DialogOptions class
        '''
        super(LayoutTabWidget, self).__init__(dialog_options.base_container)

        self.tab_custom_columns = QtGui.QWidget()
        self.custom_columns_layout = QtGui.QVBoxLayout(self.tab_custom_columns)

        self.addTab(self.tab_custom_columns, "General")

        dialog_options.base_container_layout.addWidget(self)
