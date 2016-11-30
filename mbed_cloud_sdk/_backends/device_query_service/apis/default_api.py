# coding: utf-8

"""
    Device Query Service API

    This is the API Documentation for the mbed device query service update service.

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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def device_query_create(self, name, query, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Create device query</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_create(name, query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The name of the query (required)
        :param str query: The device query (required)
        :param str description: The description of the object
        :param str object: The API resource entity
        :param str query_id: DEPRECATED: The ID of the query
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_create_with_http_info(name, query, **kwargs)
        else:
            (data) = self.device_query_create_with_http_info(name, query, **kwargs)
            return data

    def device_query_create_with_http_info(self, name, query, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Create device query</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_create_with_http_info(name, query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The name of the query (required)
        :param str query: The device query (required)
        :param str description: The description of the object
        :param str object: The API resource entity
        :param str query_id: DEPRECATED: The ID of the query
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'query', 'description', 'object', 'query_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `device_query_create`")
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `device_query_create`")

        resource_path = '/v3/device-queries{var}'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'object' in params:
            form_params.append(('object', params['object']))
        if 'query' in params:
            form_params.append(('query', params['query']))
        if 'query_id' in params:
            form_params.append(('query_id', params['query_id']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceQuerySerializer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def device_query_destroy(self, query_id, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Delete device query</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_destroy(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_destroy_with_http_info(query_id, **kwargs)
        else:
            (data) = self.device_query_destroy_with_http_info(query_id, **kwargs)
            return data

    def device_query_destroy_with_http_info(self, query_id, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Delete device query</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_destroy_with_http_info(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_destroy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_destroy`")

        resource_path = '/v3/device-queries/{query_id}{var}'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceQuerySerializer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def device_query_list(self, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>List all device queries. The result will be paged into pages of 100.</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str description: 
        :param str created_at: 
        :param str updated_at: 
        :param str etag: 
        :param str name: 
        :param str object: 
        :param str query: 
        :param str query_id: 
        :return: list[DeviceQuerySerializer]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_list_with_http_info(**kwargs)
        else:
            (data) = self.device_query_list_with_http_info(**kwargs)
            return data

    def device_query_list_with_http_info(self, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>List all device queries. The result will be paged into pages of 100.</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str description: 
        :param str created_at: 
        :param str updated_at: 
        :param str etag: 
        :param str name: 
        :param str object: 
        :param str query: 
        :param str query_id: 
        :return: list[DeviceQuerySerializer]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['description', 'created_at', 'updated_at', 'etag', 'name', 'object', 'query', 'query_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_list" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v3/device-queries{var}'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'description' in params:
            query_params['description'] = params['description']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'etag' in params:
            query_params['etag'] = params['etag']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'object' in params:
            query_params['object'] = params['object']
        if 'query' in params:
            query_params['query'] = params['query']
        if 'query_id' in params:
            query_params['query_id'] = params['query_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DeviceQuerySerializer]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def device_query_partial_update(self, query_id, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Update device query fields</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_partial_update(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :param str description: The description of the object
        :param str name: The name of the query
        :param str object: The API resource entity
        :param str query: The device query
        :param str query_id2: DEPRECATED: The ID of the query
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_partial_update_with_http_info(query_id, **kwargs)
        else:
            (data) = self.device_query_partial_update_with_http_info(query_id, **kwargs)
            return data

    def device_query_partial_update_with_http_info(self, query_id, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Update device query fields</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_partial_update_with_http_info(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :param str description: The description of the object
        :param str name: The name of the query
        :param str object: The API resource entity
        :param str query: The device query
        :param str query_id2: DEPRECATED: The ID of the query
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'description', 'name', 'object', 'query', 'query_id2']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_partial_update`")

        resource_path = '/v3/device-queries/{query_id}{var}'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'object' in params:
            form_params.append(('object', params['object']))
        if 'query' in params:
            form_params.append(('query', params['query']))
        if 'query_id2' in params:
            form_params.append(('query_id', params['query_id2']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceQuerySerializer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def device_query_retrieve(self, query_id, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Retrieve device query.</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_retrieve(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_retrieve_with_http_info(query_id, **kwargs)
        else:
            (data) = self.device_query_retrieve_with_http_info(query_id, **kwargs)
            return data

    def device_query_retrieve_with_http_info(self, query_id, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Retrieve device query.</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_retrieve_with_http_info(query_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_retrieve`")

        resource_path = '/v3/device-queries/{query_id}{var}'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceQuerySerializer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def device_query_update(self, query_id, name, query, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Update device query.</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_update(query_id, name, query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :param str name: The name of the query (required)
        :param str query: The device query (required)
        :param str description: The description of the object
        :param str object: The API resource entity
        :param str query_id2: DEPRECATED: The ID of the query
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.device_query_update_with_http_info(query_id, name, query, **kwargs)
        else:
            (data) = self.device_query_update_with_http_info(query_id, name, query, **kwargs)
            return data

    def device_query_update_with_http_info(self, query_id, name, query, **kwargs):
        """
        
        <p>The APIs for creating and manipulating device queries.  </p> <p>Update device query.</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.device_query_update_with_http_info(query_id, name, query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query_id:  (required)
        :param str name: The name of the query (required)
        :param str query: The device query (required)
        :param str description: The description of the object
        :param str object: The API resource entity
        :param str query_id2: DEPRECATED: The ID of the query
        :return: DeviceQuerySerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'name', 'query', 'description', 'object', 'query_id2']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_query_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params) or (params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `device_query_update`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `device_query_update`")
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `device_query_update`")

        resource_path = '/v3/device-queries/{query_id}{var}'.replace('{format}', 'json')
        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'object' in params:
            form_params.append(('object', params['object']))
        if 'query' in params:
            form_params.append(('query', params['query']))
        if 'query_id2' in params:
            form_params.append(('query_id', params['query_id2']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceQuerySerializer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
