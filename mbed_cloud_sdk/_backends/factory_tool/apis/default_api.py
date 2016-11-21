# coding: utf-8

"""
    Provisioning endpoints - the factory provisioning package.

    The factory provisioning package needs to be installed in factories to enroll devices onto the mbed Cloud ecosystem.  These APIs allow downloading the most recent version of the factory provisioning package for various operating systems. 

    OpenAPI spec version: 0.8
    
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

    def downloads_mbed_factory_provisioning_package_info_get(self, authorization, **kwargs):
        """
        
        Gets a list of downloadable Factory Tool versions. * mbed Cloud user role must be Administrator. * mbed Cloud account must have Factory Tool downloads enabled. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloads_mbed_factory_provisioning_package_info_get(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by a reference token (API key forbidden). (required)
        :return: AListOfDownloadableFactoryToolVersions_
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.downloads_mbed_factory_provisioning_package_info_get_with_http_info(authorization, **kwargs)
        else:
            (data) = self.downloads_mbed_factory_provisioning_package_info_get_with_http_info(authorization, **kwargs)
            return data

    def downloads_mbed_factory_provisioning_package_info_get_with_http_info(self, authorization, **kwargs):
        """
        
        Gets a list of downloadable Factory Tool versions. * mbed Cloud user role must be Administrator. * mbed Cloud account must have Factory Tool downloads enabled. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloads_mbed_factory_provisioning_package_info_get_with_http_info(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by a reference token (API key forbidden). (required)
        :return: AListOfDownloadableFactoryToolVersions_
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method downloads_mbed_factory_provisioning_package_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `downloads_mbed_factory_provisioning_package_info_get`")

        resource_path = '/downloads/mbed_factory_provisioning_package/info'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

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
                                            response_type='AListOfDownloadableFactoryToolVersions_',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def downloads_mbed_factory_provisioning_packageosos_get(self, authorization, os, **kwargs):
        """
        
        Returns a specific Factory Tool package in a ZIP archive. * mbed Cloud user role must be Administrator. * mbed Cloud account must have Factory Tool downloads enabled. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloads_mbed_factory_provisioning_packageosos_get(authorization, os, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by a reference token (API key forbidden). (required)
        :param str os: Requires Factory Tool OS name (Windows or Linux). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.downloads_mbed_factory_provisioning_packageosos_get_with_http_info(authorization, os, **kwargs)
        else:
            (data) = self.downloads_mbed_factory_provisioning_packageosos_get_with_http_info(authorization, os, **kwargs)
            return data

    def downloads_mbed_factory_provisioning_packageosos_get_with_http_info(self, authorization, os, **kwargs):
        """
        
        Returns a specific Factory Tool package in a ZIP archive. * mbed Cloud user role must be Administrator. * mbed Cloud account must have Factory Tool downloads enabled. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloads_mbed_factory_provisioning_packageosos_get_with_http_info(authorization, os, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by a reference token (API key forbidden). (required)
        :param str os: Requires Factory Tool OS name (Windows or Linux). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'os']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method downloads_mbed_factory_provisioning_packageosos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `downloads_mbed_factory_provisioning_packageosos_get`")
        # verify the required parameter 'os' is set
        if ('os' not in params) or (params['os'] is None):
            raise ValueError("Missing the required parameter `os` when calling `downloads_mbed_factory_provisioning_packageosos_get`")

        resource_path = '/downloads/mbed_factory_provisioning_package?os&#x3D;{os}'.replace('{format}', 'json')
        path_params = {}
        if 'os' in params:
            path_params['os'] = params['os']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
