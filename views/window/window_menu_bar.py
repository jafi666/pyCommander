'''
Created on Nov 25, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui

class WindowMenuBar(QtGui.QMenuBar):
    '''
    Constructor of menu bar for main window
    '''
    def __init__(self, commander_window):
        super(WindowMenuBar, self).__init__(commander_window)
        self.commander_window = commander_window
        self.setup_menu_bar_ui()
        
    '''
    This method is meant to create all the menu elements on this class
    '''
    def setup_menu_bar_ui(self):
        self.setup_menu_bar_file()
        self.setup_menu_bar_configuration()
        self.setup_menu_bar_help()
    
    '''
    This method is meant to setup up the main menu Files for menu bar 
    '''
    def setup_menu_bar_file(self):
        self.menuFile = QtGui.QMenu(self)
        self.menuFile.setTitle("Files")
        self.menuFile.addSeparator()
        
        action_new_file = self.create_menu_bar_action("New File", "Ctrl+N", "Create a new file", self.commander_window.file_manager.add_new_file)
        self.menuFile.addAction(action_new_file)
        action_quit = self.create_menu_bar_action("Quit", "Ctrl+Q", "Exit from Application", QtGui.qApp.quit)
        self.menuFile.addAction(action_quit)
        
        
        self.addAction(self.menuFile.menuAction())
    
    '''
    This method is meant to setup up the main menu Configuration for menu bar 
    '''
    def setup_menu_bar_configuration(self):
        self.menuConfiguration = QtGui.QMenu(self)
        self.menuConfiguration.setTitle("Configuration")
        self.addAction(self.menuConfiguration.menuAction())
    
    '''
    This method is meant to setup up the main menu Help for menu bar 
    '''
    def setup_menu_bar_help(self):
        self.menuHelp = QtGui.QMenu(self)        
        self.menuHelp.setTitle("Help")
        
        action_about = self.create_menu_bar_action("About PyComander...", None, "Review About PyCommander Information")
        self.menuHelp.addAction(action_about)
        
        self.addAction(self.menuHelp.menuAction())
    
    '''
    This method will create an action for the menu bar
    '''
    def create_menu_bar_action(self, text, shortcut = None, tip = "", connection = None):
        action = QtGui.QAction(self)
        action.setText(text)
        if (shortcut != None):
            action.setShortcut(shortcut)
        if (tip != "") :
            action.setStatusTip(tip)
        if connection != None :
            action.triggered.connect(connection)
        
        return action
