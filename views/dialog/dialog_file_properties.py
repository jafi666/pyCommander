'''
Created on 24/11/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui


class DialogFileProperties(QtGui.QDialog):

    def __init__(self):
        '''constructor
        initialize all Dialog elements
        '''
        super(DialogFileProperties, self).__init__()
        self.setWindowTitle('Properties')
        self.resize(self.minimumSizeHint())
