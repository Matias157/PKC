import os
import subprocess


class InstallCertificate(object):
    def __init__(self, sudo_password, address, certificate, cert_address):
        self.sudo_password = sudo_password
        self.address = address
        self.cert_address = cert_address
        with open(
            "Data/UserData/" + self.address + "/" + self.cert_address + ".crt", "wb"
        ) as f:
            f.write(certificate)

    def copy_certificate(self):
        if not os.path.exists(
            "/usr/local/share/ca-certificates/" + str(self.cert_address) + ".crt"
        ):
            command = (
                "cp Data/UserData/"
                + str(self.address)
                + "/"
                + str(self.cert_address)
                + ".crt /usr/local/share/ca-certificates"
            )
            command = command.split()

            p = subprocess.Popen(
                ["sudo", "-k", "-S"] + command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            stdout, stderr = p.communicate(self.sudo_password + "\n")
            os.remove(
                "Data/UserData/" + self.address + "/" + self.cert_address + ".crt"
            )
            if p.returncode == 0:
                return True
            else:
                return stderr
        else:
            os.remove(
                "Data/UserData/" + self.address + "/" + self.cert_address + ".crt"
            )
            return "Certificate already installed"

    def install_certificate(self):
        copy = self.copy_certificate()
        if copy == True:
            command = "update-ca-certificates --fresh".split()

            p = subprocess.Popen(
                ["sudo", "-k", "-S"] + command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            stdout, stderr = p.communicate(self.sudo_password + "\n")
            if p.returncode == 0:
                return True
            else:
                return stderr
        else:
            return copy

    def delete_certificate(self):
        if os.path.exists(
            "/usr/local/share/ca-certificates/" + str(self.cert_address) + ".crt"
        ):
            command = (
                "rm /usr/local/share/ca-certificates/" + str(self.cert_address) + ".crt"
            )
            command = command.split()

            p = subprocess.Popen(
                ["sudo", "-k", "-S"] + command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            stdout, stderr = p.communicate(self.sudo_password + "\n")

            if p.returncode == 0:
                return True
            else:
                return stderr
        else:
            return "Certificate not installed"

    def remove_certificate(self):
        delete = self.delete_certificate()
        if delete == True:
            command = "update-ca-certificates --fresh".split()

            p = subprocess.Popen(
                ["sudo", "-k", "-S"] + command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            stdout, stderr = p.communicate(self.sudo_password + "\n")
            if p.returncode == 0:
                return True
            else:
                return stderr
        else:
            return delete
