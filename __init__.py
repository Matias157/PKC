import sys
import os.path
import csv
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from GUI.Scripts.sign_window import Ui_signinsignup_window
from Scripts.compile import Compile


if __name__ == "__main__":
    if not os.path.exists("Data/CompiledFiles/compiled_public_key_chain_factory.json"):
        compile = Compile()
        compile.compilePublicKeyChainFactory()
    if not os.path.exists("Data/CompiledFiles/compiled_public_key_chain.json"):
        compile = Compile()
        compile.compilePublicKeyChain()
    if not os.path.exists("Data/UserData/accounts.csv"):
        with open("Data/UserData/accounts.csv", "w") as file:
            databasewriter = csv.writer(
                file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            databasewriter.writerow(["address", "endpoint", "password"])
    app = QtWidgets.QApplication(sys.argv)

    file = QFile("dark/stylesheet.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    signinsignup_window = QtWidgets.QWidget()
    ui = Ui_signinsignup_window()
    ui.setupUi(signinsignup_window)
    signinsignup_window.show()
    sys.exit(app.exec_())
