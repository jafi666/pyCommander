'''
Created on Dec 9, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui
from libraries import XMLSettings
from views.dialog.options.options_tree_view import OptionsTreeWidget


class DialogOptions(QtGui.QDialog):

    def __init__(self, commander_window):
        '''Constructor
        initialize all Configuration Dialog elements

        Keyword arguments:
        :param commander_window: an initialized instance (parent main window)
                                 of CommanderWindow class
        '''
        super(DialogOptions, self).__init__(commander_window)
        self.commander_window = commander_window
        self.xml = XMLSettings("config/config.xml")
        self.size = QtCore.QSize(580, 490)
        self.setWindowTitle("Configuration")
        self.resize(self.size)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(self.size)
        self.setMaximumSize(self.size)

        self.__setup_dialog_ui()

    def __setup_dialog_ui(self):
        '''This method is meant to initialize UI elements into the main
        Dialog.
        '''
        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setAutoFillBackground(False)
        self.central_layout = QtGui.QVBoxLayout(self)

        self.setup_config_panel()
        self.__setup_options_panel()

        self.central_layout.addWidget(self.central_widget)

        self.__setup_button_box()

    def __setup_options_panel(self):
        '''This method is meant to set the tree view panel UI which is the
        key to load all configuration panels in the main Dialog.
        '''
        self.option_tree_widget = OptionsTreeWidget(self)

    def setup_config_panel(self):
        '''This method initializes a main base container for the configuration panel
        the treeview options panel is the one which will call this method
        according the configuration panel required
        '''
        self.base_container = QtGui.QGroupBox(self.central_widget)
        self.base_container.setGeometry(QtCore.QRect(160, 0, 401, 435))

        self.base_container_layout = QtGui.QVBoxLayout(self.base_container)

    def __setup_button_box(self):
        '''This method is meant to set the button group box in the main Dialog
        '''
        self.button_box = QtGui.QDialogButtonBox(self)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.central_layout.addWidget(self.button_box)

        QtCore.QObject.connect(
            self.button_box, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(
            self.button_box, QtCore.SIGNAL("rejected()"), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
