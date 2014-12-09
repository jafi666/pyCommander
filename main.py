'''
Created on 21/11/2014

@author: jabber
'''

import sys

from PyQt4 import QtGui
from views.commander_window import CommanderWindow


def main():
    app = QtGui.QApplication(sys.argv)
    window = CommanderWindow()
    window.show()
    sys.exit(app.exec_())

############################################################################
if __name__ == '__main__':
    main()
