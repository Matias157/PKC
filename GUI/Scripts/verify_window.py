# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UIs/verify_window.ui'
#
# verifyd by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from GUI.Scripts.verify_results_window import Ui_verify_results_window
from GUI.Scripts.dialog import Ui_dialog
from Scripts.verify import Verify


class Ui_verify_window(object):
    def setupUi(self, verify_window, main_window, login_data):
        verify_window.setObjectName("verify_window")
        verify_window.resize(520, 217)
        self.verify_title = QtWidgets.QLabel(verify_window)
        self.verify_title.setGeometry(QtCore.QRect(90, 10, 361, 61))
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
        self.verify_button_1.setGeometry(QtCore.QRect(110, 170, 100, 31))
        self.verify_button_1.setObjectName("verify_button_1")
        self.verify_button_1.clicked.connect(lambda: self.verify(login_data))
        self.verify_button_2 = QtWidgets.QPushButton(verify_window)
        self.verify_button_2.setGeometry(QtCore.QRect(310, 170, 100, 31))
        self.verify_button_2.setObjectName("verify_button_2")
        self.verify_button_2.clicked.connect(
            lambda: self.cancel(verify_window, main_window)
        )
        self.worker = Worker()
        self.worker.finished.connect(lambda: self.pop_up.close())
        self.worker.worker_complete.connect(
            lambda x: self.createResultsWindow(x, verify_window)
        )

        self.retranslateUi(verify_window)
        QtCore.QMetaObject.connectSlotsByName(verify_window)

    def retranslateUi(self, verify_window):
        _translate = QtCore.QCoreApplication.translate
        verify_window.setWindowTitle(_translate("verify_window", "Verify"))
        self.verify_title.setText(_translate("verify_window", "Verify Certificate"))
        self.verify_label_1.setText(_translate("verify_window", "URL"))
        self.verify_button_1.setText(_translate("verify_window", "Search"))
        self.verify_button_2.setText(_translate("verify_window", "Cancel"))

    def verify(self, login_data):
        self.worker.args(login_data, self.verify_line_1.text())
        self.showPopUp()
        self.worker.start()

    def showPopUp(self):
        self.pop_up = QtWidgets.QDialog()
        ui = Ui_dialog()
        ui.setupUi(self.pop_up, "Verifing Certificate", "Searching...")
        self.pop_up.show()

    def createResultsWindow(self, out, verify_window):
        if out[0] != False:
            verify_window.hide()
            verify_results_window = QtWidgets.QWidget()
            ui = Ui_verify_results_window()
            ui.setupUi(verify_results_window, verify_window, out)
            verify_results_window.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Execution Reverted!")
            msg.setInformativeText(str(out[1]))
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def cancel(self, verify_window, main_window):
        main_window.show()
        verify_window.close()


class Worker(QThread):
    worker_complete = pyqtSignal(list)

    def run(self):
        # time.sleep(5)
        out = self.verify.verify(self.url)
        self.worker_complete.emit(out)

    def args(self, login_data, url):
        self.verify = Verify(login_data.session.endpoint)
        self.url = url


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    verify_window = QtWidgets.QWidget()
    ui = Ui_verify_window()
    ui.setupUi(verify_window)
    verify_window.show()
    sys.exit(app.exec_())
