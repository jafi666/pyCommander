'''
Created on 24/11/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui
from PyQt4 import QtCore


class DialogFileProperties(QtGui.QWidget):

    def __init__(self):
        '''constructor
        initialize all Dialog elements
        '''
        super(DialogFileProperties, self).__init__()
        

    def initUI(self):      

        self.btn = QtGui.QPushButton("okay")
        self.btn.move(20, 20)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        
 
  