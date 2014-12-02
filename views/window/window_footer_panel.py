'''
Created on Nov 25, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui

class WindowFooterPanel(object):
    
    def __init__(self, commander_window):
        '''constructor
        initialize all footer panel elements
        
        Keyword arguments:
        commander_window -- an initialized instance (parent main window) of CommanderWindow class
        '''
        self.commander_window = commander_window
        self.font = QtGui.QFont(self)
        self.font.setBold(True)
        self.font.setWeight(75)
        
        self.setup_footer_panel()
    
    def setup_footer_panel(self):
        '''This method is meant to create all the footer elements on this class
        used only from constructor
        '''
        self.create_footer_push_button("F3 View", "F3")
        self.create_footer_push_button("F4 Edit", "F4")
        self.create_footer_push_button("F5 Copy", "F5")
        self.create_footer_push_button("F6 move", "F6")
        self.create_footer_push_button("F7 New Folder", "F7")
        self.create_footer_push_button("F8 Delete", "F8")
        self.create_footer_push_button("ALT+F4 Exit")
    
    def create_footer_push_button(self, text, shortcut = None, connection = None):
        '''This method will create a button into footer layout
        
        Keyword arguments:
        text -- text to be set in the action (ie. "View")
        shortcut -- string sequence of keys or single key for shortcut (ie. "F3", default None)
        connection -- connection method that will be triggered when Action is clicked (default: None)
        '''
        button = QtGui.QPushButton(self.commander_window.footer_container)
        button.setFont(self.font)
        button.setText(text)
        if (shortcut != None):
            button.setShortcut(shortcut)
        if connection != None :
            button.triggered.connect(connection)
        self.commander_window.footer_layout.addWidget(button)
        
        return button
    