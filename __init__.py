import sys
import os.path
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
