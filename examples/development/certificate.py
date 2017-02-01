# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Example showing basic usage of developer certificates."""
from mbed_cloud.development import DevelopmentAPI
import sys

DUMMY_PUB_KEY = """
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAENVRAgPj7Ra2K/BqejIhY+oSRylHS
CdV7NZ9yEDGifNYYi0nZVpHwmbepoMbBW7jTJKjNDHaf8MhBsKPd0yyI4Q==
"""


def _print_certificate(cert):
    body = "* %s (%s) *" % (cert.pub_key, cert.created_at)
    print("*" * len(body))
    print(body)
    print("*" * len(body))


def _main():
    api = DevelopmentAPI()
    cert = api.get_certificate()

    if cert:
        print("Current certificate:")
        _print_certificate(cert)

        api.revoke_certificate()
        print("Revoked current certificate. Creating new one...")

    # Get public key from first argument on command line
    pub_key = DUMMY_PUB_KEY.strip().replace("\n", "")
    if len(sys.argv) == 2:
        pub_key = sys.argv[1]

    new_cert = api.create_certificate(pub_key)
    print("Created new certificate!")
    _print_certificate(new_cert)

if __name__ == "__main__":
    _main()
