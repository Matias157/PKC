# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UIs/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.Scripts.sign_window import Ui_signinsignup_window


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 360, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(
            lambda: self.createSignWindow(main_window, "create")
        )
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 360, 150, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(
            lambda: self.createSignWindow(main_window, "verify")
        )
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 360, 150, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(
            lambda: self.createSignWindow(main_window, "vote")
        )
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 230, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.pushButton.setText(_translate("main_window", "Create Certificate"))
        self.label.setText(_translate("main_window", "Welcome to PKC!"))
        self.pushButton_2.setText(_translate("main_window", "Verify Certificate"))
        self.pushButton_3.setText(_translate("main_window", "Validate Certificate"))
        self.label_2.setText(_translate("main_window", "What do you want to do?"))

    def createSignWindow(self, main_window, type):
        main_window.hide()
        self.sign_window = QtWidgets.QWidget()
        self.ui = Ui_signinsignup_window()
        self.ui.setupUi(self.sign_window, main_window, type)
        self.sign_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
