# coding: utf-8

"""
    Provisioning endpoints - developer certificates.

    A developer certificate is used during development to allow quick association of the device with the mbed Cloud account of the developer. It is used instead of the Factory Tool.  The developer should generate a key-pair (NIST P-256 Elliptic Curve), add the public key to the mbed Cloud account using these APIs, and use the private key on the device (typically in a file named identity_dev_security.c). This creates an association between the device and the cloud.  Only one developer certificate per account is allowed.  As an example, a developer certificate can be created using OpenSSL as follows:  ``` openssl ecparam -out key.pem -name prime256v1 -genkey openssl ec -text -in key.pem -pubout ```  The output is:  ``` read EC key Private-Key: (256 bit) priv:     4e:50:25:1c:c0:70:29:05:dc:1d:7b:58:ba:a1:27:     c3:6f:aa:92:22:ca:0f:f1:af:74:cb:15:a4:cb:36:     98:3f pub:     04:35:54:40:80:f8:fb:45:ad:8a:fc:1a:9e:8c:88:     58:fa:84:91:ca:51:d2:09:d5:7b:35:9f:72:10:31:     a2:7c:d6:18:8b:49:d9:56:91:f0:99:b7:a9:a0:c6:     c1:5b:b8:d3:24:a8:cd:0c:76:9f:f0:c8:41:b0:a3:     dd:d3:2c:88:e1 ASN1 OID: prime256v1 NIST CURVE: P-256 writing EC key -----BEGIN PUBLIC KEY----- MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAENVRAgPj7Ra2K/BqejIhY+oSRylHS CdV7NZ9yEDGifNYYi0nZVpHwmbepoMbBW7jTJKjNDHaf8MhBsKPd0yyI4Q== -----END PUBLIC KEY----- ```  The bytes under \"priv\" are the 32 private key bytes. They should be placed on the device (in the identity_dev_security.c file), as a byte array.  The text starting with \"BEGIN PUBLIC KEY\" is the public key in PEM format, which should be uploaded using the POST API.  Another example, using Python:  ``` from ecdsa import SigningKey, NIST256p private_key = SigningKey.generate(curve=NIST256p) public_key = private_key.get_verifying_key() print \"Public key:\" print public_key.to_pem() bytes = bytearray(private_key.to_string()) for byte in bytes:   print hex(byte) + \",\", ``` 

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

    def v3_developer_certificate_delete(self, authorization, **kwargs):
        """
        
        Deletes the account's developer certificate (only one per account allowed).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificate_delete(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by the reference token or API key. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_developer_certificate_delete_with_http_info(authorization, **kwargs)
        else:
            (data) = self.v3_developer_certificate_delete_with_http_info(authorization, **kwargs)
            return data

    def v3_developer_certificate_delete_with_http_info(self, authorization, **kwargs):
        """
        
        Deletes the account's developer certificate (only one per account allowed).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificate_delete_with_http_info(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by the reference token or API key. (required)
        :return: None
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
                    " to method v3_developer_certificate_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_developer_certificate_delete`")

        resource_path = '/v3/developer-certificate'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'DELETE',
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

    def v3_developer_certificate_get(self, authorization, **kwargs):
        """
        
        Gets the developer certificate of the account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificate_get(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by the reference token or API key. (required)
        :return: DeveloperCertificate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_developer_certificate_get_with_http_info(authorization, **kwargs)
        else:
            (data) = self.v3_developer_certificate_get_with_http_info(authorization, **kwargs)
            return data

    def v3_developer_certificate_get_with_http_info(self, authorization, **kwargs):
        """
        
        Gets the developer certificate of the account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificate_get_with_http_info(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by the reference token or API key. (required)
        :return: DeveloperCertificate
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
                    " to method v3_developer_certificate_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_developer_certificate_get`")

        resource_path = '/v3/developer-certificate'.replace('{format}', 'json')
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
                                            response_type='DeveloperCertificate',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v3_developer_certificate_post(self, authorization, body, **kwargs):
        """
        
        Adds a developer certificate to the account (only one per account allowed).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificate_post(authorization, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by the reference token or API key. (required)
        :param Body body:  (required)
        :return: DeveloperCertificate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_developer_certificate_post_with_http_info(authorization, body, **kwargs)
        else:
            (data) = self.v3_developer_certificate_post_with_http_info(authorization, body, **kwargs)
            return data

    def v3_developer_certificate_post_with_http_info(self, authorization, body, **kwargs):
        """
        
        Adds a developer certificate to the account (only one per account allowed).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_developer_certificate_post_with_http_info(authorization, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: \"Bearer\" followed by the reference token or API key. (required)
        :param Body body:  (required)
        :return: DeveloperCertificate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_developer_certificate_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_developer_certificate_post`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v3_developer_certificate_post`")

        resource_path = '/v3/developer-certificate'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeveloperCertificate',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
