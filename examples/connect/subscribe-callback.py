# ---------------------------------------------------------------------------
# Pelion Device Management SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Example showing basic usage of device resource subscriptions."""
from mbed_cloud import ConnectAPI

BUTTON_RESOURCE = "/5002/0/1"


def _current_val(value):
    # Print the current value
    print("Current value: %r" % (value))


def _subscription_handler(device_id, path, value):
    print("Device: %s, Resoure path: %s, Current value: %r" % (device_id, path, value))


def _main():
    api = ConnectAPI()
    # calling start_notifications is required for getting/setting resource synchronously
    api.start_notifications()
    devices = api.list_connected_devices().data
    if not devices:
        raise Exception("No connected devices registered. Aborting")

    # Synchronously get the initial/current value of the resource
    value = api.get_resource_value(devices[0].id, BUTTON_RESOURCE)
    _current_val(value)

    # Register a subscription for new values
    api.add_resource_subscription_async(devices[0].id, BUTTON_RESOURCE, _subscription_handler)

    # Run forever
    while True:
        pass


if __name__ == "__main__":
    _main()
