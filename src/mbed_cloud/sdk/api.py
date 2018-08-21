from mbed_cloud import pagination
from mbed_cloud.sdk import common
from mbed_cloud.sdk import fields
from mbed_cloud.sdk import enums


class InstanceFactory:
    """Creates instances of Entities with a client mixed in"""

    def __init__(self, client):
        self.client = client

    def account_group(self, **kwargs):
        """
        :rtype: AccountGroup
        """
        return AccountGroup(client=self.client, **kwargs)

    def api_key(self, **kwargs):
        """
        :rtype: ApiKey
        """
        return ApiKey(client=self.client, **kwargs)

    def login_history(self, **kwargs):
        """
        :rtype: LoginHistory
        """
        return LoginHistory(client=self.client, **kwargs)

    def psk(self, **kwargs):
        """
        :rtype: PSK
        """
        return PSK(client=self.client, **kwargs)

    def user(self, **kwargs):
        """
        :rtype: User
        """
        return User(client=self.client, **kwargs)


class AccountGroup(common.Entity):
    """Represents the `AccountGroup` entity in Mbed Cloud"""

    _fieldnames = [
        "account_id",
        "apikey_count",
        "code",
        "created_at",
        "id",
        "message",
        "name",
        "request_id",
        "updated_at",
        "user_count",
    ]

    def __init__(
        self,
        client=None,
        account_id=None,
        apikey_count=None,
        code=None,
        created_at=None,
        id=None,
        message=None,
        name=None,
        request_id=None,
        updated_at=None,
        user_count=None,
    ):
        """Creates a local `AccountGroup` instance

        :param account_id: The UUID of the account this group belongs to.
        :type account_id: string
        :param apikey_count: The number of API keys in this group.
        :type apikey_count: integer
        :param code: Response code.
        :type code: integer
        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param id: Entity ID.
        :type id: string
        :param message: A human readable message with detailed info.
        :type message: string
        :param name: The name of the group.
        :type name: string
        :param request_id: Request ID.
        :type request_id: string
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        :param user_count: The number of users in this group.
        :type user_count: integer
        """

        super().__init__(client=client)

        # Field attributes
        self._account_id = fields.StringField(account_id)
        self._apikey_count = fields.IntegerField(apikey_count)
        self._code = fields.IntegerField(code)
        self._created_at = fields.DateTimeField(created_at)
        self._id = fields.StringField(id)
        self._message = fields.StringField(message)
        self._name = fields.StringField(name)
        self._request_id = fields.StringField(request_id)
        self._updated_at = fields.DateTimeField(updated_at)
        self._user_count = fields.IntegerField(user_count)

    @property
    def account_id(self):
        """The UUID of the account this group belongs to.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """
        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """
        :param value: set value of `account_id`
        :type value: str
        """
        self._account_id.set(value)

    @property
    def apikey_count(self):
        """The number of API keys in this group.
        
        :rtype: int
        """
        return self._apikey_count.value

    @apikey_count.setter
    def apikey_count(self, value):
        """
        :param value: set value of `apikey_count`
        :type value: int
        """
        self._apikey_count.set(value)

    @property
    def code(self):
        """Response code.
        
        api example: 200
        
        :rtype: int
        """
        return self._code.value

    @code.setter
    def code(self, value):
        """
        :param value: set value of `code`
        :type value: int
        """
        self._code.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """
        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """
        :param value: set value of `created_at`
        :type value: datetime
        """
        self._created_at.set(value)

    @property
    def id(self):
        """Entity ID.
        
        api example: '01619571dad80242ac12000600000000'
        
        :rtype: str
        """
        return self._id.value

    @id.setter
    def id(self, value):
        """
        :param value: set value of `id`
        :type value: str
        """
        self._id.set(value)

    @property
    def message(self):
        """A human readable message with detailed info.
        
        api example: 'success'
        
        :rtype: str
        """
        return self._message.value

    @message.setter
    def message(self, value):
        """
        :param value: set value of `message`
        :type value: str
        """
        self._message.set(value)

    @property
    def name(self):
        """The name of the group.
        
        api example: 'Administrators'
        
        :rtype: str
        """
        return self._name.value

    @name.setter
    def name(self, value):
        """
        :param value: set value of `name`
        :type value: str
        """
        self._name.set(value)

    @property
    def request_id(self):
        """Request ID.
        
        api example: '0161991d63150242ac12000600000000'
        
        :rtype: str
        """
        return self._request_id.value

    @request_id.setter
    def request_id(self, value):
        """
        :param value: set value of `request_id`
        :type value: str
        """
        self._request_id.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """
        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """
        :param value: set value of `updated_at`
        :type value: datetime
        """
        self._updated_at.set(value)

    @property
    def user_count(self):
        """The number of users in this group.
        
        api example: 1
        
        :rtype: int
        """
        return self._user_count.value

    @user_count.setter
    def user_count(self, value):
        """
        :param value: set value of `user_count`
        :type value: int
        """
        self._user_count.set(value)

    def read(self):
        """Get group information.

        api documentation: https://os.mbed.com/search/?q=/v3/policy-groups/{groupID}
        """

        return self._call_api(
            method="get",
            path="/v3/policy-groups/{groupID}",
            path_params={"groupID": self._id.to_api()},
        )

    def update(self):
        """Update the group name.

        api documentation: https://os.mbed.com/search/?q=/v3/policy-groups/{groupID}
        """

        return self._call_api(
            method="put",
            path="/v3/policy-groups/{groupID}",
            path_params={"groupID": self._id.to_api()},
            body_params={"name": self._name.to_api()},
        )


class ApiKey(common.Entity):
    """Represents the `ApiKey` entity in Mbed Cloud"""

    _fieldnames = [
        "created_at",
        "creation_time",
        "groups",
        "id",
        "key",
        "last_login_time",
        "name",
        "owner",
        "status",
        "updated_at",
    ]

    def __init__(
        self,
        client=None,
        created_at=None,
        creation_time=None,
        groups=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `ApiKey` instance

        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param creation_time: The timestamp of the API key creation in the storage, in milliseconds.
        :type creation_time: integer
        :param groups: A list of group IDs this API key belongs to.
        :type groups: array
        :param id: The UUID of the API key.
        :type id: string
        :param key: The API key.
        :type key: string
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: integer
        :param name: The display name for the API key.
        :type name: string
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: string
        :param status: The status of the API key.
        :type status: string
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        """

        super().__init__(client=client)

        # Field attributes
        self._created_at = fields.DateTimeField(created_at)
        self._creation_time = fields.IntegerField(creation_time)
        self._groups = fields.ListField(groups)
        self._id = fields.StringField(id)
        self._key = fields.StringField(key)
        self._last_login_time = fields.IntegerField(last_login_time)
        self._name = fields.StringField(name)
        self._owner = fields.StringField(owner)
        self._status = fields.StringField(status)
        self._updated_at = fields.DateTimeField(updated_at)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """
        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """
        :param value: set value of `created_at`
        :type value: datetime
        """
        self._created_at.set(value)

    @property
    def creation_time(self):
        """The timestamp of the API key creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """
        return self._creation_time.value

    @creation_time.setter
    def creation_time(self, value):
        """
        :param value: set value of `creation_time`
        :type value: int
        """
        self._creation_time.set(value)

    @property
    def groups(self):
        """A list of group IDs this API key belongs to.
        
        :rtype: list
        """
        return self._groups.value

    @groups.setter
    def groups(self, value):
        """
        :param value: set value of `groups`
        :type value: list
        """
        self._groups.set(value)

    @property
    def id(self):
        """The UUID of the API key.
        
        api example: '01619571f7020242ac12000600000000'
        
        :rtype: str
        """
        return self._id.value

    @id.setter
    def id(self, value):
        """
        :param value: set value of `id`
        :type value: str
        """
        self._id.set(value)

    @property
    def key(self):
        """The API key.
        
        api example: 'ak_1MDE2MTk1NzFmNmU4MDI0MmFjMTIwMDA2MDAwMDAwMDA01619571f7020242ac12000600000000'
        
        :rtype: str
        """
        return self._key.value

    @key.setter
    def key(self, value):
        """
        :param value: set value of `key`
        :type value: str
        """
        self._key.set(value)

    @property
    def last_login_time(self):
        """The timestamp of the latest API key usage, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """
        return self._last_login_time.value

    @last_login_time.setter
    def last_login_time(self, value):
        """
        :param value: set value of `last_login_time`
        :type value: int
        """
        self._last_login_time.set(value)

    @property
    def name(self):
        """The display name for the API key.
        
        api example: 'API key gorgon'
        
        :rtype: str
        """
        return self._name.value

    @name.setter
    def name(self, value):
        """
        :param value: set value of `name`
        :type value: str
        """
        self._name.set(value)

    @property
    def owner(self):
        """The owner of this API key, who is the creator by default.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """
        return self._owner.value

    @owner.setter
    def owner(self, value):
        """
        :param value: set value of `owner`
        :type value: str
        """
        self._owner.set(value)

    @property
    def status(self):
        """The status of the API key.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """
        return self._status.value

    @status.setter
    def status(self, value):
        """
        :param value: set value of `status`
        :type value: str
        """
        self._status.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """
        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """
        :param value: set value of `updated_at`
        :type value: datetime
        """
        self._updated_at.set(value)

    def create(self):
        """Create a new API key.

        api documentation: https://os.mbed.com/search/?q=/v3/api-keys
        """

        return self._call_api(
            method="post",
            path="/v3/api-keys",
            body_params={
                "groups": self._groups.to_api(),
                "name": self._name.to_api(),
                "owner": self._owner.to_api(),
                "status": self._status.to_api(),
            },
        )

    def delete(self):
        """Delete API key.

        api documentation: https://os.mbed.com/search/?q=/v3/api-keys/{apiKey}
        """

        return self._call_api(
            method="delete",
            path="/v3/api-keys/{apiKey}",
            path_params={"apiKey": self._id.to_api()},
        )

    def group_ids(self, include=None):
        """Get groups of the API key.

        api documentation: https://os.mbed.com/search/?q=/v3/api-keys/me/groups
        """

        return self._call_api(
            method="get",
            path="/v3/api-keys/me/groups",
            query_params={
                "after": self._after.to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": self._limit.to_api(),
                "order": self._order.to_api(),
            },
        )

    def list(self, include=None):
        """Get all API keys

        api documentation: https://os.mbed.com/search/?q=/v3/api-keys
        """

        return pagination.PaginatedResponse(func=self._list, lwrap_type=self.__class__)

    def _list(self, include=None):
        """Internal 'next-page' behaviour for pagination"""

        return self._call_api(
            method="get",
            path="/v3/api-keys",
            query_params={
                "after": self._after.to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": self._limit.to_api(),
                "order": self._order.to_api(),
            },
            unpack=False,
        )

    def read(self):
        """Get API key details.

        api documentation: https://os.mbed.com/search/?q=/v3/api-keys/{apiKey}
        """

        return self._call_api(
            method="get",
            path="/v3/api-keys/{apiKey}",
            path_params={"apiKey": self._id.to_api()},
        )

    def update(self):
        """Update API key details.

        api documentation: https://os.mbed.com/search/?q=/v3/api-keys/{apiKey}
        """

        return self._call_api(
            method="put",
            path="/v3/api-keys/{apiKey}",
            path_params={"apiKey": self._id.to_api()},
            body_params={
                "groups": self._groups.to_api(),
                "name": self._name.to_api(),
                "owner": self._owner.to_api(),
                "status": self._status.to_api(),
            },
        )


class LoginHistory(common.Entity):
    """Represents the `LoginHistory` entity in Mbed Cloud"""

    _fieldnames = ["date", "ip_address", "success", "user_agent"]

    def __init__(
        self, client=None, date=None, ip_address=None, success=None, user_agent=None
    ):
        """Creates a local `LoginHistory` instance

        :param date: UTC time RFC3339 for this login attempt.
        :type date: string
        :param ip_address: IP address of the client.
        :type ip_address: string
        :param success: Flag indicating whether login attempt was successful or not.
        :type success: boolean
        :param user_agent: User Agent header from the login request.
        :type user_agent: string
        """

        super().__init__(client=client)

        # Field attributes
        self._date = fields.DateTimeField(date)
        self._ip_address = fields.StringField(ip_address)
        self._success = fields.BooleanField(success)
        self._user_agent = fields.StringField(user_agent)

    @property
    def date(self):
        """UTC time RFC3339 for this login attempt.
        
        api example: '2018-02-14T17:52:07Z'
        
        :rtype: datetime
        """
        return self._date.value

    @date.setter
    def date(self, value):
        """
        :param value: set value of `date`
        :type value: datetime
        """
        self._date.set(value)

    @property
    def ip_address(self):
        """IP address of the client.
        
        api example: '127.0.0.1'
        
        :rtype: str
        """
        return self._ip_address.value

    @ip_address.setter
    def ip_address(self, value):
        """
        :param value: set value of `ip_address`
        :type value: str
        """
        self._ip_address.set(value)

    @property
    def success(self):
        """Flag indicating whether login attempt was successful or not.
        
        api example: True
        
        :rtype: bool
        """
        return self._success.value

    @success.setter
    def success(self, value):
        """
        :param value: set value of `success`
        :type value: bool
        """
        self._success.set(value)

    @property
    def user_agent(self):
        """User Agent header from the login request.
        
        api example: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)
            Chrome/41.0.2227.1 Safari/537.36'
        
        :rtype: str
        """
        return self._user_agent.value

    @user_agent.setter
    def user_agent(self, value):
        """
        :param value: set value of `user_agent`
        :type value: str
        """
        self._user_agent.set(value)


class PSK(common.Entity):
    """Represents the `PSK` entity in Mbed Cloud"""

    _fieldnames = ["created_at", "endpoint_name"]

    def __init__(self, client=None, created_at=None, endpoint_name=None):
        """Creates a local `PSK` instance

        :param created_at: The date-time (RFC3339) when this pre-shared key was uploaded to Mbed Cloud.
        :type created_at: string
        :param endpoint_name: The unique endpoint identifier that this pre-shared key applies to. 16-64
            [printable](https://en.wikipedia.org/wiki/ASCII#Printable_characters) (non-control)
            ASCII characters.
        :type endpoint_name: string
        """

        super().__init__(client=client)

        # Field attributes
        self._created_at = fields.DateTimeField(created_at)
        self._endpoint_name = fields.StringField(endpoint_name)

    @property
    def created_at(self):
        """The date-time (RFC3339) when this pre-shared key was uploaded to Mbed Cloud.
        
        api example: '2017-07-21T17:32:28.012Z'
        
        :rtype: datetime
        """
        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """
        :param value: set value of `created_at`
        :type value: datetime
        """
        self._created_at.set(value)

    @property
    def endpoint_name(self):
        """The unique endpoint identifier that this pre-shared key applies to. 16-64
        [printable](https://en.wikipedia.org/wiki/ASCII#Printable_characters) (non-control)
        ASCII characters.
        
        api example: 'my-endpoint-0001'
        
        :rtype: str
        """
        return self._endpoint_name.value

    @endpoint_name.setter
    def endpoint_name(self, value):
        """
        :param value: set value of `endpoint_name`
        :type value: str
        """
        self._endpoint_name.set(value)

    def create(self, secret_hex=None):
        """Upload a pre-shared key to Mbed Cloud.

        api documentation: https://os.mbed.com/search/?q=/v2/device-shared-keys
        """

        return self._call_api(
            method="post",
            path="/v2/device-shared-keys",
            body_params={
                "endpoint_name": self._endpoint_name.to_api(),
                "secret_hex": fields.StringField(secret_hex).to_api(),
            },
        )

    def delete(self):
        """Remove a pre-shared key.

        api documentation: https://os.mbed.com/search/?q=/v2/device-shared-keys/{endpoint_name}
        """

        return self._call_api(
            method="delete",
            path="/v2/device-shared-keys/{endpoint_name}",
            path_params={"endpoint_name": self._endpoint_name.to_api()},
        )

    def list(self):
        """List pre-shared keys.

        api documentation: https://os.mbed.com/search/?q=/v2/device-shared-keys
        """

        return pagination.PaginatedResponse(func=self._list, lwrap_type=self.__class__)

    def _list(self):
        """Internal 'next-page' behaviour for pagination"""

        return self._call_api(
            method="get",
            path="/v2/device-shared-keys",
            query_params={"after": self._after.to_api(), "limit": self._limit.to_api()},
            unpack=False,
        )

    def read(self):
        """Get a pre-shared key.

        api documentation: https://os.mbed.com/search/?q=/v2/device-shared-keys/{endpoint_name}
        """

        return self._call_api(
            method="get",
            path="/v2/device-shared-keys/{endpoint_name}",
            path_params={"endpoint_name": self._endpoint_name.to_api()},
        )


class User(common.Entity):
    """Represents the `User` entity in Mbed Cloud"""

    _fieldnames = [
        "account_id",
        "address",
        "created_at",
        "creation_time",
        "email",
        "email_verified",
        "full_name",
        "groups",
        "id",
        "last_login_time",
        "login_history",
        "marketing_accepted",
        "password",
        "password_changed_time",
        "phone_number",
        "status",
        "terms_accepted",
        "two_factor_auth_enabled",
        "updated_at",
        "username",
    ]

    def __init__(
        self,
        client=None,
        account_id=None,
        address=None,
        created_at=None,
        creation_time=None,
        email=None,
        email_verified=None,
        full_name=None,
        groups=None,
        id=None,
        last_login_time=None,
        login_history=None,
        marketing_accepted=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        terms_accepted=None,
        two_factor_auth_enabled=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `User` instance

        :param account_id: The UUID of the account.
        :type account_id: string
        :param address: Address.
        :type address: string
        :param created_at: Creation UTC time RFC3339.
        :type created_at: string
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: integer
        :param email: The email address.
        :type email: string
        :param email_verified: A flag indicating whether the user's email address has been verified or not.
        :type email_verified: boolean
        :param full_name: The full name of the user.
        :type full_name: string
        :param groups: A list of IDs of the groups this user belongs to.
        :type groups: array
        :param id: The UUID of the user.
        :type id: string
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: integer
        :param login_history: Timestamps, succeedings, IP addresses and user agent information of the last five logins
            of the user, with timestamps in RFC3339 format.
        :type login_history: array
        :param marketing_accepted: A flag indicating that receiving marketing information has been accepted.
        :type marketing_accepted: boolean
        :param password: The password when creating a new user. It will be generated when not present in the
            request.
        :type password: string
        :param password_changed_time: A timestamp of the latest change of the user password, in milliseconds.
        :type password_changed_time: integer
        :param phone_number: Phone number.
        :type phone_number: string
        :param status: The status of the user. ENROLLING state indicates that the user is in the middle of the
            enrollment process. INVITED means that the user has not accepted the invitation request.
            RESET means that the password must be changed immediately. INACTIVE users are locked out
            and not permitted to use the system.
        :type status: string
        :param terms_accepted: A flag indicating that the General Terms and Conditions has been accepted.
        :type terms_accepted: boolean
        :param two_factor_auth_enabled: A flag indicating whether 2-factor authentication (TOTP) has been enabled.
        :type two_factor_auth_enabled: boolean
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: string
        :param username: A username containing alphanumerical letters and -,._@+= characters.
        :type username: string
        """

        super().__init__(client=client)

        # Field attributes
        self._account_id = fields.StringField(account_id)
        self._address = fields.StringField(address)
        self._created_at = fields.DateTimeField(created_at)
        self._creation_time = fields.IntegerField(creation_time)
        self._email = fields.StringField(email)
        self._email_verified = fields.BooleanField(email_verified)
        self._full_name = fields.StringField(full_name)
        self._groups = fields.ListField(groups)
        self._id = fields.StringField(id)
        self._last_login_time = fields.IntegerField(last_login_time)
        self._login_history = fields.ListField(login_history)
        self._marketing_accepted = fields.BooleanField(marketing_accepted)
        self._password = fields.StringField(password)
        self._password_changed_time = fields.IntegerField(password_changed_time)
        self._phone_number = fields.StringField(phone_number)
        self._status = fields.StringField(status)
        self._terms_accepted = fields.BooleanField(terms_accepted)
        self._two_factor_auth_enabled = fields.BooleanField(two_factor_auth_enabled)
        self._updated_at = fields.DateTimeField(updated_at)
        self._username = fields.StringField(username)

    @property
    def account_id(self):
        """The UUID of the account.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """
        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """
        :param value: set value of `account_id`
        :type value: str
        """
        self._account_id.set(value)

    @property
    def address(self):
        """Address.
        
        api example: '110 Fulbourn Rd, Cambridge, United Kingdom'
        
        :rtype: str
        """
        return self._address.value

    @address.setter
    def address(self, value):
        """
        :param value: set value of `address`
        :type value: str
        """
        self._address.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """
        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """
        :param value: set value of `created_at`
        :type value: datetime
        """
        self._created_at.set(value)

    @property
    def creation_time(self):
        """A timestamp of the user creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """
        return self._creation_time.value

    @creation_time.setter
    def creation_time(self, value):
        """
        :param value: set value of `creation_time`
        :type value: int
        """
        self._creation_time.set(value)

    @property
    def email(self):
        """The email address.
        
        api example: 'user@arm.com'
        
        :rtype: str
        """
        return self._email.value

    @email.setter
    def email(self, value):
        """
        :param value: set value of `email`
        :type value: str
        """
        self._email.set(value)

    @property
    def email_verified(self):
        """A flag indicating whether the user's email address has been verified or not.
        
        api example: True
        
        :rtype: bool
        """
        return self._email_verified.value

    @email_verified.setter
    def email_verified(self, value):
        """
        :param value: set value of `email_verified`
        :type value: bool
        """
        self._email_verified.set(value)

    @property
    def full_name(self):
        """The full name of the user.
        
        api example: 'User Doe'
        
        :rtype: str
        """
        return self._full_name.value

    @full_name.setter
    def full_name(self, value):
        """
        :param value: set value of `full_name`
        :type value: str
        """
        self._full_name.set(value)

    @property
    def groups(self):
        """A list of IDs of the groups this user belongs to.
        
        :rtype: list
        """
        return self._groups.value

    @groups.setter
    def groups(self, value):
        """
        :param value: set value of `groups`
        :type value: list
        """
        self._groups.set(value)

    @property
    def id(self):
        """The UUID of the user.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """
        return self._id.value

    @id.setter
    def id(self, value):
        """
        :param value: set value of `id`
        :type value: str
        """
        self._id.set(value)

    @property
    def last_login_time(self):
        """A timestamp of the latest login of the user, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """
        return self._last_login_time.value

    @last_login_time.setter
    def last_login_time(self, value):
        """
        :param value: set value of `last_login_time`
        :type value: int
        """
        self._last_login_time.set(value)

    @property
    def login_history(self):
        """Timestamps, succeedings, IP addresses and user agent information of the last five logins
        of the user, with timestamps in RFC3339 format.
        
        :rtype: list
        """
        return self._login_history.value

    @login_history.setter
    def login_history(self, value):
        """
        :param value: set value of `login_history`
        :type value: list
        """
        self._login_history.set(value)

    @property
    def marketing_accepted(self):
        """A flag indicating that receiving marketing information has been accepted.
        
        api example: True
        
        :rtype: bool
        """
        return self._marketing_accepted.value

    @marketing_accepted.setter
    def marketing_accepted(self, value):
        """
        :param value: set value of `marketing_accepted`
        :type value: bool
        """
        self._marketing_accepted.set(value)

    @property
    def password(self):
        """The password when creating a new user. It will be generated when not present in the
        request.
        
        api example: 'PZf9eEUH43DAPE9ULINFeuj'
        
        :rtype: str
        """
        return self._password.value

    @password.setter
    def password(self, value):
        """
        :param value: set value of `password`
        :type value: str
        """
        self._password.set(value)

    @property
    def password_changed_time(self):
        """A timestamp of the latest change of the user password, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """
        return self._password_changed_time.value

    @password_changed_time.setter
    def password_changed_time(self, value):
        """
        :param value: set value of `password_changed_time`
        :type value: int
        """
        self._password_changed_time.set(value)

    @property
    def phone_number(self):
        """Phone number.
        
        api example: '+44 (1223) 400 400'
        
        :rtype: str
        """
        return self._phone_number.value

    @phone_number.setter
    def phone_number(self, value):
        """
        :param value: set value of `phone_number`
        :type value: str
        """
        self._phone_number.set(value)

    @property
    def status(self):
        """The status of the user. ENROLLING state indicates that the user is in the middle of the
        enrollment process. INVITED means that the user has not accepted the invitation request.
        RESET means that the password must be changed immediately. INACTIVE users are locked out
        and not permitted to use the system.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """
        return self._status.value

    @status.setter
    def status(self, value):
        """
        :param value: set value of `status`
        :type value: str
        """
        self._status.set(value)

    @property
    def terms_accepted(self):
        """A flag indicating that the General Terms and Conditions has been accepted.
        
        api example: True
        
        :rtype: bool
        """
        return self._terms_accepted.value

    @terms_accepted.setter
    def terms_accepted(self, value):
        """
        :param value: set value of `terms_accepted`
        :type value: bool
        """
        self._terms_accepted.set(value)

    @property
    def two_factor_auth_enabled(self):
        """A flag indicating whether 2-factor authentication (TOTP) has been enabled.
        
        api example: True
        
        :rtype: bool
        """
        return self._two_factor_auth_enabled.value

    @two_factor_auth_enabled.setter
    def two_factor_auth_enabled(self, value):
        """
        :param value: set value of `two_factor_auth_enabled`
        :type value: bool
        """
        self._two_factor_auth_enabled.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """
        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """
        :param value: set value of `updated_at`
        :type value: datetime
        """
        self._updated_at.set(value)

    @property
    def username(self):
        """A username containing alphanumerical letters and -,._@+= characters.
        
        api example: 'admin'
        
        :rtype: str
        """
        return self._username.value

    @username.setter
    def username(self, value):
        """
        :param value: set value of `username`
        :type value: str
        """
        self._username.set(value)

    def delete(self):
        """Delete a user.

        api documentation: https://os.mbed.com/search/?q=/v3/users/{user-id}
        """

        return self._call_api(
            method="delete",
            path="/v3/users/{user-id}",
            path_params={"user-id": self._id.to_api()},
            inbound_renames={
                "is_marketing_accepted": "marketing_accepted",
                "is_gtc_accepted": "terms_accepted",
                "is_totp_enabled": "two_factor_auth_enabled",
            },
        )

    def group_ids(self, include=None):
        """Get groups of the user.

        api documentation: https://os.mbed.com/search/?q=/v3/accounts/{accountID}/users/{user-id}/groups
        """

        return self._call_api(
            method="get",
            path="/v3/accounts/{accountID}/users/{user-id}/groups",
            path_params={
                "accountID": self._account_id.to_api(),
                "user-id": self._id.to_api(),
            },
            query_params={
                "after": self._after.to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": self._limit.to_api(),
                "order": self._order.to_api(),
            },
            inbound_renames={
                "is_marketing_accepted": "marketing_accepted",
                "is_gtc_accepted": "terms_accepted",
                "is_totp_enabled": "two_factor_auth_enabled",
            },
        )

    def list(self, include=None):
        """Get the details of all users.

        api documentation: https://os.mbed.com/search/?q=/v3/users
        """

        return pagination.PaginatedResponse(func=self._list, lwrap_type=self.__class__)

    def _list(self, include=None):
        """Internal 'next-page' behaviour for pagination"""

        return self._call_api(
            method="get",
            path="/v3/users",
            query_params={
                "after": self._after.to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": self._limit.to_api(),
                "order": self._order.to_api(),
            },
            inbound_renames={
                "is_marketing_accepted": "marketing_accepted",
                "is_gtc_accepted": "terms_accepted",
                "is_totp_enabled": "two_factor_auth_enabled",
            },
            unpack=False,
        )

    def read(self):
        """Details of a user.

        api documentation: https://os.mbed.com/search/?q=/v3/users/{user-id}
        """

        return self._call_api(
            method="get",
            path="/v3/users/{user-id}",
            path_params={"user-id": self._id.to_api()},
            inbound_renames={
                "is_marketing_accepted": "marketing_accepted",
                "is_gtc_accepted": "terms_accepted",
                "is_totp_enabled": "two_factor_auth_enabled",
            },
        )

    def update(self):
        """Update user details.

        api documentation: https://os.mbed.com/search/?q=/v3/users/{user-id}
        """

        return self._call_api(
            method="put",
            path="/v3/users/{user-id}",
            path_params={"user-id": self._id.to_api()},
            body_params={
                "address": self._address.to_api(),
                "full_name": self._full_name.to_api(),
                "groups": self._groups.to_api(),
                "is_marketing_accepted": self._marketing_accepted.to_api(),
                "phone_number": self._phone_number.to_api(),
                "is_gtc_accepted": self._terms_accepted.to_api(),
                "is_totp_enabled": self._two_factor_auth_enabled.to_api(),
                "username": self._username.to_api(),
            },
            inbound_renames={
                "is_marketing_accepted": "marketing_accepted",
                "is_gtc_accepted": "terms_accepted",
                "is_totp_enabled": "two_factor_auth_enabled",
            },
        )
