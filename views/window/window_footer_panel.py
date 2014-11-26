'''
Created on Nov 25, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui

class WindowFooterPanel(object):
    '''
    classdocs
    '''
    def __init__(self, commander_window):
        self.commander_window = commander_window
        self.font = QtGui.QFont(self)
        self.font.setBold(True)
        self.font.setWeight(75)
        
        self.setup_footer_panel()
    
    '''
    This method is meant to create all the footer elements on this class
    '''
    def setup_footer_panel(self):
        self.create_footer_push_button("F3 View", "F3")
        self.create_footer_push_button("F4 Edit", "F4")
        self.create_footer_push_button("F5 Copy", "F5")
        self.create_footer_push_button("F6 move", "F6")
        self.create_footer_push_button("F7 New Folder", "F7")
        self.create_footer_push_button("F8 Delete", "F8")
        self.create_footer_push_button("ALT+F4 Exit")
    
    '''
    This method will create a button into footer layout
    '''
    def create_footer_push_button(self, text, shortcut = None, connection = None):
        button = QtGui.QPushButton(self.commander_window.footer_container)
        button.setFont(self.font)
        button.setText(text)
        if (shortcut != None):
            button.setShortcut(shortcut)
        if connection != None :
            button.triggered.connect(connection)
        self.commander_window.footer_layout.addWidget(button)
        
        return button
    