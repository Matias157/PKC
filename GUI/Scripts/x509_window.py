# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UIs/x509_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from tldextract import extract
from urllib.parse import urlparse
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from GUI.Scripts.rsa_window import Ui_rsa_window
from Scripts.generate_certificate import GenerateCertificate


class Ui_x509_window(object):
    def setupUi(self, x509_window, create_certificate_window, login_data):
        x509_window.setObjectName("x509_window")
        x509_window.resize(619, 794)
        x509_window.setFixedSize(619, 794)
        self.tableWidget = QtWidgets.QTableWidget(x509_window)
        self.tableWidget.setGeometry(QtCore.QRect(10, 530, 591, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        self.tableWidget.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(23)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.x509_label_1 = QtWidgets.QLabel(x509_window)
        self.x509_label_1.setGeometry(QtCore.QRect(10, 190, 111, 19))
        self.x509_label_1.setObjectName("x509_label_1")
        self.x509_button_3 = QtWidgets.QPushButton(x509_window)
        self.x509_button_3.setGeometry(QtCore.QRect(500, 350, 100, 31))
        self.x509_button_3.setObjectName("x509_button_3")
        self.x509_button_3.clicked.connect(
            lambda: self.browseFiles(x509_window, login_data)
        )
        self.x509_label_1_1 = QtWidgets.QLabel(x509_window)
        self.x509_label_1_1.setGeometry(QtCore.QRect(10, 230, 171, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.x509_label_1_1.setFont(font)
        self.x509_label_1_1.setObjectName("x509_label_1_1")
        self.x509_line_3 = QtWidgets.QLineEdit(x509_window)
        self.x509_line_3.setGeometry(QtCore.QRect(10, 350, 461, 31))
        self.x509_line_3.setObjectName("x509_line_3")
        self.x509_button_4 = QtWidgets.QPushButton(x509_window)
        self.x509_button_4.setGeometry(QtCore.QRect(10, 260, 100, 31))
        self.x509_button_4.setObjectName("x509_button_4")
        self.x509_button_4.clicked.connect(
            lambda: self.createRSAWindow(x509_window, login_data)
        )
        self.x509_label_1_2 = QtWidgets.QLabel(x509_window)
        self.x509_label_1_2.setGeometry(QtCore.QRect(10, 320, 121, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.x509_label_1_2.setFont(font)
        self.x509_label_1_2.setObjectName("x509_label_1_2")
        self.create_title = QtWidgets.QLabel(x509_window)
        self.create_title.setGeometry(QtCore.QRect(150, 10, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.create_title.setFont(font)
        self.create_title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.create_title.setObjectName("create_title")
        self.x509_label_2 = QtWidgets.QLabel(x509_window)
        self.x509_label_2.setGeometry(QtCore.QRect(10, 500, 141, 19))
        self.x509_label_2.setObjectName("x509_label_2")
        self.x509_button_2 = QtWidgets.QPushButton(x509_window)
        self.x509_button_2.setGeometry(QtCore.QRect(430, 750, 100, 31))
        self.x509_button_2.setObjectName("x509_button_2")
        self.x509_button_2.clicked.connect(
            lambda: self.cancel(x509_window, create_certificate_window)
        )
        self.x509_button_1 = QtWidgets.QPushButton(x509_window)
        self.x509_button_1.setGeometry(QtCore.QRect(110, 750, 100, 31))
        self.x509_button_1.setObjectName("x509_button_1")
        self.x509_button_1.clicked.connect(
            lambda: self.create(x509_window, create_certificate_window, login_data)
        )
        self.x509_line_2 = QtWidgets.QLineEdit(x509_window)
        self.x509_line_2.setGeometry(QtCore.QRect(10, 440, 601, 31))
        self.x509_line_2.setObjectName("x509_line_2")
        self.x509_line_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.x509_label_1_3 = QtWidgets.QLabel(x509_window)
        self.x509_label_1_3.setGeometry(QtCore.QRect(10, 410, 171, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.x509_label_1_3.setFont(font)
        self.x509_label_1_3.setObjectName("x509_label_1_3")
        self.x509_line_1 = QtWidgets.QLineEdit(x509_window)
        self.x509_line_1.setGeometry(QtCore.QRect(10, 130, 601, 31))
        self.x509_line_1.setObjectName("x509_line_1")
        self.x509_label_3 = QtWidgets.QLabel(x509_window)
        self.x509_label_3.setGeometry(QtCore.QRect(10, 100, 81, 19))
        self.x509_label_3.setObjectName("x509_label_3")

        self.retranslateUi(x509_window)
        QtCore.QMetaObject.connectSlotsByName(x509_window)

    def retranslateUi(self, x509_window):
        _translate = QtCore.QCoreApplication.translate
        x509_window.setWindowTitle(_translate("x509_window", "x509 Certificate"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("x509_window", "Country Name"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("x509_window", "Locality Name"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("x509_window", "State or Province Name"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("x509_window", "Street Address"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("x509_window", "Organization Name"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("x509_window", "Organizational Unit Name"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("x509_window", "Serial Number"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("x509_window", "Surname"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("x509_window", "Given Name"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("x509_window", "Title"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("x509_window", "Generation Qualifier"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("x509_window", "x500 Unique Identifier"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("x509_window", "DN Qualifier"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("x509_window", "Pseudonym"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("x509_window", "User ID"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("x509_window", "Domain Component"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("x509_window", "E-mail Address"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("x509_window", "Jurisdiction Country Name"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("x509_window", "Jurisdiction Locality Name"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("x509_window", "Jurisdiction State or Province Name"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("x509_window", "Business Category"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("x509_window", "Postal Address"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("x509_window", "Postal Code"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("x509_window", "Attribute"))
        self.x509_label_1.setText(_translate("x509_window", "RSA Private Key"))
        self.x509_button_3.setText(_translate("x509_window", "Select"))
        self.x509_label_1_1.setText(
            _translate("x509_window", "Generate a new RSA Private Key")
        )
        self.x509_button_4.setText(_translate("x509_window", "Generate"))
        self.x509_label_1_2.setText(_translate("x509_window", "Browse your PEM file"))
        self.create_title.setText(_translate("x509_window", "x509 Certificate"))
        self.x509_label_2.setText(_translate("x509_window", "Attributes (optional)"))
        self.x509_button_2.setText(_translate("x509_window", "Cancel"))
        self.x509_button_1.setText(_translate("x509_window", "Create"))
        self.x509_label_1_3.setText(
            _translate("x509_window", "PEM file password (not stored)")
        )
        self.x509_label_3.setText(_translate("x509_window", "URL"))

    def browseFiles(self, x509_window, login_data):
        fname = QFileDialog.getOpenFileName(
            x509_window, "Open file", "./Data/UserData/" + login_data.session.address
        )
        self.x509_line_3.setText(fname[0])

    def validateUrl(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def create(self, x509_window, create_certificate_window, login_data):
        if self.validateUrl(self.x509_line_1.text()):
            self.generate_certificate = GenerateCertificate()
            try:
                attrbs = []
                for i in range(23):
                    if self.tableWidget.item(i, 0) is not None:
                        attrbs.append(self.tableWidget.item(i, 0).text())
                    else:
                        attrbs.append("")
                dir = self.generate_certificate.generate_certificate(
                    self.x509_line_2.text(),
                    login_data.session.address,
                    self.x509_line_3.text(),
                    extract(self.x509_line_1.text()).registered_domain,
                    attrbs[0],
                    attrbs[1],
                    attrbs[2],
                    attrbs[3],
                    attrbs[4],
                    attrbs[5],
                    attrbs[6],
                    attrbs[7],
                    attrbs[8],
                    attrbs[9],
                    attrbs[10],
                    attrbs[11],
                    attrbs[12],
                    attrbs[13],
                    attrbs[14],
                    attrbs[15],
                    attrbs[16],
                    attrbs[17],
                    attrbs[18],
                    attrbs[19],
                    attrbs[20],
                    attrbs[21],
                    attrbs[22],
                )
                self.showMsgBox(
                    x509_window,
                    create_certificate_window,
                    "Completion",
                    "Certificate created!",
                    "Your Certificate was saved to " + str(dir),
                    False,
                )
            except Exception as e:
                self.showMsgBox(
                    x509_window,
                    create_certificate_window,
                    "Error",
                    "An error has occurred!",
                    str(e),
                    True,
                )
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Invalid URL!")
            msg.setInformativeText(
                "The informed URL is invalid or incorrectly formated"
            )
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def createRSAWindow(self, x509_window, login_data):
        x509_window.hide()
        self.rsa_window = QtWidgets.QWidget()
        self.ui = Ui_rsa_window()
        self.ui.setupUi(self.rsa_window, x509_window, login_data)
        self.rsa_window.show()

    def showMsgBox(
        self, x509_window, create_certificate_window, title, text, inform, err
    ):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setInformativeText(inform)
        if err:
            msg.setIcon(QMessageBox.Critical)
        else:
            msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(
            lambda: self.cancel(x509_window, create_certificate_window)
        )
        x = msg.exec_()

    def cancel(self, x509_window, create_certificate_window):
        create_certificate_window.show()
        x509_window.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    x509_window = QtWidgets.QWidget()
    ui = Ui_x509_window()
    ui.setupUi(x509_window)
    x509_window.show()
    sys.exit(app.exec_())
