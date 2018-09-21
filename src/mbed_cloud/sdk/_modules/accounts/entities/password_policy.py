"""
Entity module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class PasswordPolicy(Entity):
    """Represents the `PasswordPolicy` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = []

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(self, _client=None):
        """Creates a local `PasswordPolicy` instance

        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
