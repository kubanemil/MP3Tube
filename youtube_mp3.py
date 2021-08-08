# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube_mp3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from __future__ import unicode_literals
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

print('Please,wait while program is opening...')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 590)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line.setGeometry(QtCore.QRect(170, 140, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.input_line.setFont(font)
        self.input_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_line.setObjectName("input_line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 440, 441, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);\n"
"color: rgb(211, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 611, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(150, 530, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 200, 34);")
        self.btn_1.setObjectName("btn_1")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 500, 621, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(15, 5, 211, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 591, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 290, 591, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 601, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 320, 591, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 350, 591, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 380, 591, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 410, 591, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 560, 101, 21))
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 470, 591, 30))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 0, 127);\n"
"color: rgb(0, 85, 0);")
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushbutton()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Youtube Link:"))
        self.label_2.setText(_translate("MainWindow", "Youtube Video to MP3 File"))
        self.label_4.setText(_translate("MainWindow", "Please, wait until all MP3 files will download!"))
        self.btn_1.setText(_translate("MainWindow", "Download"))
        self.label_6.setText(_translate("MainWindow", "MP3Tube"))
        self.label_7.setText(_translate("MainWindow", "   MP3Tube has simple design and high-speed functionality, which"))
        self.label_8.setText(_translate("MainWindow", "To download more than one audio, create open youtube playlist"))
        self.label_9.setText(_translate("MainWindow", "can download youtube video\'s audio fast and with exellent quality."))
        self.label_10.setText(_translate("MainWindow", "with video you want to download and input only one link from"))
        self.label_11.setText(_translate("MainWindow", "playlist. MP3Tube will download all music in that playlist. "))
        self.label_12.setText(_translate("MainWindow", "Limitation on a playlist size is 25 videos. If  playlist contains "))
        self.label_13.setText(_translate("MainWindow", "more than 25 videos, MP3Tube will download only first 25 videos."))
        self.label_3.setText(_translate("MainWindow", "Instruction:"))
        self.label_5.setText(_translate("MainWindow", "Made by Emil Kuban."))
        self.label_14.setText(_translate("MainWindow", "MP3 files will downloaded to same folder where MP3Tube is located."))

    def pushbutton(self):
        self.btn_1.clicked.connect(self.download)


    def download(self):
        error = QMessageBox()
        error.setWindowTitle('Downloading...')
        error.setText("Wait while your music downloading...")
        error.setIcon(QMessageBox.Information)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()
        self.btn_1.setText('Downloading...')
        youtube_link = self.input_line.text()
        print('Wait a while...')
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_link])

        print("Your files have downloaded successfully!")
        print("Files' location: D:\\MP3_Youtube")

        error = QMessageBox()
        error.setWindowTitle('Success!')
        error.setText("Your youtube MP3 was downloaded successfully!")
        error.setIcon(QMessageBox.Information)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

        self.btn_1.setText('Download')
        self.input_line.setText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())