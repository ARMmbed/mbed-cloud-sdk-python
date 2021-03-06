# coding: utf-8

"""
    Connect CA API

    Connect CA API allows services to get device credentials.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeveloperCertificateResponseData(object):
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
        'account_id': 'str',
        'created_at': 'datetime',
        'description': 'str',
        'developer_certificate': 'str',
        'developer_private_key': 'str',
        'etag': 'str',
        'id': 'str',
        'name': 'str',
        'object': 'str',
        'security_file_content': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'created_at': 'created_at',
        'description': 'description',
        'developer_certificate': 'developer_certificate',
        'developer_private_key': 'developer_private_key',
        'etag': 'etag',
        'id': 'id',
        'name': 'name',
        'object': 'object',
        'security_file_content': 'security_file_content'
    }

    def __init__(self, account_id=None, created_at=None, description=None, developer_certificate=None, developer_private_key=None, etag=None, id=None, name=None, object=None, security_file_content=None):
        """
        DeveloperCertificateResponseData - a model defined in Swagger
        """

        self._account_id = account_id
        self._created_at = created_at
        self._description = description
        self._developer_certificate = developer_certificate
        self._developer_private_key = developer_private_key
        self._etag = etag
        self._id = id
        self._name = name
        self._object = object
        self._security_file_content = security_file_content
        self.discriminator = None

    @property
    def account_id(self):
        """
        Gets the account_id of this DeveloperCertificateResponseData.
        account to which the developer certificate belongs

        :return: The account_id of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this DeveloperCertificateResponseData.
        account to which the developer certificate belongs

        :param account_id: The account_id of this DeveloperCertificateResponseData.
        :type: str
        """

        self._account_id = account_id

    @property
    def created_at(self):
        """
        Gets the created_at of this DeveloperCertificateResponseData.
        Creation UTC time RFC3339.

        :return: The created_at of this DeveloperCertificateResponseData.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DeveloperCertificateResponseData.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this DeveloperCertificateResponseData.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """
        Gets the description of this DeveloperCertificateResponseData.
        Description for the developer certificate.

        :return: The description of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeveloperCertificateResponseData.
        Description for the developer certificate.

        :param description: The description of this DeveloperCertificateResponseData.
        :type: str
        """

        self._description = description

    @property
    def developer_certificate(self):
        """
        Gets the developer_certificate of this DeveloperCertificateResponseData.
        PEM format X.509 developer certificate.

        :return: The developer_certificate of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._developer_certificate

    @developer_certificate.setter
    def developer_certificate(self, developer_certificate):
        """
        Sets the developer_certificate of this DeveloperCertificateResponseData.
        PEM format X.509 developer certificate.

        :param developer_certificate: The developer_certificate of this DeveloperCertificateResponseData.
        :type: str
        """

        self._developer_certificate = developer_certificate

    @property
    def developer_private_key(self):
        """
        Gets the developer_private_key of this DeveloperCertificateResponseData.
        PEM format developer private key associated to the certificate.

        :return: The developer_private_key of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._developer_private_key

    @developer_private_key.setter
    def developer_private_key(self, developer_private_key):
        """
        Sets the developer_private_key of this DeveloperCertificateResponseData.
        PEM format developer private key associated to the certificate.

        :param developer_private_key: The developer_private_key of this DeveloperCertificateResponseData.
        :type: str
        """

        self._developer_private_key = developer_private_key

    @property
    def etag(self):
        """
        Gets the etag of this DeveloperCertificateResponseData.
        API resource entity version.

        :return: The etag of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this DeveloperCertificateResponseData.
        API resource entity version.

        :param etag: The etag of this DeveloperCertificateResponseData.
        :type: str
        """

        self._etag = etag

    @property
    def id(self):
        """
        Gets the id of this DeveloperCertificateResponseData.
        mUUID that uniquely identifies the developer certificate.

        :return: The id of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeveloperCertificateResponseData.
        mUUID that uniquely identifies the developer certificate.

        :param id: The id of this DeveloperCertificateResponseData.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DeveloperCertificateResponseData.
        Name of the developer certificate.

        :return: The name of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeveloperCertificateResponseData.
        Name of the developer certificate.

        :param name: The name of this DeveloperCertificateResponseData.
        :type: str
        """

        self._name = name

    @property
    def object(self):
        """
        Gets the object of this DeveloperCertificateResponseData.
        Entity name, always 'trusted-cert'

        :return: The object of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeveloperCertificateResponseData.
        Entity name, always 'trusted-cert'

        :param object: The object of this DeveloperCertificateResponseData.
        :type: str
        """

        self._object = object

    @property
    def security_file_content(self):
        """
        Gets the security_file_content of this DeveloperCertificateResponseData.
        Content of the security.c file that will be flashed into the device to provide the security credentials

        :return: The security_file_content of this DeveloperCertificateResponseData.
        :rtype: str
        """
        return self._security_file_content

    @security_file_content.setter
    def security_file_content(self, security_file_content):
        """
        Sets the security_file_content of this DeveloperCertificateResponseData.
        Content of the security.c file that will be flashed into the device to provide the security credentials

        :param security_file_content: The security_file_content of this DeveloperCertificateResponseData.
        :type: str
        """

        self._security_file_content = security_file_content

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
        if not isinstance(other, DeveloperCertificateResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
