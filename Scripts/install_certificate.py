import subprocess


class InstallCertificate(object):
    def __init__(self, sudo_password, cert_address, certificate):
        self.sudo_password = sudo_password
        self.cert_address = cert_address
        self.certificate = certificate

    def copy_certificate(self):
        with open(
            "/usr/local/share/ca-certificates/" + self.cert_address + ".crt", "wb"
        ) as f:
            f.write(self.certificate)

    def remove_certificate(self):
        command = (
            "rm /usr/local/share/ca-certificates/" + self.cert_address + ".crt".split()
        )

        p = subprocess.Popen(
            ["sudo", "-S"] + command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        stdout, stderr = p.communicate(self.sudo_password + "\n")
        print(stdout)
        print(stderr)
        print("Done!")

    def install_certificate(self):
        command = "update-ca-certificates".split()

        p = subprocess.Popen(
            ["sudo", "-S"] + command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        stdout, stderr = p.communicate(self.sudo_password + "\n")
        print(stdout)
        print(stderr)
        print("Done!")
