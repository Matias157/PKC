from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class GenerateKeys(object):
    def generate_keys(self, password, address):
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        with open("Data/UserData/" + address + "/private_key.pem", "wb") as f:
            f.write(
                key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.BestAvailableEncryption(
                        password.encode()
                    ),
                )
            )
