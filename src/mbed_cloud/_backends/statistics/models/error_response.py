# coding: utf-8

"""
    Connect Statistics API

    Connect Statistics API provides statistics about other cloud services through defined counters.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ErrorResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'fields': 'list[Fields]',
        'message': 'str',
        'object': 'str',
        'request_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'fields': 'fields',
        'message': 'message',
        'object': 'object',
        'request_id': 'request_id',
        'type': 'type'
    }

    def __init__(self, code=None, fields=None, message=None, object=None, request_id=None, type=None):
        """
        ErrorResponse - a model defined in Swagger
        """

        self._code = code
        self._fields = fields
        self._message = message
        self._object = object
        self._request_id = request_id
        self._type = type
        self.discriminator = None

    @property
    def code(self):
        """
        Gets the code of this ErrorResponse.
        HTTP response code.

        :return: The code of this ErrorResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorResponse.
        HTTP response code.

        :param code: The code of this ErrorResponse.
        :type: int
        """

        self._code = code

    @property
    def fields(self):
        """
        Gets the fields of this ErrorResponse.
        Details of the error fields.

        :return: The fields of this ErrorResponse.
        :rtype: list[Fields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this ErrorResponse.
        Details of the error fields.

        :param fields: The fields of this ErrorResponse.
        :type: list[Fields]
        """

        self._fields = fields

    @property
    def message(self):
        """
        Gets the message of this ErrorResponse.
        Description of the error.

        :return: The message of this ErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorResponse.
        Description of the error.

        :param message: The message of this ErrorResponse.
        :type: str
        """

        self._message = message

    @property
    def object(self):
        """
        Gets the object of this ErrorResponse.
        Response type, always \"error\".

        :return: The object of this ErrorResponse.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this ErrorResponse.
        Response type, always \"error\".

        :param object: The object of this ErrorResponse.
        :type: str
        """

        self._object = object

    @property
    def request_id(self):
        """
        Gets the request_id of this ErrorResponse.
        Request ID.

        :return: The request_id of this ErrorResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this ErrorResponse.
        Request ID.

        :param request_id: The request_id of this ErrorResponse.
        :type: str
        """

        self._request_id = request_id

    @property
    def type(self):
        """
        Gets the type of this ErrorResponse.
        Type of error.

        :return: The type of this ErrorResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ErrorResponse.
        Type of error.

        :param type: The type of this ErrorResponse.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, ErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
