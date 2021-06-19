# Author: Kamran Hussain
# Date: 4/18/21
# Dependencies

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()

        loadUi("homeGui.ui", self)
        self.editCourse1.clicked.connect(lambda: print("edit 1 hit"))

app = QApplication(sys.argv)
mainwindow = Home()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

widget.show()
app.exec_()