# coding: utf-8

"""
    Device Query Service API

    This is the API Documentation for the mbed device query service update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.body import Body
from .models.device_query_detail import DeviceQueryDetail
from .models.device_query_resp import DeviceQueryResp

# import apis into sdk package
from .apis.default_api import DefaultApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
