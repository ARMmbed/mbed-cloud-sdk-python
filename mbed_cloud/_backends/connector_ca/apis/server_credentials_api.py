# coding: utf-8

"""
    Connect CA API

    Connect CA API provides methods to create and get Developer certificate. Also Connect CA provides server-credentials for Bootstarp and LWM2M Server.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ServerCredentialsApi(object):
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

    def v3_server_credentials_bootstrap_get(self, authorization, **kwargs):
        """
        Fetch bootstrap server credentials.
        This REST API is intended to be used by customers to fetch bootstrap server credentials that they need to use with their clients to connect to bootstrap server. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_server_credentials_bootstrap_get(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_server_credentials_bootstrap_get_with_http_info(authorization, **kwargs)
        else:
            (data) = self.v3_server_credentials_bootstrap_get_with_http_info(authorization, **kwargs)
            return data

    def v3_server_credentials_bootstrap_get_with_http_info(self, authorization, **kwargs):
        """
        Fetch bootstrap server credentials.
        This REST API is intended to be used by customers to fetch bootstrap server credentials that they need to use with their clients to connect to bootstrap server. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_server_credentials_bootstrap_get_with_http_info(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_server_credentials_bootstrap_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_server_credentials_bootstrap_get`")


        collection_formats = {}

        resource_path = '/v3/server-credentials/bootstrap'.replace('{format}', 'json')
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
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ServerCredentialsResponseData',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def v3_server_credentials_lwm2m_get(self, authorization, **kwargs):
        """
        Fetch LWM2M server credentials.
        This REST API is intended to be used by customers to fetch LWM2M server credentials that they need to use with their clients to connect to LWM2M server. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_server_credentials_lwm2m_get(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_server_credentials_lwm2m_get_with_http_info(authorization, **kwargs)
        else:
            (data) = self.v3_server_credentials_lwm2m_get_with_http_info(authorization, **kwargs)
            return data

    def v3_server_credentials_lwm2m_get_with_http_info(self, authorization, **kwargs):
        """
        Fetch LWM2M server credentials.
        This REST API is intended to be used by customers to fetch LWM2M server credentials that they need to use with their clients to connect to LWM2M server. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_server_credentials_lwm2m_get_with_http_info(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_server_credentials_lwm2m_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_server_credentials_lwm2m_get`")


        collection_formats = {}

        resource_path = '/v3/server-credentials/lwm2m'.replace('{format}', 'json')
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
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ServerCredentialsResponseData',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
