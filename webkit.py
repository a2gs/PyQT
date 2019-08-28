#!/usr/bin/env python3

# https://pythonspot.com/pyqt5-browser/

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("https://pythonspot.com"))
web.show()

sys.exit(app.exec_())