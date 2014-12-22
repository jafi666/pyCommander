import os
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from platform import system
from smb.SMBConnection import SMBConnection
import socket

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class LoginNetwork(QtGui.QDialog):
    def __init__(self, ip_address):
        '''constructor
        initializes al required qtgui objects for set Network credential dialog box
        
        Keyword arguments:
        :param ip_address: an initialized instance (parent widget)
                                  of WindowFilePanel class
        '''
        self.ip_address=ip_address
        QtGui.QDialog.__init__(self)
        self.setWindowTitle('PyCommander')
        self.declare_QtGuies()
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.lbl1)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.cb)

    def declare_QtGuies(self):
        '''Method used by constructor to declare and set  qtgui objects values, it is only used from constructor
        '''
        self.lbl1 = QtGui.QLabel('Enter you credential to connect to: ' + self.ip_address, self)
        self.button = PicButton(QPixmap("index2.jpg"))
        self.button.resize(5,5)
        self.textName = QtGui.QLineEdit(self)
        self.textName.setPlaceholderText("User name e.g. Domain\user ") 
        self.textPass = QtGui.QLineEdit(self)
        self.textPass.setPlaceholderText("Password")
        self.buttonLogin = QtGui.QPushButton('Connect', self)
        self.buttonLogin.clicked.connect(self.determine_platform)
        self.cb = QtGui.QCheckBox('Remember Password', self)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.change_title)

    def determine_platform(self):
        '''Method used to verify if the Client is Linux or windows
        '''
        os_platform= system()
        if os_platform == 'Windows':         
            self.handle_windows_login()
        else:
            self.handle_linux_login()

    def handle_windows_login(self):
        '''Method used to set the Network connection to windows share with the credential  passed by final user
        '''
        ip_address_concatenated = self.ip_address
        ip_address_concatenated = str("\\\\" + ip_address_concatenated)
        username_concatenated = self.textName.text()
        username_concatenated = str(username_concatenated.replace("\\","\\\\"))
        password = self.textPass.text()
        command_query = str('NET USE ' + ip_address_concatenated + ' ' + password + ' /USER:"'+ username_concatenated +'"')
        validation = os.system(command_query)
        
        if validation == 0 :
            QtGui.QMessageBox.information(self, "Authentication successfull","Now, you are already connected to share folder.")
        if validation == 2 :
            QtGui.QMessageBox.warning(self, 'Multiple connections',  "Multiple connections to a server or shared resource by the same user")
        else:
            QtGui.QMessageBox.warning(self, 'Bad credential Error', 'You entered bad user or password, please try again')
          
    def handle_linux_login(self):
        '''Method used to set the Network connection to Samba share with the credential  passed by final user
        '''
        server_name = self.ip_address
        server_name = server_name.replace("\\\\","")
        client_name = socket.gethostname()
        username_concatenated = self.textName.text()
        username_concatenated = str(username_concatenated.replace("\\","\\\\"))
        password = self.textPass.text()
        try:
            s = SMBConnection(username_concatenated, password, client_name, server_name, use_ntlm_v2 = True)
            s.connect(server_name, 139)
            filelist = s.listShares()
        except AttributeError:
            QtGui.QMessageBox.warning(self, 'Multiple connections',  "Multiple connections to a server or shared resource by the same user")
