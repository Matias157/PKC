import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


class GenerateCertificate(object):
    def generate_certificate(
        self,
        password,
        address,
        private_key_direct,
        common_name,
        country_name="",
        locality_name="",
        state_or_province_name="",
        street_address="",
        organization_name="",
        organizational_unit_name="",
        serial_number="",
        surname="",
        given_name="",
        title="",
        generation_qualifier="",
        x500_unique_identifier="",
        dn_qualifier="",
        pseudonym="",
        user_id="",
        domain_component="",
        email_address="",
        jurisdiction_country_name="",
        jurisdiction_locality_name="",
        jurisdiction_state_or_province_name="",
        business_category="",
        postal_address="",
        postal_code="",
    ):
        with open(private_key_direct, "rb") as key:
            key = serialization.load_pem_private_key(
                key.read(), password=password.encode()
            )

        attrs = [x509.NameAttribute(NameOID.COMMON_NAME, common_name)]
        if country_name != "":
            attrs.append(x509.NameAttribute(NameOID.COUNTRY_NAME, country_name))
        elif state_or_province_name != "":
            attrs.append(
                x509.NameAttribute(
                    NameOID.STATE_OR_PROVINCE_NAME, state_or_province_name
                )
            )
        elif street_address != "":
            attrs.append(x509.NameAttribute(NameOID.STREET_ADDRESS, street_address))
        elif locality_name != "":
            attrs.append(x509.NameAttribute(NameOID.LOCALITY_NAME, locality_name))
        elif organization_name != "":
            attrs.append(
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization_name)
            )
        elif organizational_unit_name != "":
            attrs.append(
                x509.NameAttribute(
                    NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit_name
                )
            )
        elif serial_number != "":
            attrs.append(x509.NameAttribute(NameOID.SERIAL_NUMBER, serial_number))
        elif surname != "":
            attrs.append(x509.NameAttribute(NameOID.SURNAME, surname))
        elif given_name != "":
            attrs.append(x509.NameAttribute(NameOID.GIVEN_NAME, given_name))
        elif title != "":
            attrs.append(x509.NameAttribute(NameOID.TITLE, title))
        elif generation_qualifier != "":
            attrs.append(
                x509.NameAttribute(NameOID.GENERATION_QUALIFIER, generation_qualifier)
            )
        elif x500_unique_identifier != "":
            attrs.append(
                x509.NameAttribute(
                    NameOID.X500_UNIQUE_IDENTIFIER, x500_unique_identifier
                )
            )
        elif dn_qualifier != "":
            attrs.append(x509.NameAttribute(NameOID.DN_QUALIFIER, dn_qualifier))
        elif pseudonym != "":
            attrs.append(x509.NameAttribute(NameOID.PSEUDONYM, pseudonym))
        elif user_id != "":
            attrs.append(x509.NameAttribute(NameOID.USER_ID, user_id))
        elif domain_component != "":
            attrs.append(x509.NameAttribute(NameOID.DOMAIN_COMPONENT, domain_component))
        elif email_address != "":
            attrs.append(x509.NameAttribute(NameOID.EMAIL_ADDRESS, email_address))
        elif jurisdiction_country_name != "":
            attrs.append(
                x509.NameAttribute(
                    NameOID.JURISDICTION_COUNTRY_NAME, jurisdiction_country_name
                )
            )
        elif jurisdiction_locality_name != "":
            attrs.append(
                x509.NameAttribute(
                    NameOID.JURISDICTION_LOCALITY_NAME, jurisdiction_locality_name
                )
            )
        elif jurisdiction_state_or_province_name != "":
            attrs.append(
                x509.NameAttribute(
                    NameOID.JURISDICTION_STATE_OR_PROVINCE_NAME,
                    jurisdiction_state_or_province_name,
                )
            )
        elif business_category != "":
            attrs.append(
                x509.NameAttribute(NameOID.BUSINESS_CATEGORY, business_category)
            )
        elif postal_address != "":
            attrs.append(x509.NameAttribute(NameOID.POSTAL_ADDRESS, postal_address))
        elif postal_code != "":
            attrs.append(x509.NameAttribute(NameOID.POSTAL_CODE, postal_code))

        subject = issuer = x509.Name(attrs)

        cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
            .add_extension(
                x509.SubjectAlternativeName([x509.DNSName(common_name)]),
                critical=False,
            )
            .sign(key, hashes.SHA256())
        )

        print(cert.public_bytes(serialization.Encoding.PEM))
        with open("Data/UserData/" + address + "/certificate.crt", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
