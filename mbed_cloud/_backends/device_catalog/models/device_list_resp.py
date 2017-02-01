# coding: utf-8

"""
    Device Catalog API

    This is the API Documentation for the mbed device catalog update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceListResp(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, object=None, has_more=None, total_count=None, after=None, limit=None, data=None, order=None):
        """
        DeviceListResp - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'object': 'str',
            'has_more': 'bool',
            'total_count': 'int',
            'after': 'str',
            'limit': 'int',
            'data': 'list[DeviceDetail]',
            'order': 'str'
        }

        self.attribute_map = {
            'object': 'object',
            'has_more': 'has_more',
            'total_count': 'total_count',
            'after': 'after',
            'limit': 'limit',
            'data': 'data',
            'order': 'order'
        }

        self._object = object
        self._has_more = has_more
        self._total_count = total_count
        self._after = after
        self._limit = limit
        self._data = data
        self._order = order

    @property
    def object(self):
        """
        Gets the object of this DeviceListResp.
        API Resource name

        :return: The object of this DeviceListResp.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceListResp.
        API Resource name

        :param object: The object of this DeviceListResp.
        :type: str
        """

        self._object = object

    @property
    def has_more(self):
        """
        Gets the has_more of this DeviceListResp.
        Whether there are more results to display

        :return: The has_more of this DeviceListResp.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this DeviceListResp.
        Whether there are more results to display

        :param has_more: The has_more of this DeviceListResp.
        :type: bool
        """

        self._has_more = has_more

    @property
    def total_count(self):
        """
        Gets the total_count of this DeviceListResp.
        Total number of records

        :return: The total_count of this DeviceListResp.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this DeviceListResp.
        Total number of records

        :param total_count: The total_count of this DeviceListResp.
        :type: int
        """

        self._total_count = total_count

    @property
    def after(self):
        """
        Gets the after of this DeviceListResp.
        Entity id for fetch after it

        :return: The after of this DeviceListResp.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this DeviceListResp.
        Entity id for fetch after it

        :param after: The after of this DeviceListResp.
        :type: str
        """

        self._after = after

    @property
    def limit(self):
        """
        Gets the limit of this DeviceListResp.
        The number of results to return

        :return: The limit of this DeviceListResp.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this DeviceListResp.
        The number of results to return

        :param limit: The limit of this DeviceListResp.
        :type: int
        """

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this DeviceListResp.

        :return: The data of this DeviceListResp.
        :rtype: list[DeviceDetail]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this DeviceListResp.

        :param data: The data of this DeviceListResp.
        :type: list[DeviceDetail]
        """

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this DeviceListResp.
        Order of returned records

        :return: The order of this DeviceListResp.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this DeviceListResp.
        Order of returned records

        :param order: The order of this DeviceListResp.
        :type: str
        """

        self._order = order

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
        if not isinstance(other, DeviceListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
