# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UIs/login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Scripts.login import Login
from GUI.Scripts.verify_window import Ui_verify_window
from GUI.Scripts.create_certificate_window import Ui_create_certificate_window


class Ui_login_window(object):
    def setupUi(self, login_window, signinsignup_window, type):
        login_window.setObjectName("login_window")
        login_window.resize(527, 264)
        self.login_line_2 = QtWidgets.QLineEdit(login_window)
        self.login_line_2.setGeometry(QtCore.QRect(20, 150, 481, 31))
        self.login_line_2.setObjectName("login_line_2")
        self.login_line_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_label_2 = QtWidgets.QLabel(login_window)
        self.login_label_2.setGeometry(QtCore.QRect(20, 120, 81, 19))
        self.login_label_2.setObjectName("login_label_2")
        self.login_line_1 = QtWidgets.QLineEdit(login_window)
        self.login_line_1.setGeometry(QtCore.QRect(20, 50, 481, 31))
        self.login_line_1.setObjectName("login_line_1")
        self.login_label_1 = QtWidgets.QLabel(login_window)
        self.login_label_1.setGeometry(QtCore.QRect(20, 20, 81, 19))
        self.login_label_1.setObjectName("login_label_1")
        self.login_button_1 = QtWidgets.QPushButton(login_window)
        self.login_button_1.setGeometry(QtCore.QRect(110, 220, 100, 31))
        self.login_button_1.setObjectName("login_button_1")
        self.login_button_1.clicked.connect(lambda: self.login(login_window, type))
        self.login_button_2 = QtWidgets.QPushButton(login_window)
        self.login_button_2.setGeometry(QtCore.QRect(310, 220, 100, 31))
        self.login_button_2.setObjectName("login_button_2")
        self.login_button_2.clicked.connect(
            lambda: self.cancel(login_window, signinsignup_window)
        )

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Login"))
        self.login_label_2.setText(_translate("login_window", "Password"))
        self.login_label_1.setText(_translate("login_window", "Username"))
        self.login_button_1.setText(_translate("login_window", "Login"))
        self.login_button_2.setText(_translate("login_window", "Cancel"))

    def login(self, login_window, type):
        self.session = Login(self.login_line_1.text(), self.login_line_2.text())
        if self.session.login():
            login_window.hide()
            if type == "create":
                self.create_certificate_window = QtWidgets.QWidget()
                self.ui = Ui_create_certificate_window()
                self.ui.setupUi(self.create_certificate_window, self)
                self.create_certificate_window.show()
            elif type == "verify":
                self.verify_window = QtWidgets.QWidget()
                self.ui = Ui_verify_window()
                self.ui.setupUi(self.verify_window, self)
                self.verify_window.show()
            else:
                pass
        else:
            print("Login Failed!")

    def cancel(self, login_window, signinsignup_window):
        signinsignup_window.show()
        login_window.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QWidget()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())