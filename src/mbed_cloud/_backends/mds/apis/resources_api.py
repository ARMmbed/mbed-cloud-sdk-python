# coding: utf-8

"""
    Connect API

    Pelion Device Management Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. Device Management Connect allows connectivity to devices by queueing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class ResourcesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_resource_path(self, device_id, _resource_path, **kwargs):  # noqa: E501
        """Delete a resource path  # noqa: E501

        A request to delete a resource path must be handled by both Device Management Client and Device Management Connect.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  **Example usage:**      curl -X DELETE \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.delete_resource_path(device_id, _resource_path, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool no_resp: If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.delete_resource_path_with_http_info(device_id, _resource_path, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_resource_path_with_http_info(device_id, _resource_path, **kwargs)  # noqa: E501
            return data

    def delete_resource_path_with_http_info(self, device_id, _resource_path, **kwargs):  # noqa: E501
        """Delete a resource path  # noqa: E501

        A request to delete a resource path must be handled by both Device Management Client and Device Management Connect.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  **Example usage:**      curl -X DELETE \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.delete_resource_path_with_http_info(device_id, _resource_path, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool no_resp: If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'no_resp']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_resource_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `delete_resource_path`")  # noqa: E501
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params or
                params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `delete_resource_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']  # noqa: E501
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']  # noqa: E501

        query_params = []
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/endpoints/{device-id}/{resourcePath}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncID',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def execute_or_create_resource(self, device_id, _resource_path, **kwargs):  # noqa: E501
        """Execute a function on a Resource or create new Object instance  # noqa: E501

        With this API, you can [execute a function](/docs/current/connecting/handle-resource-webapp.html#the-execute-operation) on an existing resource and create new Object instance to the device. The resource-path does not have to exist - it can be created by the call. The maximum length of resource-path is 255 characters.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  Supported content types depend on the device and its resource. Device Management translates HTTP to equivalent CoAP content type.  **Example usage:**  This example resets the min and max values of the [temperature sensor](http://www.openmobilealliance.org/tech/profiles/lwm2m/3303.xml) instance 0 by executing the Resource 5605 'Reset Min and Max Measured Values'.      curl -X POST \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3303/0/5605 \\       -H 'authorization: Bearer {api-key}'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.execute_or_create_resource(device_id, _resource_path, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource. (required)
        :param str resource_function: This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in Device Management Client. 
        :param bool no_resp: If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.execute_or_create_resource_with_http_info(device_id, _resource_path, **kwargs)  # noqa: E501
        else:
            (data) = self.execute_or_create_resource_with_http_info(device_id, _resource_path, **kwargs)  # noqa: E501
            return data

    def execute_or_create_resource_with_http_info(self, device_id, _resource_path, **kwargs):  # noqa: E501
        """Execute a function on a Resource or create new Object instance  # noqa: E501

        With this API, you can [execute a function](/docs/current/connecting/handle-resource-webapp.html#the-execute-operation) on an existing resource and create new Object instance to the device. The resource-path does not have to exist - it can be created by the call. The maximum length of resource-path is 255 characters.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  Supported content types depend on the device and its resource. Device Management translates HTTP to equivalent CoAP content type.  **Example usage:**  This example resets the min and max values of the [temperature sensor](http://www.openmobilealliance.org/tech/profiles/lwm2m/3303.xml) instance 0 by executing the Resource 5605 'Reset Min and Max Measured Values'.      curl -X POST \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3303/0/5605 \\       -H 'authorization: Bearer {api-key}'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.execute_or_create_resource_with_http_info(device_id, _resource_path, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource. (required)
        :param str resource_function: This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in Device Management Client. 
        :param bool no_resp: If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'resource_function', 'no_resp']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute_or_create_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `execute_or_create_resource`")  # noqa: E501
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params or
                params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `execute_or_create_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']  # noqa: E501
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']  # noqa: E501

        query_params = []
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resource_function' in params:
            body_params = params['resource_function']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain', 'application/xml', 'application/octet-stream', 'application/exi', 'application/json', 'application/link-format', 'application/senml+json', 'application/nanoservice-tlv', 'application/vnd.oma.lwm2m+text', 'application/vnd.oma.lwm2m+opaq', 'application/vnd.oma.lwm2m+tlv', 'application/vnd.oma.lwm2m+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/endpoints/{device-id}/{resourcePath}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncID',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resource_value(self, device_id, _resource_path, **kwargs):  # noqa: E501
        """Read from a resource  # noqa: E501

        Requests the resource value and when the response is available, an `AsyncIDResponse` json object is received in the notification channel. The preferred way to get resource values is to use the **subscribe** and **callback** methods.  All resource APIs are asynchronous. These APIs only respond if the device is turned on and connected to Device Management.   See also how [resource caching](/docs/current/connecting/device-guidelines.html#resource-cache) works.  Please refer to [Lightweight Machine to Machine Technical specification](http://www.openmobilealliance.org/release/LightweightM2M/V1_0-20170208-A/OMA-TS-LightweightM2M-V1_0-20170208-A.pdf) for more inforamtion.  **Example usage:**      curl -X GET \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_resource_value(device_id, _resource_path, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: Unique Device Management device ID for the endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool cache_only: If true, the response comes only from the cache. Default: false. Device Management Connect caches the received resource values for the time of [max_age](/docs/current/connecting/working-with-the-resources.html) defined in the client side. 
        :param bool no_resp: If a request is made with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_resource_value_with_http_info(device_id, _resource_path, **kwargs)  # noqa: E501
        else:
            (data) = self.get_resource_value_with_http_info(device_id, _resource_path, **kwargs)  # noqa: E501
            return data

    def get_resource_value_with_http_info(self, device_id, _resource_path, **kwargs):  # noqa: E501
        """Read from a resource  # noqa: E501

        Requests the resource value and when the response is available, an `AsyncIDResponse` json object is received in the notification channel. The preferred way to get resource values is to use the **subscribe** and **callback** methods.  All resource APIs are asynchronous. These APIs only respond if the device is turned on and connected to Device Management.   See also how [resource caching](/docs/current/connecting/device-guidelines.html#resource-cache) works.  Please refer to [Lightweight Machine to Machine Technical specification](http://www.openmobilealliance.org/release/LightweightM2M/V1_0-20170208-A/OMA-TS-LightweightM2M-V1_0-20170208-A.pdf) for more inforamtion.  **Example usage:**      curl -X GET \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_resource_value_with_http_info(device_id, _resource_path, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: Unique Device Management device ID for the endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool cache_only: If true, the response comes only from the cache. Default: false. Device Management Connect caches the received resource values for the time of [max_age](/docs/current/connecting/working-with-the-resources.html) defined in the client side. 
        :param bool no_resp: If a request is made with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'cache_only', 'no_resp']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_value" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_resource_value`")  # noqa: E501
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params or
                params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `get_resource_value`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']  # noqa: E501
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']  # noqa: E501

        query_params = []
        if 'cache_only' in params:
            query_params.append(('cacheOnly', params['cache_only']))  # noqa: E501
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/endpoints/{device-id}/{resourcePath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_resource_value(self, device_id, _resource_path, resource_value, **kwargs):  # noqa: E501
        """Write to a resource or use write-attributes for a resource  # noqa: E501

        With this API, you can [write a new value to existing resources](/docs/current/connecting/handle-resource-webapp.html) or [use the write-attributes](/docs/current/connecting/resource-change-webapp.html) for a resource.  This API can also be used to transfer files to the device. Device Management Connect LwM2M server implements the Option 1 from RFC7959. The maximum block size is 1024 bytes. The block size versus transferred file size is something to note in low quality networks. The customer application needs to know what type of file is transferred (for example txt) and the payload can be encrypted by the customer. The maximum size of payload is 1048576 bytes.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  Supported content types depend on the device and its resource. Device Management translates HTTP to equivalent CoAP content type.  **Example usage:**  This example sets the alarm on a buzzer. The command writes the [Buzzer](http://www.openmobilealliance.org/tech/profiles/lwm2m/3338.xml) instance 0, \"On/Off\" boolean resource to '1'.      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3338/0/5850 -H \"content-type: text/plain\" \\       -H 'authorization: Bearer {api-key}' -d '1'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.update_resource_value(device_id, _resource_path, resource_value, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource URL. (required)
        :param str resource_value: The value to be set to the resource.  (required)
        :param bool no_resp: If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.update_resource_value_with_http_info(device_id, _resource_path, resource_value, **kwargs)  # noqa: E501
        else:
            (data) = self.update_resource_value_with_http_info(device_id, _resource_path, resource_value, **kwargs)  # noqa: E501
            return data

    def update_resource_value_with_http_info(self, device_id, _resource_path, resource_value, **kwargs):  # noqa: E501
        """Write to a resource or use write-attributes for a resource  # noqa: E501

        With this API, you can [write a new value to existing resources](/docs/current/connecting/handle-resource-webapp.html) or [use the write-attributes](/docs/current/connecting/resource-change-webapp.html) for a resource.  This API can also be used to transfer files to the device. Device Management Connect LwM2M server implements the Option 1 from RFC7959. The maximum block size is 1024 bytes. The block size versus transferred file size is something to note in low quality networks. The customer application needs to know what type of file is transferred (for example txt) and the payload can be encrypted by the customer. The maximum size of payload is 1048576 bytes.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Device Management Connect and there is an active notification channel.  Supported content types depend on the device and its resource. Device Management translates HTTP to equivalent CoAP content type.  **Example usage:**  This example sets the alarm on a buzzer. The command writes the [Buzzer](http://www.openmobilealliance.org/tech/profiles/lwm2m/3338.xml) instance 0, \"On/Off\" boolean resource to '1'.      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3338/0/5850 -H \"content-type: text/plain\" \\       -H 'authorization: Bearer {api-key}' -d '1'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.update_resource_value_with_http_info(device_id, _resource_path, resource_value, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str device_id: A unique Device Management device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource URL. (required)
        :param str resource_value: The value to be set to the resource.  (required)
        :param bool no_resp: If you make a request with `noResp=true`, Device Management Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'resource_value', 'no_resp']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_resource_value" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `update_resource_value`")  # noqa: E501
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params or
                params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `update_resource_value`")  # noqa: E501
        # verify the required parameter 'resource_value' is set
        if ('resource_value' not in params or
                params['resource_value'] is None):
            raise ValueError("Missing the required parameter `resource_value` when calling `update_resource_value`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']  # noqa: E501
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']  # noqa: E501

        query_params = []
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resource_value' in params:
            body_params = params['resource_value']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain', 'application/xml', 'application/octet-stream', 'application/exi', 'application/json', 'application/link-format', 'application/senml+json', 'application/nanoservice-tlv', 'application/vnd.oma.lwm2m+text', 'application/vnd.oma.lwm2m+opaq', 'application/vnd.oma.lwm2m+tlv', 'application/vnd.oma.lwm2m+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/endpoints/{device-id}/{resourcePath}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncID',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
