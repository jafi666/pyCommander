'''
Created on 7/12/2014

@author: Jafeth Garcia
'''
from libraries import XMLSettings


class WindowConfig(object):

    def __init__(self, commander_window):
        '''constructor
        initialize all file panel elements

        Keyword arguments:
        :param commander_window: an initialized instance (parent main window)
                                 of CommanderWindow class
        '''
        self.commander_window = commander_window
        self.xml = XMLSettings("config/config.xml")
        self.load_window_size()

    def load_window_size(self):
        width = int(self.xml.get("window/size/width", 800))
        height = int(self.xml.get("window/size/height", 600))

        self.commander_window.resize(width, height)
