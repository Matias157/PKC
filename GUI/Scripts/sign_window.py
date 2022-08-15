# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UIs/sign_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.Scripts.login_window import Ui_login_window
from GUI.Scripts.create_window import Ui_create_window


class Ui_signinsignup_window(object):
    def setupUi(self, signinsignup_window):
        signinsignup_window.setObjectName("signinsignup_window")
        signinsignup_window.resize(524, 264)
        self.sign_button_1 = QtWidgets.QPushButton(signinsignup_window)
        self.sign_button_1.setGeometry(QtCore.QRect(50, 140, 131, 31))
        self.sign_button_1.setObjectName("sign_button_1")
        self.sign_button_1.clicked.connect(
            lambda: self.createLoginWindow(signinsignup_window)
        )
        self.sign_title = QtWidgets.QLabel(signinsignup_window)
        self.sign_title.setGeometry(QtCore.QRect(80, 10, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.sign_title.setFont(font)
        self.sign_title.setObjectName("sign_title")
        self.sign_button_2 = QtWidgets.QPushButton(signinsignup_window)
        self.sign_button_2.setGeometry(QtCore.QRect(340, 140, 131, 31))
        self.sign_button_2.setObjectName("sign_button_2")
        self.sign_button_2.clicked.connect(
            lambda: self.createCreateWindow(signinsignup_window)
        )
        self.sign_button_3 = QtWidgets.QPushButton(signinsignup_window)
        self.sign_button_3.setGeometry(QtCore.QRect(200, 220, 121, 31))
        self.sign_button_3.setObjectName("sign_button_3")
        self.sign_button_3.clicked.connect(lambda: self.cancel(signinsignup_window))

        self.retranslateUi(signinsignup_window)
        QtCore.QMetaObject.connectSlotsByName(signinsignup_window)

    def retranslateUi(self, signinsignup_window):
        _translate = QtCore.QCoreApplication.translate
        signinsignup_window.setWindowTitle(
            _translate("signinsignup_window", "Sign In Sign Up")
        )
        self.sign_button_1.setText(_translate("signinsignup_window", "Login"))
        self.sign_title.setText(_translate("signinsignup_window", "Welcome to PKC!"))
        self.sign_button_2.setText(_translate("signinsignup_window", "Create account"))
        self.sign_button_3.setText(_translate("signinsignup_window", "Quit"))

    def createLoginWindow(self, signinsignup_window):
        signinsignup_window.hide()
        self.login_window = QtWidgets.QWidget()
        self.ui = Ui_login_window()
        self.ui.setupUi(self.login_window, signinsignup_window)
        self.login_window.show()

    def createCreateWindow(self, signinsignup_window):
        signinsignup_window.hide()
        self.create_window = QtWidgets.QWidget()
        self.ui = Ui_create_window()
        self.ui.setupUi(self.create_window, signinsignup_window)
        self.create_window.show()

    def cancel(self, signinsignup_window):
        signinsignup_window.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    signinsignup_window = QtWidgets.QWidget()
    ui = Ui_signinsignup_window()
    ui.setupUi(signinsignup_window)
    signinsignup_window.show()
    sys.exit(app.exec_())
