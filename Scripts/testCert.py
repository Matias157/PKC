from cryptography import x509
from cryptography.hazmat.primitives import serialization

with open(
    "../Data/UserData/0x07A9CF7790300E884C35A97041059e2941B9EaB6/certificate.crt", "rb"
) as crt:
    cert = x509.load_pem_x509_certificate(crt.read())

attrList = []
for attribute in cert.subject:
    attrList.append(str(attribute.oid._name))
    attrList.append(str(attribute.value))

print(attrList)
print(cert.public_bytes(serialization.Encoding.PEM).decode("utf-8"))
