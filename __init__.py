import sys
from PyQt5 import QtWidgets
from GUI.Scripts.sign_window import Ui_signinsignup_window
from Scripts.compile import Compile
from Scripts.gererate_keys import GenerateKeys
from Scripts.generate_certificate import GenerateCertificate
from Scripts.install_certificate import InstallCertificate

if __name__ == "__main__":
    # compile = Compile()
    # compile.compilePublicKeyChain()
    # compile.compilePublicKeyChainFactory()
    app = QtWidgets.QApplication(sys.argv)
    signinsignup_window = QtWidgets.QWidget()
    ui = Ui_signinsignup_window()
    ui.setupUi(signinsignup_window)
    signinsignup_window.show()
    sys.exit(app.exec_())
    # genK = GenerateKeys()
    # genK.generate_keys("abc123")
    # genC = GenerateCertificate()
    # genC.generate_certificate(
    #    password="abc123", common_name="mysite.com", country_name="BR"
    # )
    # insC = InstallCertificate("alerei1998")
    # insC.copy_certificate()
    # insC.install_certificate()
