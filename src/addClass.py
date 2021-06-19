# Author: Kamran Hussain
# Date: 6/18/21
# Dependencies: PyQt5, home.ui, homegui.py, qt -> addClassGui.py
from FileChanger import FileChanger
import HomeGui
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


# adds class
class AddClass(QDialog):
    def __init__(self):
        super(AddClass, self).__init__()
        loadUi("addClassGUI.ui", self)
        self.classEntered.clicked.connect(self.classDataInput)

    # called when user presses save
    def classDataInput(self):
        AddClass.writeToList()
        AddClass.close()

    # Write to list
    # pass in Data object d and course number
    def writeToList(self, d, num):
        courseName = self.className.text()
        courseLink = self.classLink.text()
        meetingLink = self.meetingLink.text()

        # future => check if url is valid
        s = courseName + ';' + courseLink + ';' + meetingLink
        d.replaceStrings(num, s)
        try:
            FileChanger.write_file(d.returnStrings())
        except Exception as e:
            print("Error WriteToList: ", e)

        HomeGui.refresh();


app = QApplication(sys.argv)
mainwindow = AddClass()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(710)
widget.setFixedHeight(512)
widget.show()
app.exec_()
