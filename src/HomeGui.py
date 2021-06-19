#Author: Kamran Hussain
#Date: 4/18/21
#Dependencies

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from AddClass import *


class Home(QDialog):
    def __init__(self):
        super(Home,self).__init__()
        loadUi("home.ui",self)

        self.editCourse1.clicked.connect(addClass())
        self.editCourse2.clicked.connect(self.editCourse2)
        self.editCourse3.clicked.connect(self.editCourse3)
        self.editCourse4.clicked.connect(self.editCourse4)
        self.editCourse5.clicked.connect(self.editCourse5)
        self.editCourse6.clicked.connect(self.editCourse6)
        self.editCourse7.clicked.connect(self.editCourse7)
        self.editCourse8.clicked.connect(self.editCourse8)

        self.launchCourse1.clicked.connect(self.launchCourse1)
        self.launchCourse2.clicked.connect(self.launchCourse2)
        self.launchCourse3.clicked.connect(self.launchCourse3)
        self.launchCourse4.clicked.connect(self.launchCourse4)
        self.launchCourse5.clicked.connect(self.launchCourse5)
        self.launchCourse6.clicked.connect(self.launchCourse6)
        self.launchCourse7.clicked.connect(self.launchCourse7)
        self.launchCourse8.clicked.connect(self.launchCourse8)

    def editCourse1(self, addClass):
        print('course 1 edited')

    def refresh(self):
        print('got here')

app=QApplication(sys.argv)
mainwindow=Home()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1412)
widget.setFixedHeight(948)
widget.show()
app.exec_()