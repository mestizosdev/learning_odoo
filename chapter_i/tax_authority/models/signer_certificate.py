from odoo import fields, models, tools
from typing import Union

from cryptography.hazmat.primitives.serialization import pkcs12

from base64 import b64decode

class SignerCertificate(models.Model):
    _name = 'signer.certificate'
    _description = 'Electronic Signature Certificate'

    name = fields.Char(required=True)
    file_content = fields.Binary(string="Signature File")
    file_name = fields.Char(string="Filename")
    password = fields.Char(string="Signing key")
    active = fields.Boolean(string="Active?", default=True)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
    state = fields.Selection(
        [
            ("unverified", "Unverified"),
            ("valid", "Valid Signature"),
            ("expired", "Signature Expired"),
        ],
        default="unverified",
        readonly=True,
    )
    issue_date = fields.Date(string="Date of issue", readonly=True)
    expire_date = fields.Date(string="Expiration date", readonly=True)
    subject_serial_number = fields.Char(string="Serial Number(Subject)", readonly=True)
    subject_common_name = fields.Char(string="Organization(Subject)", readonly=True)
    issuer_common_name = fields.Char(string="Organization (Issuer)", readonly=True)
    cert_serial_number = fields.Char(
        string="Serial number (certificate)", readonly=True
    )
    cert_version = fields.Char(string="Version", readonly=True)

    def action_validate_and_load(self):
        print("action_validate_and_load")
        self._decode_certificate()
        return True

    @tools.ormcache("self.file_content", "self.password", "self.state")
    def _decode_certificate(self):
        print("_decode_certificate")
        file_content = b64decode(self.file_content)
        self.read_pfx_file(file_content, self.password)

    def read_pfx_file(self, pfx_file: Union[str, bytes], password):
        try:
            if isinstance(pfx_file, str):
                with open(pfx_file, "rb") as cert_file:
                    cert_content = cert_file.read()
            elif isinstance(pfx_file, bytes):
                cert_content = pfx_file
            else:
                raise RuntimeError("pfx_file must be str or bytes")

            private_key, cert, additional_certificates = pkcs12.load_key_and_certificates(
                cert_content,
                password.encode()
            )
            print("private_key", private_key)
            print("cert", cert)
            print("additional_certificates", additional_certificates)

        except FileNotFoundError as err:
            raise FileNotFoundError(f"File not found. {err}")
        except Exception as err:
            raise Exception(f"Fail to open file. {err}")