'''
Created on 25/11/2014

@author: Jafeth Garcia
'''
import os
from PyQt4 import QtCore, QtGui
from panel_double_click_path import PanelDoubleClickPath
from subprocess import call
from platform import system
from panel_network_dialog import LoginNetwork

class PanelFilePath(QtGui.QWidget):

    def __init__(self, window_file_panel):
        '''constructor
        initializes a widget with a edit line and button to be put on
        WindowFilePanel.

        Keyword arguments:
        :param window_file_panel: an initialized instance (parent widget)
                                  of WindowFilePanel class
        '''
        super(PanelFilePath, self).__init__(window_file_panel.tab_widget)
        self.window_file_panel = window_file_panel

        self.setup_file_path_ui()
        self.setup_connections()

    def setup_file_path_ui(self):
        '''setup path file elements including go to parent button
        used only from constructor
        '''
        self.path_layout = QtGui.QHBoxLayout(self)
        self.path_layout.setMargin(0)
        self.path_layout.setSpacing(0)

        self.path_line_edit = PanelDoubleClickPath(self)
        self.path_line_edit.setReadOnly(True)
        self.path_layout.addWidget(self.path_line_edit)

        self.push_up_dir = QtGui.QPushButton(self)
        self.push_up_dir.setToolTip("Go up folder")
        self.push_up_dir.setIcon(QtGui.QIcon('resources/icon/cdtoparent.png'))
        self.push_up_dir.setIconSize(QtCore.QSize(24, 24))

        self.path_layout.addWidget(self.push_up_dir)

    def setup_connections(self):
        '''setup path and go to parent button connections
        used only from constructor
        '''
        self.push_up_dir.clicked.connect(self.goto_parent_clicked_connection)
        self.path_line_edit.returnPressed.connect(
            self.update_file_path_connection)
        self.connect(self.window_file_panel.tree_view, QtCore.SIGNAL(
            "backspacePressed"), self.goto_parent_clicked_connection)

    def goto_parent_clicked_connection(self):
        '''This connection visually goes to parent folder from current folder
        '''
        if self.window_file_panel.current_folder_name != "":
            parent_index = self.window_file_panel.tree_view.model.index(
                self.window_file_panel.current_folder_path)
            folder_index = self.window_file_panel.tree_view.model.parent(
                parent_index)
            self.window_file_panel.goto_folder(folder_index)

    def update_file_path_connection(self):
        '''This connection visually goes to written path in the path field
        '''
        edit_path = str(self.path_line_edit.text())
        try:
            edit_path.replace("/", "//")
            self.window_file_panel.goto_folder(
                self.window_file_panel.tree_view.model.index(edit_path))
            self.path_line_edit.setReadOnly(True)
        except AttributeError:
            path_contatenated = edit_path.replace("\\\\","")
            path_contatenated = path_contatenated.replace("//","")
            if (os.system("PING -n 2  " + path_contatenated) == 0):
                LoginNetwork(edit_path).exec_()
                self.window_file_panel.goto_folder(
                self.window_file_panel.tree_view.model.index(edit_path))
            else:
                QtGui.QMessageBox.warning(self, 'Error de red','Es posible que el nombre de la ubicacion no este bien escrito o que exista un problema con la red. Para intentar identificar y resolver problemas de red, haga clic en Diagnosticar')




        
        # path_vali = bs[0] + bs[0]+ edit_path
        # print os.path.exists('\\\\localhost')
        # print "FALSE"
        # if (os.path.exists(path_vali)):
        #     edit_path.replace("/", "//")
        #     self.window_file_panel.goto_folder(
        #         self.window_file_panel.tree_view.model.index(edit_path))
        #     self.path_line_edit.setReadOnly(True)
        # else:
        #     path_contatenated = edit_path.replace("\\\\","")
        #     path_contatenated = path_contatenated.replace("//","")
        #     if (os.system("PING -n 2  " + path_contatenated) == 0):
        #         LoginNetwork(edit_path).exec_()
        #     else:
        #         QtGui.QMessageBox.warning(self, 'Error de red','Es posible que el nombre de la ubicacion no este bien escrito o que exista un problema con la red. Para intentar identificar y resolver problemas de red, haga clic en Diagnosticar')
    


