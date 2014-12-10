'''
Created on Dec 9, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtGui, QtCore


class DisplayTabWidget(QtGui.QTabWidget):
    '''
    This class in particular will handle all configuration related Display
    options
    '''

    def __init__(self, dialog_options):
        '''Constructor
        initialize all QTabWidget elements, meant for configuration panel

        Keyword arguments:
        :param dialog_options: an initialized instance (parent Dialog)
                               of DialogOptions class
        '''
        super(DisplayTabWidget, self).__init__(dialog_options.base_container)
        self.dialog_options = dialog_options
        self.tab_custom_columns = QtGui.QWidget()
        self.custom_columns_layout = QtGui.QVBoxLayout(self.tab_custom_columns)
        self.custom_columns_layout.setAlignment(QtCore.Qt.AlignTop)

        self.__load_custom_columns()
        self.addTab(self.tab_custom_columns, "Custom columns")

        self.dialog_options.base_container_layout.addWidget(self)

    def __load_custom_columns(self):
        '''This method is part of UI initialization, for this configuration
        it will be created customer column check boxes here
        '''
        group_box = QtGui.QGroupBox(self.tab_custom_columns)
        group_box.setTitle("Viewable Columns")
        group_layout = QtGui.QVBoxLayout(group_box)

        checkbox_name = self.configure_custom_column_checkbox(
            group_box, 0, "Column name", "treeview/showColumns/name")
        checkbox_name.setEnabled(False)
        group_layout.addWidget(checkbox_name)

        checkbox_size = self.configure_custom_column_checkbox(
            group_box, 1, "Column size", "treeview/showColumns/size")
        group_layout.addWidget(checkbox_size)

        checkbox_type = self.configure_custom_column_checkbox(
            group_box, 2, "Column type", "treeview/showColumns/type")
        group_layout.addWidget(checkbox_type)

        checkbox_date = self.configure_custom_column_checkbox(
            group_box, 3, "Column size", "treeview/showColumns/dateModified")
        group_layout.addWidget(checkbox_date)
        self.custom_columns_layout.addWidget(group_box)

    def configure_custom_column_checkbox(self, parent, column, text, xpath):
        '''This method is part of custom columns check boxes configuration,
        this method is a helper to avoid duplication creating check boxes, here
        check boxes are created and associated with a generic connection method

        :param parent: a UI widget element that will hold the check box,
        example a QGroupBox
        :param column: an integer value which represent the column index
        associated with the checkbox
        :param text: string value to be set in the checkbox text.
        :param xpath: string path to access the column configuration in the
        config.xml file (example: 'treeview/showColumns/dateModified')
        '''
        checkbox = QtGui.QCheckBox(parent)
        checkbox.setText(text)

        if self.dialog_options.xml.get(xpath, 0):
            checkbox.setChecked(True)

        checkbox.clicked.connect(
            lambda: self.checkbox_click_connection(checkbox, xpath, column))
        return checkbox

    def checkbox_click_connection(self, checkbox, xpath, column):
        '''This method is a generic connection that should be related with a
        checkbox, in order to select and unselect a column, this method will
        also perform de UI change

        :param checkbox: the checkbox QCheckBox element, which will provided
        checked status
        :param xpath: string path to access the column configuration in the
        config.xml file (example: 'treeview/showColumns/dateModified')
        :param column: an integer value which represent the column index
        associated with the checkbox
        '''
        commander_window = self.dialog_options.commander_window
        if checkbox.isChecked():
            commander_window.tab_left.tree_view.showColumn(column)
            commander_window.tab_right.tree_view.showColumn(column)
            new_config_value = 1
        else:
            commander_window.tab_left.tree_view.hideColumn(column)
            commander_window.tab_right.tree_view.hideColumn(column)
            new_config_value = 0

        self.dialog_options.xml.put(xpath, new_config_value)
        self.dialog_options.xml.save()
