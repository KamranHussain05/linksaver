#Author: Kamran Hussain
#Date: 4/18/21
#Dependencies

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

#adds class
class Home(QDialog):
    def __init__(self):
        super(Home,self).__init__()
        loadUi("home.ui",self)
        self.editCourse1.clicked.connect(self.editCourse1)

    def editCourse1(self):
        addClass()

    def classDataInput(self):
        courseName=self.className.text()
        courseLink=self.classLink.text()
        meetingLink=self.meetingLink.text()
        print("All Class Data entered")
        print("Class Name: " + courseName)
        print("Class Link: " + courseLink)
        print("Meeting Link: " + meetingLink)
        Home.close()

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
mainwindow=Home()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(710)
widget.setFixedHeight(512)
widget.show()
app.exec_()