import functools
import requests
import dotenv
import os
import json
import functools
import textwrap

from mbed_cloud import utils
from mbed_cloud import pagination


def pluck_if_not_none(source, *pluck):
    return {k: source[k] for k in pluck if source[k] is not None}


def strip_none_values(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}


DEFAULT_HOST = "https://api.us-east-1.mbedcloud.com"
DEFAULT_API_KEY = None

global_sdk = None


class ApiErrorResponse(requests.HTTPError):
    pass


def paginate(unpack):
    """Decorator that wraps listable_call

    In a way that allows it to be paginated
    """

    def decorator(listable_call):
        @functools.wraps(listable_call)
        def wrapper(**kwargs):
            return pagination.PaginatedResponse(
                func=listable_call, lwrap_type=unpack, unpack=False, **kwargs
            )

        return wrapper

    return decorator


class Config:
    _tried_dotenv = False
    api_key = None
    host = None

    def __init__(self, **kwargs):
        self._set_defaults(**kwargs)
        if not self.api_key and not Config._tried_dotenv:
            dotenv.load_dotenv(
                dotenv.find_dotenv(usecwd=True, raise_error_if_not_found=True)
            )
            self._set_defaults()
            # mark dotenv load complete, so we don't have to do it again
            Config._tried_dotenv = True

    def _set_defaults(self, **updates):
        self.update(updates)
        self.api_key = (
            self.api_key or os.getenv("MBED_CLOUD_SDK_API_KEY") or DEFAULT_API_KEY
        )
        self.host = self.host or os.getenv("MBED_CLOUD_SDK_HOST") or DEFAULT_HOST
        self.user_agent = utils.get_user_agent()

    def update(self, *updates, **kwargs):
        for update in updates:
            self.update(**update)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def items(self):
        return ((k, v) for k, v in vars(self).items() if not k.startswith("_"))


class SDK:
    def __init__(self, config=None, **config_overrides):
        self._config = Config()
        self._config.update({"user_agent": utils.get_user_agent()})
        self._config.update(config or {})
        self._config.update(config_overrides)

        self._client = Client(self._config)

        from mbed_cloud.sdk import api

        self.factory = api.InstanceFactory(self)

    @property
    def client(self):
        return self._client


class Client:
    def __init__(self, config):
        """

        :param config:
        :type config: Config
        """
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": "Bearer %s" % self.config.api_key,
                "UserAgent": utils.get_user_agent(),
            }
        )


def get_or_create_global_sdk_instance():
    global global_sdk
    if global_sdk is None:
        global_sdk = SDK()
    return global_sdk


class Entity:
    def __init__(self, client, **kwargs):
        """

        :param client:
        :type client: Client or SDK
        :param kwargs:
        """
        if client is None:
            client = get_or_create_global_sdk_instance()
        if isinstance(client, SDK):
            client = client.client
        self._client = client

    def __repr__(self):
        return repr({k: v for k, v in vars(self).items() if k in self._fieldnames})

    def _call_api(
        self,
        method,
        path,
        headers=None,
        path_params=None,
        query_params=None,
        body_params=None,
        stream_params=None,
        inbound_renames=None,
        unpack=None,
        **kwargs,
    ):
        """Uses an http request handling mechanism to fetch and return results from the network"""
        url = self._client.config.host + path
        if path_params:
            url = url.format(**path_params)
        response = self._client.session.request(
            method=method,
            url=url,
            headers=headers,
            params=query_params,
            json=body_params,
            files=stream_params,
            stream=bool(stream_params),
            **kwargs,
        )
        if unpack is None:
            unpack = self

        if response.status_code // 100 == 2:
            if unpack:
                for k, v in response.json().items():
                    field = getattr(unpack, "_" + inbound_renames.get(k, k), None)
                    if field:
                        field.from_api(v)
                return unpack
            else:
                return response
        else:
            # check if we didn't have an api key set
            all_params = locals()
            api_key = self._client.config.api_key or ""
            host = self._client.config.host
            hints = [
                "URL: %s" % url,
                "Using host: %r api_key: '%s%s%s'"
                % (host, api_key[:2], "***" if api_key else "", api_key[-3:]),
                "More parameters are attached to this error as `all_parameters`.",
            ]
            if not api_key:
                hints.append(
                    "There was no API key detected. You need to set one to interact with the cloud."
                )
            if not host.startswith("https"):
                hints.append(
                    "The host scheme should start with 'https' for a secure connection to the cloud."
                )
            hints = "\n".join(hints)
            try:
                content = json.loads(response.content)
            except Exception:
                content = {"response": content}
            api_feedback = textwrap.indent(json.dumps(content, indent=2), "  ")
            error = ApiErrorResponse(
                "Error response from API (HTTP %s):\n%s\nMore information:\n%s"
                % (response.status_code, api_feedback, hints)
            )
            error.content = content
            error.all_parameters = all_params
            raise error
