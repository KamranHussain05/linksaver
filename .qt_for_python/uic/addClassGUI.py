# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kamran\Documents\GitHub\linksaver\src\addClassGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(710, 512)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 14pt;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 40, 201, 61))
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("color: rgb(253, 253, 255);\n"
"font-size:28pt;\n"
"text-align: center;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 121, 41))
        self.label_2.setStyleSheet("color: rgb(255, 232, 162);\n"
"font-size: 16pt;")
        self.label_2.setObjectName("label_2")
        self.className = QtWidgets.QLineEdit(Dialog)
        self.className.setGeometry(QtCore.QRect(170, 150, 531, 61))
        self.className.setStyleSheet("color: rgb(0, 0, 0)")
        self.className.setObjectName("className")
        self.classEntered = QtWidgets.QPushButton(Dialog)
        self.classEntered.setGeometry(QtCore.QRect(0, 460, 711, 61))
        self.classEntered.setStyleSheet("background-color: rgb(206, 197, 146)")
        self.classEntered.setObjectName("classEntered")
        self.classLink = QtWidgets.QLineEdit(Dialog)
        self.classLink.setGeometry(QtCore.QRect(170, 240, 531, 61))
        self.classLink.setStyleSheet("color: rgb(255, 255, 255)")
        self.classLink.setObjectName("classLink")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 111, 41))
        self.label_3.setStyleSheet("color: rgb(255, 232, 162);\n"
"font-size: 16pt;")
        self.label_3.setObjectName("label_3")
        self.meetingLink = QtWidgets.QLineEdit(Dialog)
        self.meetingLink.setGeometry(QtCore.QRect(170, 330, 531, 61))
        self.meetingLink.setStyleSheet("color: rgb(255, 255, 255)")
        self.meetingLink.setObjectName("meetingLink")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 121, 41))
        self.label_4.setStyleSheet("color: rgb(255, 232, 162);\n"
"font-size: 16pt;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Link-Saver"))
        self.label.setText(_translate("Dialog", "Add a Class"))
        self.label_2.setText(_translate("Dialog", "Class Name"))
        self.classEntered.setText(_translate("Dialog", "Enter"))
        self.label_3.setText(_translate("Dialog", "CourseLink"))
        self.label_4.setText(_translate("Dialog", "Meeting Link"))
