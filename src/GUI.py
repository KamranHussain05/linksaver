# Author: Kamran Hussain
# Date: 4/18/21
# Dependencies

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

from OpenLink import LinkOpener
from Data import Data
from FileChanger import FileChanger
from Datajson import Datajson


class Home(QDialog):
    d = Data(8)
    print('marker 0, Home')
    def __init__(self):
        super(Home, self).__init__()
        self.setMinimumSize(1451, 891)
        loadUi("homeGui.ui", self)

        self.editCourse1.clicked.connect(self.editCourse_1)
        self.editCourse2.clicked.connect(self.editCourse_2)
        self.editCourse3.clicked.connect(self.editCourse_3)
        self.editCourse4.clicked.connect(self.editCourse_4)
        self.editCourse5.clicked.connect(self.editCourse_5)
        self.editCourse6.clicked.connect(self.editCourse_6)
        self.editCourse7.clicked.connect(self.editCourse_7)
        self.editCourse8.clicked.connect(self.editCourse_8)

        self.launchCourse1.clicked.connect(self.launchCourse_1)
        self.launchCourse2.clicked.connect(self.launchCourse_2)
        self.launchCourse3.clicked.connect(self.launchCourse_3)
        self.launchCourse4.clicked.connect(self.launchCourse_4)
        self.launchCourse5.clicked.connect(self.launchCourse_5)
        self.launchCourse6.clicked.connect(self.launchCourse_6)
        self.launchCourse7.clicked.connect(self.launchCourse_7)
        self.launchCourse8.clicked.connect(self.launchCourse_8)

        self.settings.clicked.connect(self.launchSettings)
        self.help.clicked.connect(self.launchHelp)

    def editCourse_1(self):
        print('marker 1a')
        print('Editing Course 1')
        s = "course1"
        print(s)
        edit_course = AddClass(self)
        edit_course.classDataInput(s)
        widget.addWidget(edit_course)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def editCourse_2(self):
        print('marker 1b')
        print('Editing Course 2')
        s='course2'
        print(s)
        edit_course = AddClass()
        edit_course.classDataInput(s)
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
        print('Launching Course 1')
        indexSource = "course1"
        d = Data(0)
        LinkOpener.openLink(d.getCourseLink(0))
        LinkOpener.openLink(d.getMeetingLink(0))

    def launchCourse_2(self):
        print('Launching Course 2')
        indexSource = "course2"
        d = Data(1)
        LinkOpener.openLink(d.getCourseLink(1))
        LinkOpener.openLink(d.getMeetingLink(1))

    def launchCourse_3(self):
        print('Launching Course 3')
        indexSource = "course3"
        d = Data(2)
        LinkOpener.openLink(d.getCourseLink(2))
        LinkOpener.openLink(d.getMeetingLink(2))

    def launchCourse_4(self):
        print('Launching Course 4')
        indexSource = "course4"
        d = Data(3)
        LinkOpener.openLink(d.getCourseLink(3))
        LinkOpener.openLink(d.getMeetingLink(3))

    def launchCourse_5(self):
        print('Launching Course 5')
        indexSource = "course5"
        d = Data(4)
        LinkOpener.openLink(d.getCourseLink(4))
        LinkOpener.openLink(d.getMeetingLink(4))

    def launchCourse_6(self):
        print('Launching Course 6')
        indexSource = "course6"
        d = Data(5)
        LinkOpener.openLink(d.getCourseLink(5))
        LinkOpener.openLink(d.getMeetingLink(5))

    def launchCourse_7(self):
        print('Launching Course 7')
        indexSource = "course7"
        d = Data(6)
        LinkOpener.openLink(d.getCourseLink(6))
        LinkOpener.openLink(d.getMeetingLink(6))

    def launchCourse_8(self):
        print('Launching Course 8')
        indexSource = "course8"
        d = Data(7)
        LinkOpener.openLink(d.getCourseLink(7))
        LinkOpener.openLink(d.getMeetingLink(7))

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
        d = Data(8)
        # reset = Ui_Dialog()
        # reset.launchCourse1.setText(QCoreApplication.translate("Dialog", u"test", None))
        print('Refreshed Home')


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

class AddClass(QDialog):
    def __init__(self, d=None, courseNum=None):
        super(AddClass, self).__init__()
        loadUi("addClassGUI.ui", self)
        self.classEntered.clicked.connect(self.classDataInput)
        print('marker 2, Home')
        print('In, innit method for AddClass, Marker')
        # if courseNum is not None:
        #     print('-------------------here')
        #     self.courseNumber = courseNum
        #     print(self.dataObject)
        #     print('---------------end init')

    # called when user presses save
    def classDataInput(self, source):
        print('marker 3, Home')
        courseName = self.className.text()
        courseLink = self.classLink.text()
        meetingLink = self.meetingLink.text()
        s = source

        print('Inputted Data')
        #print('Source: ' + s)
        print('Class name: ' + courseName)
        print('Class Link: ' + courseLink)
        print('Meeting Link: ' + meetingLink)

        print('before writing to JSON')
        d = Datajson()
        d.editIndexSource(s.__str__(), courseName, courseLink, meetingLink)
        print('marker 4, Home')
        print('after writing to JSON')

        back = Home()
        #back.refresh()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        print('marker 5, Home')

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


# ----------------------------------------------------------
# ----------------------------------------------------------

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
