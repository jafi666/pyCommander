'''
Created on Nov 25, 2014

@author: Jafeth Garcia
'''
import os

from PyQt4 import QtCore, QtGui
from os.path import expanduser
from views.window.filepanel.panel_tree_view import PanelTreeView
from views.window.filepanel.panel_file_path import PanelFilePath
from views.window.filepanel.panel_status_label import PanelStatusLabel


class WindowFilePanel(QtGui.QWidget):

    def __init__(self, commander_window):
        '''constructor
        initialize all file panel elements

        Keyword arguments:
        :param commander_window: an initialized instance (parent main window)
                                 of CommanderWindow class
        '''
        super(WindowFilePanel, self).__init__(commander_window.body_container)
        self.commander_window = commander_window
        self.active = False
        self.set_current_folder()
        self.setup_file_panel_ui()

        self.goto_folder(self.tree_view.model.index(self.current_folder_path))
        commander_window.body_layout.addWidget(self)

        self.setup_connections()

    def set_current_folder(self, current_folder_path=""):
        '''Initialize current folder path and name to be used as reference

        Keyword arguments:
        :param current_folder_path: a string var of desired file system path
                                    (ie. C:\windows\foo\bar)
        '''
        if current_folder_path == "":
            # when no default current folder path is passed as argument
            # it gets the user's home directory
            current_folder_path = expanduser("~")
            current_folder_name = os.path.basename(current_folder_path)
        else:
            current_folder_name = os.path.basename(current_folder_path)

        self.current_folder_path = current_folder_path
        self.current_folder_name = current_folder_name

    def setup_file_panel_ui(self):
        '''setup window panel elements for UI
        used only from constructor
        '''
        # setting up main layout
        self.main_layout = QtGui.QVBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setMargin(0)

        # setting up tab
        self.tab = QtGui.QTabWidget(self)
        self.tab_widget = QtGui.QWidget()
        self.tab_layout = QtGui.QVBoxLayout(self.tab_widget)

        self.tree_view = PanelTreeView(self)

        self.path_widget = PanelFilePath(self)
        self.tab_layout.addWidget(self.path_widget)

        # Setting up tree view widget it contains the file system model as
        # attribute
        self.tab_layout.addWidget(self.tree_view)

        self.status_widget = PanelStatusLabel(self)
        self.tab_layout.addWidget(self.status_widget)

        self.tab.addTab(self.tab_widget, "")
        self.main_layout.addWidget(self.tab)

    def goto_folder(self, index):
        '''takes the file system model to an specific folder based on the
        index provided it will also visually update the tree view

        Keyword arguments:
        :param index: a QModelIndex variable used to set the root index
                      of TreeView
        '''
        # left index represent the index with current selected row and first
        # column
        left_index = index.model().index(
            index.row(), 0, index.model().parent(index))
        self.tree_view.setRootIndex(left_index)
        self.set_current_folder(str(self.tree_view.model.filePath(left_index)))
        self.tree_view.model.setRootPath(self.current_folder_path)
        self.path_widget.path_line_edit.setText(self.current_folder_path)
        if self.current_folder_name != "":
            self.tab.setTabText(
                self.tab.indexOf(self.tab_widget), self.current_folder_name)
        else:
            self.tab.setTabText(
                self.tab.indexOf(self.tab_widget), self.current_folder_path)

    def setup_connections(self):
        '''setup the connections that will be handled by signals for this tree view
        used only from constructor
        '''
        self.connect(self.tree_view, QtCore.SIGNAL(
            "altEnterPressed"), self.open_properties_connection)

    def open_properties_connection(self):
        '''should open the dialog with selected item(s) in the tree to show
        their properties
        TODO: functionality should be included in future iterations
        '''
        pass
