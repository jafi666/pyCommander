'''
Created on Dec 9, 2014

@author: jafeth garcia
'''
from PyQt4 import QtCore, QtGui
from views.dialog.options.treeview import LayoutTabWidget

_fromList = ["DisplayTabWidget", "LayoutTabWidget"]
_tree_item_list = ["Layout", "Display"]


class OptionsTreeWidget(QtGui.QTreeWidget):

    def __init__(self, dialog_options):
        '''
        Constructor
        '''
        super(OptionsTreeWidget, self).__init__(dialog_options.central_widget)
        self.dialog_options = dialog_options
        self.setGeometry(QtCore.QRect(0, 0, 150, 435))
        self.setIndentation(10)
        self.headerItem().setText(0, "Options")
        self.header().setVisible(False)
        self.configuration_widget = LayoutTabWidget(self.dialog_options)
        self.__setup_widget_ui()
        self.selectionModel().select(
            self.model().index(0, 0), QtGui.QItemSelectionModel.Select)

    def __setup_widget_ui(self):
        '''
        '''
        for tree_item_name in _tree_item_list:
            tree_item = QtGui.QTreeWidgetItem(self)
            tree_item.setText(0, tree_item_name)

        self.itemClicked.connect(self.show_custom_configuration_content)

    def show_custom_configuration_content(self, item):
        '''
        '''
        mod = __import__('views.dialog.options.treeview', fromlist=_fromList)
        if self.configuration_widget is not None:
            self.configuration_widget.setParent(None)

        target_class = getattr(
            mod, str(item.text(0) + "TabWidget"))

        self.configuration_widget = target_class(self.dialog_options)
