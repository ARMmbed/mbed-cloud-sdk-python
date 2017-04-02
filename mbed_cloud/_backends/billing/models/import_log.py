# coding: utf-8

"""
    mbed-billing REST API documentation for API-server

    This document contains the public REST API definitions of the mbed-billing service's API server component.

    OpenAPI spec version: 1.3.4-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ImportLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, import_id=None, bootstrap_count=None, _from=None, service=None, timestamp=None, transaction_count=None, device_count=None, to=None, firmware_update_count=None):
        """
        ImportLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'import_id': 'int',
            'bootstrap_count': 'int',
            '_from': 'int',
            'service': 'str',
            'timestamp': 'int',
            'transaction_count': 'int',
            'device_count': 'int',
            'to': 'int',
            'firmware_update_count': 'int'
        }

        self.attribute_map = {
            'import_id': 'import_id',
            'bootstrap_count': 'bootstrap_count',
            '_from': 'from',
            'service': 'service',
            'timestamp': 'timestamp',
            'transaction_count': 'transaction_count',
            'device_count': 'device_count',
            'to': 'to',
            'firmware_update_count': 'firmware_update_count'
        }

        self._import_id = import_id
        self._bootstrap_count = bootstrap_count
        self.__from = _from
        self._service = service
        self._timestamp = timestamp
        self._transaction_count = transaction_count
        self._device_count = device_count
        self._to = to
        self._firmware_update_count = firmware_update_count

    @property
    def import_id(self):
        """
        Gets the import_id of this ImportLog.

        :return: The import_id of this ImportLog.
        :rtype: int
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """
        Sets the import_id of this ImportLog.

        :param import_id: The import_id of this ImportLog.
        :type: int
        """
        if import_id is None:
            raise ValueError("Invalid value for `import_id`, must not be `None`")

        self._import_id = import_id

    @property
    def bootstrap_count(self):
        """
        Gets the bootstrap_count of this ImportLog.

        :return: The bootstrap_count of this ImportLog.
        :rtype: int
        """
        return self._bootstrap_count

    @bootstrap_count.setter
    def bootstrap_count(self, bootstrap_count):
        """
        Sets the bootstrap_count of this ImportLog.

        :param bootstrap_count: The bootstrap_count of this ImportLog.
        :type: int
        """

        self._bootstrap_count = bootstrap_count

    @property
    def _from(self):
        """
        Gets the _from of this ImportLog.

        :return: The _from of this ImportLog.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this ImportLog.

        :param _from: The _from of this ImportLog.
        :type: int
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def service(self):
        """
        Gets the service of this ImportLog.

        :return: The service of this ImportLog.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this ImportLog.

        :param service: The service of this ImportLog.
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")

        self._service = service

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ImportLog.

        :return: The timestamp of this ImportLog.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ImportLog.

        :param timestamp: The timestamp of this ImportLog.
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def transaction_count(self):
        """
        Gets the transaction_count of this ImportLog.

        :return: The transaction_count of this ImportLog.
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """
        Sets the transaction_count of this ImportLog.

        :param transaction_count: The transaction_count of this ImportLog.
        :type: int
        """

        self._transaction_count = transaction_count

    @property
    def device_count(self):
        """
        Gets the device_count of this ImportLog.

        :return: The device_count of this ImportLog.
        :rtype: int
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """
        Sets the device_count of this ImportLog.

        :param device_count: The device_count of this ImportLog.
        :type: int
        """

        self._device_count = device_count

    @property
    def to(self):
        """
        Gets the to of this ImportLog.

        :return: The to of this ImportLog.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this ImportLog.

        :param to: The to of this ImportLog.
        :type: int
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")

        self._to = to

    @property
    def firmware_update_count(self):
        """
        Gets the firmware_update_count of this ImportLog.

        :return: The firmware_update_count of this ImportLog.
        :rtype: int
        """
        return self._firmware_update_count

    @firmware_update_count.setter
    def firmware_update_count(self, firmware_update_count):
        """
        Sets the firmware_update_count of this ImportLog.

        :param firmware_update_count: The firmware_update_count of this ImportLog.
        :type: int
        """

        self._firmware_update_count = firmware_update_count

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ImportLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
