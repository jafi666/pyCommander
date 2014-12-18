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
        self.setup_menu_bar_command()
        self.setup_menu_bar_configuration()
        self.setup_menu_bar_help()

    def setup_menu_bar_file(self):
        """This method is meant to setup up the main menu Files for menu bar
        used only from constructor
        """
        self.menu_file = QtGui.QMenu(self)
        self.menu_file.setTitle("Files")

        # variable to store the add new file connection
        add_new_file_con = self.commander_window.file_manager.add_new_file
        action_new_file = self.create_menu_bar_action("New File",
                                                      "Ctrl+N",
                                                      "Create a new file",
                                                      add_new_file_con)
        action_new_file.setIcon(QtGui.QIcon("resources/icon/new.png"))
        self.menu_file.addAction(action_new_file)
        self.menu_file.addSeparator()

        action_select_all = self.create_menu_bar_action("Select All Files",
                                                        "Ctrl+Num++",
                                                        "Select all files",
                                                        self.commander_window.select_all_files)
        action_select_all.setIcon(QtGui.QIcon("resources/icon/selectall.png"))
        self.menu_file.addAction(action_select_all)

        action_unselect_all = self.create_menu_bar_action("Unselect All Files",
                                                          "Ctrl+Num+-",
                                                          "Unselect all files",
                                                          self.commander_window.unselect_all_files)
        self.menu_file.addAction(action_unselect_all)
        action_rename_tool = self.create_menu_bar_action("Multi-Rename Tool...",
                                                         "Ctrl+M")
        action_rename_tool.setIcon(QtGui.QIcon("resources/icon/mrename.png"))
        self.menu_file.addAction(action_rename_tool)
        self.menu_file.addSeparator()
        action_quit = self.create_menu_bar_action("Quit", "Ctrl+Q",
                                                  "Exit from Application",
                                                  QtGui.qApp.quit)
        self.menu_file.addAction(action_quit)

        self.addAction(self.menu_file.menuAction())

    def setup_menu_bar_command(self):
        """This method is meant to setup up the main menu Commands for
        menu bar used only from constructor
        """
        self.menu_command = QtGui.QMenu(self)
        self.menu_command.setTitle("Commands")
        action_search = self.create_menu_bar_action(
            "Search...", "Alt+F7")
        action_search.setIcon(
            QtGui.QIcon("resources/icon/search.png"))
        self.menu_command.addAction(action_search)

        action_navigation_up = self.create_menu_bar_action(
            "Go up folder")
        action_navigation_up.setIcon(
            QtGui.QIcon("resources/icon/cdtoparent.png"))
        self.menu_command.addAction(action_navigation_up)
        self.menu_command.addSeparator()

        action_list_view = self.create_menu_bar_action(
            "Full List View", "Ctrl+F2")
        action_list_view.setIcon(
            QtGui.QIcon("resources/icon/detailview.png"))
        self.menu_command.addAction(action_list_view)

        action_icon_view = self.create_menu_bar_action(
            "Thumbnail view", "Ctrl+Shift+F1")
        action_icon_view.setIcon(
            QtGui.QIcon("resources/icon/iconview.png"))
        self.menu_command.addAction(action_icon_view)

        self.addAction(self.menu_command.menuAction())

    def setup_menu_bar_configuration(self):
        """This method is meant to setup up the main menu Configuration for
        menu bar used only from constructor
        """
        self.menu_configuration = QtGui.QMenu(self)
        self.menu_configuration.setTitle("Configuration")

        options = self.create_menu_bar_action(
            "Options...", None, "", self.commander_window.open_dialog_options)
        options.setIcon(QtGui.QIcon("resources/icon/options.png"))
        self.menu_configuration.addAction(options)

        self.addAction(self.menu_configuration.menuAction())

    def setup_menu_bar_help(self):
        """This method is meant to setup up the main menu Help for menu bar
        used only from constructor
        """
        self.menu_help = QtGui.QMenu(self)
        self.menu_help.setTitle("Help")

        action_about = self.create_menu_bar_action("About PyComander...", None,
                                                   "Review About PyCommander\
                                                   Information")
        self.menu_help.addAction(action_about)

        self.addAction(self.menu_help.menuAction())

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
