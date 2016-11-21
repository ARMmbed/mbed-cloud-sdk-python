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
import io
import json
import ssl
import certifi
import logging
import re

# python 2 and python 3 compatibility library
from six import iteritems

from .configuration import Configuration

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')

try:
    # for python3
    from urllib.parse import urlencode
except ImportError:
    # for python2
    from urllib import urlencode


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """
        Returns a dictionary of the response headers.
        """
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """
        Returns a given response header.
        """
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, pools_size=4):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680
        # ca_certs vs cert_file vs key_file
        # http://stackoverflow.com/a/23957365/2985775

        # cert_reqs
        if Configuration().verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if Configuration().ssl_ca_cert:
            ca_certs = Configuration().ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        # cert_file
        cert_file = Configuration().cert_file

        # key file
        key_file = Configuration().key_file

        # https pool manager
        self.pool_manager = urllib3.PoolManager(
            num_pools=pools_size,
            cert_reqs=cert_reqs,
            ca_certs=ca_certs,
            cert_file=cert_file,
            key_file=key_file
        )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None):
        """
        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencode`
                            and `multipart/form-data`
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = None
                    if body:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(method, url,
                                                  body=request_body,
                                                  headers=headers)
                if headers['Content-Type'] == 'application/x-www-form-urlencoded':
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=False,
                                                  headers=headers)
                if headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct Content-Type
                    # which generated by urllib3 will be overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=True,
                                                  headers=headers)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        r = RESTResponse(r)

        # In the python 3, the response.data is bytes.
        # we need to decode it to string.
        if sys.version_info > (3,):
            r.data = r.data.decode('utf8')

        # log response body
        logger.debug("response body: %s" % r.data)

        if r.status not in range(200, 206):
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None):
        return self.request("GET", url,
                            headers=headers,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None):
        return self.request("HEAD", url,
                            headers=headers,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None, body=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None, body=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None, body=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """
        Custom error messages for exception
        """
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
