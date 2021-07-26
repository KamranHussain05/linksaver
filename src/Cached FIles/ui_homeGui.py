# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeGuilKnbpV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1451, 891)
        Dialog.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1451, 134))
        self.label.setStyleSheet(u"color: rgb(253, 253, 255);\n"
"font-size:28pt;\n"
"text-align: center;")
        self.label.setAlignment(Qt.AlignCenter)
        self.help = QPushButton(Dialog)
        self.help.setObjectName(u"help")
        self.help.setGeometry(QRect(0, 800, 1451, 91))
        self.help.setStyleSheet(u"color: rgb(253, 255, 255);\n"
"background-color: rgb(162, 162, 121);\n"
"font-size:18pt;\n"
"text-align: center;")
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 130, 1451, 671))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 15)
        self.frame_9 = QFrame(self.gridLayoutWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.launchCourse2 = QPushButton(self.frame_9)
        self.launchCourse2.setObjectName(u"launchCourse2")
        self.launchCourse2.setGeometry(QRect(0, 110, 361, 221))
        self.launchCourse2.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 361, 121))
        self.label_3.setPixmap(QPixmap(u"../../../../Downloads/economy-2.jpg"))
        self.label_3.setScaledContents(True)
        self.editCourse2 = QToolButton(self.frame_9)
        self.editCourse2.setObjectName(u"editCourse2")
        self.editCourse2.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse2.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_9, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.gridLayoutWidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.launchCourse6 = QPushButton(self.frame_7)
        self.launchCourse6.setObjectName(u"launchCourse6")
        self.launchCourse6.setGeometry(QRect(0, 90, 361, 241))
        self.launchCourse6.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 361, 111))
        self.label_7.setPixmap(QPixmap(u"../../../../Downloads/photo-1515325595179-59cd5262ca53.jpg"))
        self.label_7.setScaledContents(True)
        self.editCourse6 = QToolButton(self.frame_7)
        self.editCourse6.setObjectName(u"editCourse6")
        self.editCourse6.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse6.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_7, 1, 1, 1, 1)

        self.frame_5 = QFrame(self.gridLayoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.launchCourse1 = QPushButton(self.frame_5)
        self.launchCourse1.setObjectName(u"launchCourse1")
        self.launchCourse1.setGeometry(QRect(0, 110, 361, 221))
        self.launchCourse1.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 361, 121))
        self.label_2.setPixmap(QPixmap(u"../../../../Downloads/download.jpg"))
        self.label_2.setScaledContents(True)
        self.editCourse1 = QToolButton(self.frame_5)
        self.editCourse1.setObjectName(u"editCourse1")
        self.editCourse1.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse1.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.gridLayoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.launchCourse7 = QPushButton(self.frame_8)
        self.launchCourse7.setObjectName(u"launchCourse7")
        self.launchCourse7.setGeometry(QRect(0, 90, 361, 241))
        self.launchCourse7.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 361, 111))
        self.label_8.setPixmap(QPixmap(u"../../../../Downloads/download.png"))
        self.label_8.setScaledContents(True)
        self.editCourse7 = QToolButton(self.frame_8)
        self.editCourse7.setObjectName(u"editCourse7")
        self.editCourse7.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse7.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_8, 1, 2, 1, 1)

        self.frame_10 = QFrame(self.gridLayoutWidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.launchCourse3 = QPushButton(self.frame_10)
        self.launchCourse3.setObjectName(u"launchCourse3")
        self.launchCourse3.setGeometry(QRect(0, 90, 361, 241))
        self.launchCourse3.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 361, 121))
        self.label_4.setPixmap(QPixmap(u"../../../../Downloads/images.jpg"))
        self.label_4.setScaledContents(True)
        self.editCourse3 = QToolButton(self.frame_10)
        self.editCourse3.setObjectName(u"editCourse3")
        self.editCourse3.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse3.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_10, 0, 2, 1, 1)

        self.frame_6 = QFrame(self.gridLayoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.launchCourse5 = QPushButton(self.frame_6)
        self.launchCourse5.setObjectName(u"launchCourse5")
        self.launchCourse5.setGeometry(QRect(0, 90, 361, 241))
        self.launchCourse5.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 361, 111))
        self.label_6.setPixmap(QPixmap(u"../../../../Downloads/sports-balls.png"))
        self.label_6.setScaledContents(True)
        self.editCourse5 = QToolButton(self.frame_6)
        self.editCourse5.setObjectName(u"editCourse5")
        self.editCourse5.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse5.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.gridLayoutWidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.launchCourse4 = QPushButton(self.frame_11)
        self.launchCourse4.setObjectName(u"launchCourse4")
        self.launchCourse4.setGeometry(QRect(0, 90, 361, 241))
        self.launchCourse4.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 361, 121))
        self.label_5.setPixmap(QPixmap(u"../../../../Downloads/Screenshot 2021-06-19 170259.png"))
        self.label_5.setScaledContents(True)
        self.editCourse4 = QToolButton(self.frame_11)
        self.editCourse4.setObjectName(u"editCourse4")
        self.editCourse4.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse4.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_11, 0, 3, 1, 1)

        self.frame_12 = QFrame(self.gridLayoutWidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.launchCourse8 = QPushButton(self.frame_12)
        self.launchCourse8.setObjectName(u"launchCourse8")
        self.launchCourse8.setGeometry(QRect(0, 90, 361, 241))
        self.launchCourse8.setStyleSheet(u"background-color: rgb(206, 197, 146);\n"
"font-size:15pt\n"
"")
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 361, 111))
        self.label_9.setPixmap(QPixmap(u"../../../../Downloads/Homeroom.jpg"))
        self.label_9.setScaledContents(True)
        self.editCourse8 = QToolButton(self.frame_12)
        self.editCourse8.setObjectName(u"editCourse8")
        self.editCourse8.setGeometry(QRect(320, 10, 25, 19))
        self.editCourse8.setStyleSheet(u"background-color: yellow;")

        self.gridLayout.addWidget(self.frame_12, 1, 3, 1, 1)

        self.settings = QPushButton(Dialog)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(1340, 30, 75, 41))
        self.settings.setStyleSheet(u"color: white;\n"
"background-color: gray;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Link-Saver", None))
        self.help.setText(QCoreApplication.translate("Dialog", u"Help", None))
        self.launchCourse2.setText(QCoreApplication.translate("Dialog", u"Math", None))
        self.label_3.setText("")
        self.editCourse2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.launchCourse6.setText(QCoreApplication.translate("Dialog", u"History", None))
        self.label_7.setText("")
        self.editCourse6.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.launchCourse1.setText(QCoreApplication.translate("Dialog", u"English", None))
        self.label_2.setText("")
        self.editCourse1.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.launchCourse7.setText(QCoreApplication.translate("Dialog", u"World Language", None))
        self.label_8.setText("")
        self.editCourse7.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.launchCourse3.setText(QCoreApplication.translate("Dialog", u"Science", None))
        self.label_4.setText("")
        self.editCourse3.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.launchCourse5.setText(QCoreApplication.translate("Dialog", u"PE", None))
        self.label_6.setText("")
        self.editCourse5.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.launchCourse4.setText(QCoreApplication.translate("Dialog", u"Computer Science", None))
        self.label_5.setText("")
        self.editCourse4.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.launchCourse8.setText(QCoreApplication.translate("Dialog", u"Homeroom", None))
        self.label_9.setText("")
        self.editCourse8.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.settings.setText(QCoreApplication.translate("Dialog", u"Settings", None))
    # retranslateUi

