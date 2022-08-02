# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UIs/verify_results_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import insert


class Ui_verify_results_window(object):
    def setupUi(self, verify_results_window, verify_window, data):
        verify_results_window.setObjectName("verify_results_window")
        verify_results_window.resize(535, 416)
        self.verifyres_table = QtWidgets.QTableWidget(verify_results_window)
        self.verifyres_table.setGeometry(QtCore.QRect(10, 90, 511, 261))
        self.verifyres_table.setObjectName("veirfyres_table")
        self.verifyres_table.setColumnCount(2)
        self.verifyres_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem())
        self.verifyres_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem())
        self.verifyres_title = QtWidgets.QLabel(verify_results_window)
        self.verifyres_title.setGeometry(QtCore.QRect(120, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.verifyres_title.setFont(font)
        self.verifyres_title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verifyres_title.setObjectName("verifyres_title")
        self.verifyres_button_2 = QtWidgets.QPushButton(verify_results_window)
        self.verifyres_button_2.setGeometry(QtCore.QRect(380, 370, 100, 31))
        self.verifyres_button_2.setObjectName("verifyres_button_2")
        self.verifyres_button_1 = QtWidgets.QPushButton(verify_results_window)
        self.verifyres_button_1.setGeometry(QtCore.QRect(50, 370, 100, 31))
        self.verifyres_button_1.setObjectName("verifyres_button_1")
        self.verifyres_button_1.clicked.connect(
            lambda: self.cancel(verify_results_window, verify_window)
        )
        self.verifyres_button_3 = QtWidgets.QPushButton(verify_results_window)
        self.verifyres_button_3.setGeometry(QtCore.QRect(210, 370, 100, 31))
        self.verifyres_button_3.setObjectName("verifyres_button_3")
        self.verifyres_button_3.hide()
        self.verifyres_button_3.clicked.connect(lambda: self.showDetails())
        self.verifyres_table.itemClicked.connect(lambda: self.showDetailsButton())
        for cert in data:
            self.insertTable(cert[0], cert[1])

        self.retranslateUi(verify_results_window)
        QtCore.QMetaObject.connectSlotsByName(verify_results_window)

    def retranslateUi(self, verify_results_window):
        _translate = QtCore.QCoreApplication.translate
        verify_results_window.setWindowTitle(
            _translate("verify_results_window", "Verify Results")
        )
        self.verifyres_title.setText(
            _translate("verify_results_window", "Verify Results")
        )
        self.verifyres_button_2.setText(
            _translate("verify_results_window", "Init Proxy")
        )
        self.verifyres_button_1.setText(_translate("verify_results_window", "Back"))
        self.verifyres_button_3.setText(
            _translate("verify_results_window", "Show Details")
        )
        self.verifyres_table.horizontalHeaderItem(0).setText(
            _translate("verify_results_window", "Address")
        )
        self.verifyres_table.horizontalHeaderItem(1).setText(
            _translate("verify_results_window", "URL")
        )

    def insertTable(self, t0, t1):
        rowPosition = self.verifyres_table.rowCount()
        self.verifyres_table.insertRow(rowPosition)
        self.verifyres_table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(t0))
        self.verifyres_table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(t1))
        self.verifyres_table.resizeColumnToContents(0)
        self.verifyres_table.resizeColumnToContents(1)

    def showDetailsButton(self):
        self.verifyres_button_3.show()

    def showDetails(self):
        index = self.verifyres_table.currentRow()
        print(self.verifyres_table.item(index, 0).text())

    def cancel(self, verify_results_window, verify_window):
        verify_window.show()
        verify_results_window.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    verify_results_window = QtWidgets.QWidget()
    ui = Ui_verify_results_window()
    ui.setupUi(verify_results_window)
    verify_results_window.show()
    sys.exit(app.exec_())