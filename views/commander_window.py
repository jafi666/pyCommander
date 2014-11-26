'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui
from views.window.window_file_panel import WindowFilePanel
from views.window.window_menu_bar import WindowMenuBar
from views.window.window_footer_panel import WindowFooterPanel

class CommanderWindow(QtGui.QMainWindow):
    '''
    constructor
    initialize all Main Window elements
    '''
    def __init__(self):
        super(CommanderWindow, self).__init__()
        
        self.resize(1024, 800)
        self.setWindowTitle("PyCommander")
        
        self.setup_window_ui()
    
    '''
    setup_window_ui
    This method is part of constructor method and meant to be only called by constructor
    '''    
    def setup_window_ui(self):
        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setAutoFillBackground(False)
        self.central_layout = QtGui.QVBoxLayout(self.central_widget)
        
        self.setup_body_footer_ui()
        self.setup_menu_bar_ui()
        self.setup_status_bar_ui()
        self.setup_connections()
        
        QtCore.QMetaObject.connectSlotsByName(self)
    
    '''
    setup_body_footer_ui
    This method is part of constructor meant to be only called by constructor
    '''
    def setup_body_footer_ui(self):
        # Setting up body container where panels with system files with be created
        self.body_container = QtGui.QSplitter(self.central_widget)
        self.body_layout = QtGui.QHBoxLayout(self.body_container)
        self.body_layout.setMargin(0)
        # Setting up tab commander panels
        self.tab_left = WindowFilePanel(self)
        self.tab_right = WindowFilePanel(self)
        self.central_layout.addWidget(self.body_container)
        # Setting up footer container where quick buttons will be created
        self.footer_container = QtGui.QFrame(self.central_widget)
        self.footer_layout = QtGui.QHBoxLayout(self.footer_container)
        self.footer_layout.setMargin(0)
        # Setting up footer components
        self.setup_footer_ui()
        self.central_layout.addWidget(self.footer_container)
        # adding the main central widget for the main window
        self.setCentralWidget(self.central_widget)
    
    '''
    This method is meant to create the menu bar of this window
    '''
    def setup_menu_bar_ui(self):
        self.menubar = WindowMenuBar(self)        
        self.setMenuBar(self.menubar)
    
    '''
    This method is meant to create the status bar of this window
    '''
    def setup_status_bar_ui(self):
        self.statusbar = QtGui.QStatusBar(self)        
        self.setStatusBar(self.statusbar)
    '''
    This method is meant to create the footer push button elemensts
    '''            
    def setup_footer_ui(self):
        self.footer = WindowFooterPanel(self);
        
    '''
    this method is meant to initiate any connection with window commander
    '''
    def setup_connections(self):
        self.connect(self.tab_left.tree_view, QtCore.SIGNAL("tabPressed"), self.switch_to_right_panel_connection)
        self.connect(self.tab_right.tree_view, QtCore.SIGNAL("tabPressed"), self.switch_to_left_panel_connection)
    
    '''
    action to switch from panel right to left panel
    '''
    def switch_to_left_panel_connection(self):
        self.tab_left.tree_view.setFocus()
    
    '''
    action to switch from panel left to right panel
    '''
    def switch_to_right_panel_connection(self):
        self.tab_right.tree_view.setFocus()
    