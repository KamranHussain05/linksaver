import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class AddClass(QDialog):
    def __init__(self):
        super(AddClass,self).__init__()
        loadUi("addClassGUI.ui",self)
        self.classEntered.clicked.connect(self.loginfunction)

    def loginfunction(self):
        courseName=self.className.text()
        courseLink=self.classLink.text()
        meetingLink=self.meetingLink.text()
        print("All Class Data entered")
        print("Class Name: " + courseName)
        print("Class Link: " + courseLink)
        print("Meeting Link: " + meetingLink)

app=QApplication(sys.argv)
mainwindow=AddClass()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(710)
widget.setFixedHeight(512)
widget.show()
app.exec_()