# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UIs/test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signinsignup_window(object):
    def setupUi(self, signinsignup_window):
        signinsignup_window.setObjectName("signinsignup_window")
        signinsignup_window.resize(524, 264)
        signinsignup_window.setStyleSheet("QWidget#signinsignup_window{\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0.239, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.sign_button_1 = QtWidgets.QPushButton(signinsignup_window)
        self.sign_button_1.setGeometry(QtCore.QRect(50, 140, 41, 41))
        self.sign_button_1.setStyleSheet("font: 11pt \"Serif\";\n"
"border-radius:20px;\n"
"background-color:rgb(0,0,0);\n"
"color: rgb(255, 255, 255);")
        self.sign_button_1.setObjectName("sign_button_1")
        self.sign_title = QtWidgets.QLabel(signinsignup_window)
        self.sign_title.setGeometry(QtCore.QRect(160, 10, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sign_title.setFont(font)
        self.sign_title.setStyleSheet("font: 36pt \"Serif\";\n"
"color: rgb(255, 255, 255);")
        self.sign_title.setObjectName("sign_title")
        self.sign_button_2 = QtWidgets.QPushButton(signinsignup_window)
        self.sign_button_2.setGeometry(QtCore.QRect(340, 140, 131, 31))
        self.sign_button_2.setStyleSheet("font: 11pt \"Serif\";\n"
"color: rgb(255, 255, 255);")
        self.sign_button_2.setObjectName("sign_button_2")
        self.sign_button_3 = QtWidgets.QPushButton(signinsignup_window)
        self.sign_button_3.setGeometry(QtCore.QRect(200, 220, 121, 31))
        self.sign_button_3.setStyleSheet("font: 11pt \"Serif\";\n"
"color: rgb(255, 255, 255);")
        self.sign_button_3.setObjectName("sign_button_3")
        self.sign_title_2 = QtWidgets.QLabel(signinsignup_window)
        self.sign_title_2.setGeometry(QtCore.QRect(150, 70, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sign_title_2.setFont(font)
        self.sign_title_2.setStyleSheet("font: 11pt \"Serif\";\n"
"color: rgb(255, 255, 255);")
        self.sign_title_2.setObjectName("sign_title_2")

        self.retranslateUi(signinsignup_window)
        QtCore.QMetaObject.connectSlotsByName(signinsignup_window)

    def retranslateUi(self, signinsignup_window):
        _translate = QtCore.QCoreApplication.translate
        signinsignup_window.setWindowTitle(_translate("signinsignup_window", "Sign In Sign Up"))
        self.sign_button_1.setText(_translate("signinsignup_window", "Login"))
        self.sign_title.setText(_translate("signinsignup_window", "Welcome"))
        self.sign_button_2.setText(_translate("signinsignup_window", "Create account"))
        self.sign_button_3.setText(_translate("signinsignup_window", "Quit"))
        self.sign_title_2.setText(_translate("signinsignup_window", "Sign in or create a new account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signinsignup_window = QtWidgets.QWidget()
    ui = Ui_signinsignup_window()
    ui.setupUi(signinsignup_window)
    signinsignup_window.show()
    sys.exit(app.exec_())
