'''
Created on Dec 06, 2014

@author: JorgeX
'''
from PyQt4 import QtGui, QtCore
#from views.dialog.dialog_file_properties import DialogFileProperties

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        self.setGeometry(250, 250 , 500 , 400)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        self.keylist = []
        self.new_list = []

    def handleButton(self):
        modifiers = QtGui.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ShiftModifier:
            print('Shift+Click')
        elif modifiers == QtCore.Qt.ControlModifier:
            print('Control+Click')
        else:
            print('Click')
    
    def keyPressEvent(self, event):
        self.firstrelease = True 
        astr = str(event.key())
        self.keylist.append(astr)

    def keyReleaseEvent(self, event):
        if self.firstrelease == True: 
            self.processmultikeys(self.keylist)
    
        self.firstrelease = False
        del self.keylist[-1]
    
    def processmultikeys(self,keyspressed):
        
        if(len(self.keylist) > 1):
            first_value = self.keylist[0]
            second_value = self.keylist[1]
            print  first_value, type(first_value), second_value, type(second_value)
            if first_value =='16777251' and second_value == '16777220': 
               print "more than 2 keys with Alt + Enter:"
               print  first_value, second_value
        else:
            print keyspressed 
            
        

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())