#Author: Kamran Hussain
#Date: 6/18/21
#Dependencies: PyQt5, home.ui, homegui.py,

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

#adds class
class AddClass(QDialog):
    def __init__(self):
        super(AddClass,self).__init__()
        loadUi("addClassGUI.ui",self)
        self.classEntered.clicked.connect(self.classDataInput)

    def classDataInput(self):
        courseName=self.className.text()
        courseLink=self.classLink.text()
        meetingLink=self.meetingLink.text()
        print("All Class Data entered")
        print("Class Name: " + courseName)
        print("Class Link: " + courseLink)
        print("Meeting Link: " + meetingLink)
        AddClass.close()

    def getCourseName(self):
        courseName=self.className.text()
        return courseName

    def getCourseLink(self):
        courseLink = self.classLink.text()
        return courseLink

    def getMeetingLink(self):
        meetingLink = self.meetingLink.text()
        return meetingLink

app=QApplication(sys.argv)
mainwindow=AddClass()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(710)
widget.setFixedHeight(512)
widget.show()
app.exec_()