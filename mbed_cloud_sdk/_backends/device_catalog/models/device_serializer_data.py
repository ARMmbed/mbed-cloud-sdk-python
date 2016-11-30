# coding: utf-8

"""
    Device Catalog API

    This is the API Documentation for the mbed device catalog update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class DeviceSerializerData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bootstrapped_timestamp=None, updated_at=None, custom_attributes=None, device_class=None, id=None, description=None, auto_update=None, mechanism=None, state=None, etag=None, provision_key=None, serial_number=None, vendor_id=None, account_id=None, deployed_state=None, object=None, trust_class=None, deployment=None, mechanism_url=None, trust_level=None, device_id=None, name=None, created_at=None, manifest=None):
        """
        DeviceSerializerData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bootstrapped_timestamp': 'str',
            'updated_at': 'datetime',
            'custom_attributes': 'str',
            'device_class': 'str',
            'id': 'str',
            'description': 'str',
            'auto_update': 'bool',
            'mechanism': 'str',
            'state': 'str',
            'etag': 'datetime',
            'provision_key': 'str',
            'serial_number': 'str',
            'vendor_id': 'str',
            'account_id': 'str',
            'deployed_state': 'str',
            'object': 'str',
            'trust_class': 'int',
            'deployment': 'str',
            'mechanism_url': 'str',
            'trust_level': 'int',
            'device_id': 'str',
            'name': 'str',
            'created_at': 'datetime',
            'manifest': 'str'
        }

        self.attribute_map = {
            'bootstrapped_timestamp': 'bootstrapped_timestamp',
            'updated_at': 'updated_at',
            'custom_attributes': 'custom_attributes',
            'device_class': 'device_class',
            'id': 'id',
            'description': 'description',
            'auto_update': 'auto_update',
            'mechanism': 'mechanism',
            'state': 'state',
            'etag': 'etag',
            'provision_key': 'provision_key',
            'serial_number': 'serial_number',
            'vendor_id': 'vendor_id',
            'account_id': 'account_id',
            'deployed_state': 'deployed_state',
            'object': 'object',
            'trust_class': 'trust_class',
            'deployment': 'deployment',
            'mechanism_url': 'mechanism_url',
            'trust_level': 'trust_level',
            'device_id': 'device_id',
            'name': 'name',
            'created_at': 'created_at',
            'manifest': 'manifest'
        }

        self._bootstrapped_timestamp = bootstrapped_timestamp
        self._updated_at = updated_at
        self._custom_attributes = custom_attributes
        self._device_class = device_class
        self._id = id
        self._description = description
        self._auto_update = auto_update
        self._mechanism = mechanism
        self._state = state
        self._etag = etag
        self._provision_key = provision_key
        self._serial_number = serial_number
        self._vendor_id = vendor_id
        self._account_id = account_id
        self._deployed_state = deployed_state
        self._object = object
        self._trust_class = trust_class
        self._deployment = deployment
        self._mechanism_url = mechanism_url
        self._trust_level = trust_level
        self._device_id = device_id
        self._name = name
        self._created_at = created_at
        self._manifest = manifest

    @property
    def bootstrapped_timestamp(self):
        """
        Gets the bootstrapped_timestamp of this DeviceSerializerData.


        :return: The bootstrapped_timestamp of this DeviceSerializerData.
        :rtype: str
        """
        return self._bootstrapped_timestamp

    @bootstrapped_timestamp.setter
    def bootstrapped_timestamp(self, bootstrapped_timestamp):
        """
        Sets the bootstrapped_timestamp of this DeviceSerializerData.


        :param bootstrapped_timestamp: The bootstrapped_timestamp of this DeviceSerializerData.
        :type: str
        """

        self._bootstrapped_timestamp = bootstrapped_timestamp

    @property
    def updated_at(self):
        """
        Gets the updated_at of this DeviceSerializerData.
        The time the object was updated

        :return: The updated_at of this DeviceSerializerData.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this DeviceSerializerData.
        The time the object was updated

        :param updated_at: The updated_at of this DeviceSerializerData.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceSerializerData.
        Up to 5 custom JSON attributes

        :return: The custom_attributes of this DeviceSerializerData.
        :rtype: str
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceSerializerData.
        Up to 5 custom JSON attributes

        :param custom_attributes: The custom_attributes of this DeviceSerializerData.
        :type: str
        """

        self._custom_attributes = custom_attributes

    @property
    def device_class(self):
        """
        Gets the device_class of this DeviceSerializerData.
        The device class

        :return: The device_class of this DeviceSerializerData.
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """
        Sets the device_class of this DeviceSerializerData.
        The device class

        :param device_class: The device_class of this DeviceSerializerData.
        :type: str
        """

        self._device_class = device_class

    @property
    def id(self):
        """
        Gets the id of this DeviceSerializerData.
        The ID of the device

        :return: The id of this DeviceSerializerData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceSerializerData.
        The ID of the device

        :param id: The id of this DeviceSerializerData.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this DeviceSerializerData.
        The description of the object

        :return: The description of this DeviceSerializerData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceSerializerData.
        The description of the object

        :param description: The description of this DeviceSerializerData.
        :type: str
        """

        self._description = description

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceSerializerData.
        Mark this device for auto firmware update

        :return: The auto_update of this DeviceSerializerData.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceSerializerData.
        Mark this device for auto firmware update

        :param auto_update: The auto_update of this DeviceSerializerData.
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def mechanism(self):
        """
        Gets the mechanism of this DeviceSerializerData.
        The ID of the channel used to communicate with the device

        :return: The mechanism of this DeviceSerializerData.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this DeviceSerializerData.
        The ID of the channel used to communicate with the device

        :param mechanism: The mechanism of this DeviceSerializerData.
        :type: str
        """
        allowed_values = ["connector", "direct"]
        if mechanism not in allowed_values:
            raise ValueError(
                "Invalid value for `mechanism` ({0}), must be one of {1}"
                .format(mechanism, allowed_values)
            )

        self._mechanism = mechanism

    @property
    def state(self):
        """
        Gets the state of this DeviceSerializerData.
        The current state of the device

        :return: The state of this DeviceSerializerData.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DeviceSerializerData.
        The current state of the device

        :param state: The state of this DeviceSerializerData.
        :type: str
        """
        allowed_values = ["unenrolled", "cloud_enrolling", "bootstrapped", "registered"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def etag(self):
        """
        Gets the etag of this DeviceSerializerData.
        The entity instance signature

        :return: The etag of this DeviceSerializerData.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this DeviceSerializerData.
        The entity instance signature

        :param etag: The etag of this DeviceSerializerData.
        :type: datetime
        """

        self._etag = etag

    @property
    def provision_key(self):
        """
        Gets the provision_key of this DeviceSerializerData.
        The key used to provision the device

        :return: The provision_key of this DeviceSerializerData.
        :rtype: str
        """
        return self._provision_key

    @provision_key.setter
    def provision_key(self, provision_key):
        """
        Sets the provision_key of this DeviceSerializerData.
        The key used to provision the device

        :param provision_key: The provision_key of this DeviceSerializerData.
        :type: str
        """

        self._provision_key = provision_key

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DeviceSerializerData.
        The serial number of the device

        :return: The serial_number of this DeviceSerializerData.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DeviceSerializerData.
        The serial number of the device

        :param serial_number: The serial_number of this DeviceSerializerData.
        :type: str
        """

        self._serial_number = serial_number

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this DeviceSerializerData.
        The device vendor ID

        :return: The vendor_id of this DeviceSerializerData.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this DeviceSerializerData.
        The device vendor ID

        :param vendor_id: The vendor_id of this DeviceSerializerData.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def account_id(self):
        """
        Gets the account_id of this DeviceSerializerData.
        The owning IAM account ID

        :return: The account_id of this DeviceSerializerData.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this DeviceSerializerData.
        The owning IAM account ID

        :param account_id: The account_id of this DeviceSerializerData.
        :type: str
        """

        self._account_id = account_id

    @property
    def deployed_state(self):
        """
        Gets the deployed_state of this DeviceSerializerData.
        The state of the device's deployment

        :return: The deployed_state of this DeviceSerializerData.
        :rtype: str
        """
        return self._deployed_state

    @deployed_state.setter
    def deployed_state(self, deployed_state):
        """
        Sets the deployed_state of this DeviceSerializerData.
        The state of the device's deployment

        :param deployed_state: The deployed_state of this DeviceSerializerData.
        :type: str
        """
        allowed_values = ["development", "production"]
        if deployed_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployed_state` ({0}), must be one of {1}"
                .format(deployed_state, allowed_values)
            )

        self._deployed_state = deployed_state

    @property
    def object(self):
        """
        Gets the object of this DeviceSerializerData.
        The API resource entity

        :return: The object of this DeviceSerializerData.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceSerializerData.
        The API resource entity

        :param object: The object of this DeviceSerializerData.
        :type: str
        """

        self._object = object

    @property
    def trust_class(self):
        """
        Gets the trust_class of this DeviceSerializerData.
        The device trust class

        :return: The trust_class of this DeviceSerializerData.
        :rtype: int
        """
        return self._trust_class

    @trust_class.setter
    def trust_class(self, trust_class):
        """
        Sets the trust_class of this DeviceSerializerData.
        The device trust class

        :param trust_class: The trust_class of this DeviceSerializerData.
        :type: int
        """

        if not trust_class:
            raise ValueError("Invalid value for `trust_class`, must not be `None`")
        if trust_class > 2.147483647E9:
            raise ValueError("Invalid value for `trust_class`, must be a value less than or equal to `2.147483647E9`")
        if trust_class < -2.147483648E9:
            raise ValueError("Invalid value for `trust_class`, must be a value greater than or equal to `-2.147483648E9`")

        self._trust_class = trust_class

    @property
    def deployment(self):
        """
        Gets the deployment of this DeviceSerializerData.
        The last deployment used on the device

        :return: The deployment of this DeviceSerializerData.
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this DeviceSerializerData.
        The last deployment used on the device

        :param deployment: The deployment of this DeviceSerializerData.
        :type: str
        """

        self._deployment = deployment

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this DeviceSerializerData.
        The address of the connector to use

        :return: The mechanism_url of this DeviceSerializerData.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this DeviceSerializerData.
        The address of the connector to use

        :param mechanism_url: The mechanism_url of this DeviceSerializerData.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def trust_level(self):
        """
        Gets the trust_level of this DeviceSerializerData.
        The device trust level

        :return: The trust_level of this DeviceSerializerData.
        :rtype: int
        """
        return self._trust_level

    @trust_level.setter
    def trust_level(self, trust_level):
        """
        Sets the trust_level of this DeviceSerializerData.
        The device trust level

        :param trust_level: The trust_level of this DeviceSerializerData.
        :type: int
        """

        if not trust_level:
            raise ValueError("Invalid value for `trust_level`, must not be `None`")
        if trust_level > 2.147483647E9:
            raise ValueError("Invalid value for `trust_level`, must be a value less than or equal to `2.147483647E9`")
        if trust_level < -2.147483648E9:
            raise ValueError("Invalid value for `trust_level`, must be a value greater than or equal to `-2.147483648E9`")

        self._trust_level = trust_level

    @property
    def device_id(self):
        """
        Gets the device_id of this DeviceSerializerData.
        DEPRECATED: The ID of the device

        :return: The device_id of this DeviceSerializerData.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this DeviceSerializerData.
        DEPRECATED: The ID of the device

        :param device_id: The device_id of this DeviceSerializerData.
        :type: str
        """

        self._device_id = device_id

    @property
    def name(self):
        """
        Gets the name of this DeviceSerializerData.
        The name of the object

        :return: The name of this DeviceSerializerData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceSerializerData.
        The name of the object

        :param name: The name of this DeviceSerializerData.
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this DeviceSerializerData.
        The time the object was created

        :return: The created_at of this DeviceSerializerData.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DeviceSerializerData.
        The time the object was created

        :param created_at: The created_at of this DeviceSerializerData.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def manifest(self):
        """
        Gets the manifest of this DeviceSerializerData.
        URL for the current device manifest

        :return: The manifest of this DeviceSerializerData.
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this DeviceSerializerData.
        URL for the current device manifest

        :param manifest: The manifest of this DeviceSerializerData.
        :type: str
        """

        self._manifest = manifest

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
