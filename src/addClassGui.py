#Author: Kamran Hussain
#Date: 6/17/21

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class AddCourse(QDialog):
    def __init__(self):
        super(AddCourse,self).__init__()
        loadUi("home.ui",self)
        self.classEntered.clicked.connect(self.classMaterialEntered)

    def classMaterialEntered(self):
        courseName=self.className.text()
        courseLink=self.classLink.text()
        meetingLink=self.meetingLink.text()
        otherLink=self.otherLink.text()
        print('All Class input data was gathered')
        print('Class Name: '+ courseName)
        print('Class Link: '+ courseLink)
        print('Meeting Link: '+ meetingLink)
        print('Other Link: '+ otherLink)

app=QApplication(sys.argv)
mainwindow=AddCourse()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
app.exec_()
