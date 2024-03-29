# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UIs/verify_window.ui'
#
# verifyd by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from GUI.Scripts.verify_results_window import Ui_verify_results_window
from GUI.Scripts.dialog import Ui_dialog
from Scripts.verify import Verify
from Scripts.voted_list import VotedList


class Ui_verify_window(object):
    def setupUi(self, verify_window, main_window, login_data):
        verify_window.setObjectName("verify_window")
        verify_window.resize(520, 300)
        verify_window.setFixedSize(520, 250)
        self.verify_title = QtWidgets.QLabel(verify_window)
        self.verify_title.setGeometry(QtCore.QRect(60, 10, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.verify_title.setFont(font)
        self.verify_title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verify_title.setObjectName("verify_title")
        self.verify_label_1 = QtWidgets.QLabel(verify_window)
        self.verify_label_1.setGeometry(QtCore.QRect(10, 90, 81, 19))
        self.verify_label_1.setObjectName("verify_label_1")
        self.verify_line_1 = QtWidgets.QLineEdit(verify_window)
        self.verify_line_1.setGeometry(QtCore.QRect(10, 120, 501, 31))
        self.verify_line_1.setObjectName("verify_line_1")
        self.verify_button_1 = QtWidgets.QPushButton(verify_window)
        self.verify_button_1.setGeometry(QtCore.QRect(90, 170, 100, 31))
        self.verify_button_1.setObjectName("verify_button_1")
        self.verify_button_1.clicked.connect(lambda: self.verify(login_data))
        self.verify_button_2 = QtWidgets.QPushButton(verify_window)
        self.verify_button_2.setGeometry(QtCore.QRect(200, 210, 100, 31))
        self.verify_button_2.setObjectName("verify_button_2")
        self.verify_button_2.clicked.connect(
            lambda: self.cancel(verify_window, main_window)
        )
        self.verify_button_3 = QtWidgets.QPushButton(verify_window)
        self.verify_button_3.setGeometry(QtCore.QRect(310, 170, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.verify_button_3.setFont(font)
        self.verify_button_3.setObjectName("verify_button_3")
        self.verify_button_3.clicked.connect(lambda: self.imFeelingLucky(login_data))
        self.worker = Worker()
        self.worker.finished.connect(lambda: self.pop_up.close())
        self.worker.worker_complete.connect(
            lambda x: self.verifyValidation(x, verify_window, login_data)
        )
        self.luckyOutput = []

        self.retranslateUi(verify_window)
        QtCore.QMetaObject.connectSlotsByName(verify_window)

    def retranslateUi(self, verify_window):
        _translate = QtCore.QCoreApplication.translate
        verify_window.setWindowTitle(_translate("verify_window", "Browse"))
        self.verify_title.setText(_translate("verify_window", "Browse Certificate"))
        self.verify_label_1.setText(_translate("verify_window", "URL"))
        self.verify_button_1.setText(_translate("verify_window", "Search"))
        self.verify_button_2.setText(_translate("verify_window", "Cancel"))
        self.verify_button_3.setText(_translate("verify_window", "I'm Feeling Lucky"))

    def verify(self, login_data):
        self.worker.args("search", login_data, url=self.verify_line_1.text())
        self.showPopUp("Searching Certificate", "Searching...")
        self.worker.start()

    def imFeelingLucky(self, login_data):
        self.worker.args("lucky", login_data, url=self.verify_line_1.text())
        self.showPopUp("Searching Certificate", "Searching...")
        self.worker.start()

    def showPopUp(self, title, text):
        self.pop_up = QtWidgets.QDialog()
        ui = Ui_dialog()
        ui.setupUi(self.pop_up, title, text)
        self.pop_up.show()

    def verifyValidation(self, out, verify_window, login_data):
        if out[1] == "search":
            self.createResultsWindow("search", out[0], verify_window, login_data)
        elif out[1] == "lucky":
            self.createResultsWindow("lucky", out[0], verify_window, login_data)
        else:
            for trusted, output in zip(out[0][0], out[2]):
                if trusted == output[0]:
                    self.luckyOutput.append(output)
            if out[3]:
                self.createResultsWindow(
                    "search", self.luckyOutput, verify_window, login_data
                )

    def createResultsWindow(self, type, out, verify_window, login_data):
        if out[0] != False:
            if type == "search":
                verify_window.hide()
                self.verify_line_1.setText("")
                verify_results_window = QtWidgets.QWidget()
                ui = Ui_verify_results_window()
                ui.setupUi(verify_results_window, verify_window, login_data, out)
                verify_results_window.show()
                self.luckyOutput = []
            else:
                self.getList(out, login_data)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Execution Reverted!")
            msg.setInformativeText(str(out[1]))
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            self.luckyOutput = []

    def getList(self, out, login_data):
        col_list = ["address"]
        df = pd.read_csv(
            "Data/UserData/" + login_data.session.address + "/TrustedList.csv",
            usecols=col_list,
        )
        if not df["address"].empty:
            for row in df["address"]:
                try:
                    if row == df["address"].iloc[-1]:
                        self.worker.args(
                            "list", login_data, addr=row, out=out, last=True
                        )
                    else:
                        self.worker.args("list", login_data, addr=row, out=out)
                    self.showPopUp("Getting Voted List", "Getting...")
                    self.worker.start()
                except Exception as e:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("An error has occurred!")
                    msg.setInformativeText(str(e))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setStandardButtons(QMessageBox.Ok)
                    x = msg.exec_()
        else:
            self.luckyOutput = []
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error has occurred!")
            msg.setInformativeText("Certificate could not be found!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def cancel(self, verify_window, main_window):
        main_window.show()
        verify_window.close()


class Worker(QThread):
    worker_complete = pyqtSignal(list)

    def run(self):
        if self.type == "search":
            out = self.verify.verify(self.url)
            out = [out]
            out.append("search")
        elif self.type == "lucky":
            out = self.verify.verify(self.url)
            out = [out]
            out.append("lucky")
        else:
            out = self.list.voted_list(self.address)
            out = [out]
            out.append("list")
            out.append(self.searchOut)
            out.append(self.last)
        self.worker_complete.emit(out)

    def args(self, type, login_data, url="", addr="", out=[], last=False):
        self.type = type
        if type == "search" or type == "lucky":
            self.verify = Verify(login_data.session.endpoint)
            self.url = url
        else:
            self.list = VotedList(login_data.session.endpoint)
            self.searchOut = out
            self.last = last
            self.address = addr


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    verify_window = QtWidgets.QWidget()
    ui = Ui_verify_window()
    ui.setupUi(verify_window)
    verify_window.show()
    sys.exit(app.exec_())
