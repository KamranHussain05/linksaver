import sys
import json
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


# opens the settings tab
class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        loadUi("Settings.ui", self)
        self.button1.clicked.connect(lambda: self.changeColor())
        self.button2.clicked.connect(lambda: self.button_2())
        self.button3.clicked.connect(lambda: self.button_3())
        self.button4.clicked.connect(lambda: self.button_4())
        self.closeButton.clicked.connect(lambda: self.closeTab(self))

    def changeColor(self):
        self.checkColorScheme()

    def button_2(self):
        print("Font changed to <font>")

    def button_3(self):
        print("button 3")

    def button_4(self):
        print("button 4")

    def closeTab(self):
        Settings.close()

    def checkColorScheme(self):
        with open("GUIproperties.json", "r") as jsProperties:
            properties = json.load(jsProperties)
        print(properties)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = Settings()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
