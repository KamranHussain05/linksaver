# Author: Kamran Hussain
# Date: 4/18/21
# Dependencies

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from ui_homeGui import Ui_Dialog, QCoreApplication

from OpenLink import LinkOpener
from Data import Data
from FileChanger import FileChanger

class Home(QDialog):
    d = Data(8)
    def __init__(self):
        super(Home, self).__init__()
        self.setMinimumSize(1451, 891)
        loadUi("homeGui.ui", self)

        self.editCourse1.clicked.connect(self.editCourse_1)
        self.editCourse2.clicked.connect(self.editCourse_2)
        self.editCourse3.clicked.connect(lambda: self.editCourse_3())
        self.editCourse4.clicked.connect(lambda: self.editCourse_4())
        self.editCourse5.clicked.connect(lambda: self.editCourse_5())
        self.editCourse6.clicked.connect(lambda: self.editCourse_6())
        self.editCourse7.clicked.connect(lambda: self.editCourse_7())
        self.editCourse8.clicked.connect(lambda: self.editCourse_8())

        self.launchCourse1.clicked.connect(self.launchCourse_1)
        self.launchCourse2.clicked.connect(lambda: self.launchCourse_2())
        self.launchCourse3.clicked.connect(lambda: self.launchCourse_3())
        self.launchCourse4.clicked.connect(lambda: self.launchCourse_4())
        self.launchCourse5.clicked.connect(lambda: self.launchCourse_5())
        self.launchCourse6.clicked.connect(lambda: self.launchCourse_6())
        self.launchCourse7.clicked.connect(lambda: self.launchCourse_7())
        self.launchCourse8.clicked.connect(lambda: self.launchCourse_8())

        self.settings.clicked.connect(lambda: self.launchSettings())
        self.help.clicked.connect(lambda: self.launchHelp())

    def editCourse_1(self):
        print('Editing Course 1')
        #AddClass().className.setText(Data.getCourseName)
        #AddClass()

        edit_course = AddClass(self.d, 0)
        # edit_course.d = self.d
        # edit_course.courseNum = 0
        # edit_course.writeToList(self.d, 0)
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_2(self):
        print('Editing Course 2')
        edit_course = AddClass()
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_3(self):
        print('Editing Course 3')
        edit_course = AddClass()
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_4(self):
        print('Editing Course 4')
        edit_course = AddClass()
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_5(self):
        print('Editing Course 5')
        edit_course = AddClass()
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_6(self):
        print('Editing Course 6')
        edit_course = AddClass()
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_7(self):
        print('Editing Course 7')
        edit_course = AddClass()
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_8(self):
        print('Editing Course 8')
        edit_course = AddClass()
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # ______________________________________

    def launchCourse_1(self):
        LinkOpener.openLink("https://example.com")
        LinkOpener.openLink("https://starwars.com")

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
        goToSettings = Settings()
        widget.addWidget(goToSettings)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def launchHelp(self):
        print('Help Website Launched')
        LinkOpener.openLink("https://github.com/KamranHussain05/linksaver")

    def refresh(self):
        print('Refreshing Home')
        d=Data(8)
        #reset = Ui_Dialog()
        #reset.launchCourse1.setText(QCoreApplication.translate("Dialog", u"test", None))
        print('Refreshed Home')

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

class AddClass(QDialog):
    def __init__(self, d=None, courseNum=None):
        super(AddClass, self).__init__()
        loadUi("addClassGUI.ui", self)
        self.classEntered.setObjectName("TEST")
        self.classEntered.clicked.connect(self.classDataInput)

        if d is not None and courseNum is not None:
            print('-------------------here')
            self.dataObject = d
            self.courseNumber = courseNum
            print(self.dataObject)

            print('---------------end init')

    # called when user presses save
    def classDataInput(self):
        courseName = self.className.text()
        courseLink = self.classLink.text()
        meetingLink = self.meetingLink.text()

        print('Inputted Data')
        print('Class name: ' + courseName)
        print('Class Link: ' + courseLink)
        print('Meeting Link: ' + meetingLink)

        print('before writing to list')
        #print(self.dataObject, self.courseNumber)
        #AddClass.writeToList(self.d, self.courseNumber)
        print('after writing to list')

        back = Home()
        back.refresh()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    # Write to list
    # pass in Data object d and course number
    def writeToList(self, d, num):
        print('inside writeToList')
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
#----------------------------------------------------------
#----------------------------------------------------------
class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        self.setMinimumSize(1451, 891)
        loadUi("settings.ui", self)
        self.applied.clicked.connect(self.execute)

    def execute(self):
        print('settings applied')
        back = Home()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() - 2)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
home_window = Home()
widget.addWidget(home_window)
widget.show()

add_class = AddClass()
widget.addWidget(add_class)
widget.show()

window = Settings()
widget.addWidget(window)
widget.show()
app.exec_()
