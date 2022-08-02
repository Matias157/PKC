# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UIs/create_certificate_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from GUI.Scripts.dialog import Ui_dialog
from Scripts.create_certificate import CreateCertificate


class Ui_create_certificate_window(object):
    def setupUi(self, create_certificate_window, login_window):
        create_certificate_window.setObjectName("create_certificate_window")
        create_certificate_window.resize(623, 569)
        self.create_title = QtWidgets.QLabel(create_certificate_window)
        self.create_title.setGeometry(QtCore.QRect(120, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.create_title.setFont(font)
        self.create_title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.create_title.setObjectName("create_title")
        self.createcertif_button_2 = QtWidgets.QPushButton(create_certificate_window)
        self.createcertif_button_2.setGeometry(QtCore.QRect(420, 530, 100, 31))
        self.createcertif_button_2.setObjectName("createcertif_button_2")
        self.createcertif_label_1 = QtWidgets.QLabel(create_certificate_window)
        self.createcertif_label_1.setGeometry(QtCore.QRect(10, 80, 81, 19))
        self.createcertif_label_1.setObjectName("createcertif_label_1")
        self.createcertif_label_2 = QtWidgets.QLabel(create_certificate_window)
        self.createcertif_label_2.setGeometry(QtCore.QRect(10, 180, 81, 19))
        self.createcertif_label_2.setObjectName("createcertif_label_2")
        self.createcertif_line_1 = QtWidgets.QLineEdit(create_certificate_window)
        self.createcertif_line_1.setGeometry(QtCore.QRect(10, 110, 601, 31))
        self.createcertif_line_1.setObjectName("createcertif_line_1")
        self.createcertif_button_1 = QtWidgets.QPushButton(create_certificate_window)
        self.createcertif_button_1.setGeometry(QtCore.QRect(100, 530, 100, 31))
        self.createcertif_button_1.setObjectName("createcertif_button_1")
        self.createcertif_button_1.clicked.connect(
            lambda: self.createCertificate(login_window)
        )
        self.createcertif_textEdit_1 = QtWidgets.QTextEdit(create_certificate_window)
        self.createcertif_textEdit_1.setGeometry(QtCore.QRect(10, 210, 601, 181))
        self.createcertif_textEdit_1.setObjectName("createcertif_textEdit_1")
        self.createcertif_line_2 = QtWidgets.QLineEdit(create_certificate_window)
        self.createcertif_line_2.setGeometry(QtCore.QRect(10, 460, 601, 31))
        self.createcertif_line_2.setObjectName("createcertif_line_2")
        self.createcertif_label_3 = QtWidgets.QLabel(create_certificate_window)
        self.createcertif_label_3.setGeometry(QtCore.QRect(10, 430, 291, 19))
        self.createcertif_label_3.setObjectName("createcertif_label_3")
        self.worker = Worker()
        self.worker.finished.connect(lambda: self.showMsgBox(create_certificate_window))

        self.retranslateUi(create_certificate_window)
        QtCore.QMetaObject.connectSlotsByName(create_certificate_window)

    def retranslateUi(self, create_certificate_window):
        _translate = QtCore.QCoreApplication.translate
        create_certificate_window.setWindowTitle(
            _translate("create_certificate_window", "Create Certificate")
        )
        self.create_title.setText(
            _translate("create_certificate_window", "Create Certificate")
        )
        self.createcertif_button_2.setText(
            _translate("create_certificate_window", "Cancel")
        )
        self.createcertif_label_1.setText(
            _translate("create_certificate_window", "URL")
        )
        self.createcertif_label_2.setText(
            _translate("create_certificate_window", "Public Key")
        )
        self.createcertif_button_1.setText(
            _translate("create_certificate_window", "Create")
        )
        self.createcertif_label_3.setText(
            _translate(
                "create_certificate_window", "Wallet Private Key (WILL NOT BE STORED)"
            )
        )

    def createCertificate(self, login_window):
        self.worker.args(
            login_window,
            self.createcertif_line_2.text(),
            self.createcertif_line_1.text(),
            self.createcertif_textEdit_1.toPlainText(),
        )
        self.showPopUp()
        self.worker.start()

    def showPopUp(self):
        self.pop_up = QtWidgets.QDialog()
        ui = Ui_dialog()
        ui.setupUi(
            self.pop_up, "Creating Certificate", "Cretificate is being created..."
        )
        self.pop_up.show()

    def showMsgBox(self, create_certificate_window):
        self.pop_up.close()
        msg = QMessageBox()
        msg.setWindowTitle("Completion")
        msg.setText("Execution Completed!")
        msg.setInformativeText("No Execution Details")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(lambda: self.msgBoxButton(create_certificate_window))
        x = msg.exec_()

    def msgBoxButton(self, create_certificate_window):
        create_certificate_window.close()

    def cancel(self, create_certificate_window, login_window):
        login_window.show()
        create_certificate_window.close()


class Worker(QThread):
    def run(self):
        # time.sleep(5)
        self.cert.create_certificate(self.pub_key, self.url)

    def args(self, login_window, priv_key, url, pub_key):
        self.cert = CreateCertificate(
            login_window.session.address,
            login_window.session.endpoint,
            priv_key,
        )
        self.url = url
        self.pub_key = pub_key


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    create_certificate_window = QtWidgets.QWidget()
    ui = Ui_create_certificate_window()
    ui.setupUi(create_certificate_window)
    create_certificate_window.show()
    sys.exit(app.exec_())
