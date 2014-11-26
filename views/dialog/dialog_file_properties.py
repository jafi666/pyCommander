'''
Created on 24/11/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui

class DialogFileProperties(QtGui.QDialog):
    '''
    classdocs
    '''
    def __init__(self, params = None):
        super(DialogFileProperties, self).__init__(params)
        self.setWindowTitle('Properties')
        self.resize(400,700)