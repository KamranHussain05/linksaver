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
        self.setMinimumSize(1451, 891)
        loadUi("homeGui.ui", self)
        self.editCourse1.clicked.connect(lambda: self.editCourse_1())
        self.editCourse2.clicked.connect(lambda: self.editCourse_2())
        self.editCourse3.clicked.connect(lambda: self.editCourse_3())
        self.editCourse4.clicked.connect(lambda: self.editCourse_4())
        self.editCourse5.clicked.connect(lambda: self.editCourse_5())
        self.editCourse6.clicked.connect(lambda: self.editCourse_6())
        self.editCourse7.clicked.connect(lambda: self.editCourse_7())
        self.editCourse8.clicked.connect(lambda: self.editCourse_8())

        self.launchCourse1.clicked.connect(lambda: self.launchCourse_1())
        self.launchCourse2.clicked.connect(lambda: self.launchCourse_2())
        self.launchCourse3.clicked.connect(lambda: self.launchCourse_3())
        self.launchCourse4.clicked.connect(lambda: self.launchCourse_4())
        self.launchCourse5.clicked.connect(lambda: self.launchCourse_5())
        self.launchCourse6.clicked.connect(lambda: self.launchCourse_6())
        self.launchCourse7.clicked.connect(lambda: self.launchCourse_7())
        self.launchCourse8.clicked.connect(lambda: self.launchCourse_8())

        self.settings.clicked.connect(lambda: self.launchSettings)
        self.help.clicked.connect(lambda: self.launchHelp)

    def editCourse_1(self):
        print('Editing Course 1')

    def editCourse_2(self):
        print('Editing Course 2')

    def editCourse_3(self):
        print('Editing Course 3')

    def editCourse_4(self):
        print('Editing Course 4')

    def editCourse_5(self):
        print('Editing Course 5')

    def editCourse_6(self):
        print('Editing Course 6')

    def editCourse_7(self):
        print('Editing Course 7')

    def editCourse_8(self):
        print('Editing Course 8')

    # ______________________________________

    def launchCourse_1(self):
        print('Launching Course 1')

    def launchCourse_2(self):
        print('Launching Course 2')

    def launchCourse_3(self):
        print('Launching Course 3')

    def launchCourse_4(self):
        print('Launching Course 4')

    def launchCourse_5(self):
        print('Launching Course 5')

    def launchCourse_6(self):
        print('Launching Course 6')

    def launchCourse_7(self):
        print('Launching Course 7')

    def launchCourse_8(self):
        print('Launching Course 8')

    # __________________________________________
    def launchSettings(self):
        print('Settings Launched')

    def launchHelp(self):
        print('Help Website Launched')


app = QApplication(sys.argv)
mainwindow = Home()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
app.exec_()
