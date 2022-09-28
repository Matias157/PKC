import os
import subprocess


class UninstallCertificate(object):
    def __init__(self, sudo_password, address, cert_address):
        self.sudo_password = sudo_password
        self.address = address
        self.cert_address = cert_address

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

    def update_ca_remove(self):
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

    def change_permissions(self, install):
        if install:
            update = self.update_ca_install()
        else:
            update = self.update_ca_remove()
        if update == True:
            if install:
                command = "chmod 777 Scripts/install_certificate.sh".split()
            else:
                command = "chmod 777 Scripts/remove_certificate.sh".split()

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
            return update

    def remove_certificate(self):
        perm = self.change_permissions(False)
        if perm == True:
            command = "./Scripts/remove_certificate.sh " + str(self.cert_address)
            command = command.split()

            p = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            stdout, stderr = p.communicate()
            if p.returncode == 0:
                return True
            else:
                return stderr
        else:
            return perm
