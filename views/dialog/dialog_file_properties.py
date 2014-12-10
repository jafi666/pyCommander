'''
Created on 24/11/2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui
from PyQt4 import QtCore


class DialogFileProperties(object):

    def __init__(self):
        '''constructor
        initialize all Dialog elements
        '''
        super(DialogFileProperties, self).__init__()
        self.initUI()

    def initUI(self):      

        self.btn = QtGui.QPushButton(self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
#        self.show()
        
    def showDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))
  