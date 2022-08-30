# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UIs/custom_input_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_custom_input_window(QDialog, object):
    def __init__(self, window_name, text, passw):
        super(Ui_custom_input_window, self).__init__()
        self.setupUi(self, window_name, text, passw)

    def setupUi(self, custom_input_window, window_name, text, passw):
        custom_input_window.setObjectName("custom_input_window")
        custom_input_window.resize(332, 127)
        self.buttonBox = QtWidgets.QDialogButtonBox(custom_input_window)
        self.buttonBox.setGeometry(QtCore.QRect(10, 90, 311, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(custom_input_window)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 311, 33))
        self.lineEdit.setObjectName("lineEdit")
        if passw:
            self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(custom_input_window)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 19))
        self.label.setObjectName("label")

        self.retranslateUi(custom_input_window, window_name, text)
        self.buttonBox.accepted.connect(custom_input_window.accept)
        self.buttonBox.rejected.connect(custom_input_window.reject)
        QtCore.QMetaObject.connectSlotsByName(custom_input_window)

    def retranslateUi(self, custom_input_window, window_name, text):
        _translate = QtCore.QCoreApplication.translate
        custom_input_window.setWindowTitle(
            _translate("custom_input_window", window_name)
        )
        self.label.setText(_translate("custom_input_window", text))

    def getResults(self):
        if self.exec_() == QDialog.Accepted:
            val = self.lineEdit.text()
            return val
        else:
            return None


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    custom_input_window = QtWidgets.QDialog()
    ui = Ui_custom_input_window()
    ui.setupUi(custom_input_window)
    custom_input_window.show()
    sys.exit(app.exec_())
