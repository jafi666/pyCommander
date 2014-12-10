"""
Created on Nov 25, 2014

@author: Jafeth Garcia
"""
from PyQt4 import QtGui


class WindowMenuBar(QtGui.QMenuBar):

    def __init__(self, commander_window):
        """constructor
        initialize all menu bar elements

        Keyword arguments:
        :param commander_window: an initialized instance (parent main window)
                                 of CommanderWindow class
        """
        super(WindowMenuBar, self).__init__(commander_window)
        self.commander_window = commander_window
        self.setup_menu_bar_ui()

    def setup_menu_bar_ui(self):
        """This method is meant to create all the menu elements on this class
        used only from constructor
        """
        self.setup_menu_bar_file()
        self.setup_menu_bar_configuration()
        self.setup_menu_bar_help()

    def setup_menu_bar_file(self):
        """This method is meant to setup up the main menu Files for menu bar
        used only from constructor
        """
        self.menuFile = QtGui.QMenu(self)
        self.menuFile.setTitle("Files")

        # variable to store the add new file connection
        add_new_file_con = self.commander_window.file_manager.add_new_file
        action_new_file = self.create_menu_bar_action("New File",
                                                      "Ctrl+N",
                                                      "Create a new file",
                                                      add_new_file_con)
        self.menuFile.addAction(action_new_file)
        action_quit = self.create_menu_bar_action("Quit", "Ctrl+Q",
                                                  "Exit from Application",
                                                  QtGui.qApp.quit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(action_quit)

        self.addAction(self.menuFile.menuAction())

    def setup_menu_bar_configuration(self):
        """This method is meant to setup up the main menu Configuration for
        menu bar used only from constructor
        """
        self.menuConfiguration = QtGui.QMenu(self)
        self.menuConfiguration.setTitle("Configuration")

        options = self.create_menu_bar_action(
            "Options...", None, "", self.commander_window.open_dialog_options)
        options.setIcon(QtGui.QIcon("resources/icon/options.png"))
        self.menuConfiguration.addAction(options)

        self.addAction(self.menuConfiguration.menuAction())

    def setup_menu_bar_help(self):
        """This method is meant to setup up the main menu Help for menu bar
        used only from constructor
        """
        self.menuHelp = QtGui.QMenu(self)
        self.menuHelp.setTitle("Help")

        action_about = self.create_menu_bar_action("About PyComander...", None,
                                                   "Review About PyCommander\
                                                   Information")
        self.menuHelp.addAction(action_about)

        self.addAction(self.menuHelp.menuAction())

    def create_menu_bar_action(self, text, shortcut=None,
                               tip="", connection=None):
        """This method will create an action for the menu bar
        used only from constructor

        Keyword arguments:
        :param text: text to be set in the action (ie. "File")
        :param shortcut: string sequence of keys or single key for shortcut
                         (ie. "Crtl+Q", default None)
        :param tip: string to set a tool tip (ie. "System File Menu button",
                    default empty)
        :param connection: connection method that will be triggered when Action
                           is clicked (default: None)
        """
        action = QtGui.QAction(self)
        action.setText(text)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip != "":
            action.setStatusTip(tip)
        if connection is not None:
            action.triggered.connect(connection)

        return action
