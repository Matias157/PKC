import sys
from PyQt5 import QtWidgets
from GUI.Scripts.main_window import Ui_main_window
from Scripts.compile import Compile

if __name__ == "__main__":
    # compile = Compile()
    # compile.compilePublicKeyChain()
    # compile.compilePublicKeyChainFactory()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
