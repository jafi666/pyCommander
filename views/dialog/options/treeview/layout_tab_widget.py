'''
Created on Dec 9, 2014

@author: jafeth garcia
'''
from PyQt4 import QtGui


class LayoutTabWidget(QtGui.QTabWidget):

    '''
    classdocs
    '''

    def __init__(self, dialog_options):
        '''
        Constructor
        '''
        super(LayoutTabWidget, self).__init__(dialog_options.base_container)

        self.tab_custom_columns = QtGui.QWidget()
        self.custom_columns_layout = QtGui.QVBoxLayout(self.tab_custom_columns)

        self.addTab(self.tab_custom_columns, "General")

        dialog_options.base_container_layout.addWidget(self)
