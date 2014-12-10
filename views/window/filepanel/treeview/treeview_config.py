'''
Created on 7/12/2014

@author: Jafeth Grcia
'''
from libraries import XMLSettings


class TreeviewConfig(object):

    def __init__(self, panel_tree_view):
        '''constructor
        initializes an object with a PanelTreeView as main attribute passed by
        reference

        Keyword arguments:
        :param panel_tree_view: an initialized instance (parent TreeView)
                                of PanelTreeView class
        '''
        self.panel_tree_view = panel_tree_view
        self.xml = XMLSettings("config/config.xml")
        self.load_columns()

    def load_columns(self):
        '''Determines what columns are going to be displayed
        data is gotten from config.xml
        '''
        column_size = self.xml.get("treeview/showColumns/size", 0)
        self.panel_tree_view.showColumn(1)
        if not column_size:
            self.panel_tree_view.hideColumn(1)

        column_type = self.xml.get("treeview/showColumns/type", 0)
        self.panel_tree_view.showColumn(2)
        if not column_type:
            self.panel_tree_view.hideColumn(2)

        column_date_modified = self.xml.get(
            "treeview/showColumns/dateModified", 0)
        self.panel_tree_view.showColumn(3)
        if not column_date_modified:
            self.panel_tree_view.hideColumn(3)
