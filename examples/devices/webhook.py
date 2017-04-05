# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Example showing basic usage of the webhook functionality."""
from mbed_cloud.devices import DeviceAPI
import time

BUTTON_RESOURCE = "/3200/0/5501"


def _main():
    api = DeviceAPI()
    devices = api.list_connected_devices()
    if devices.count() == 0:
        raise Exception("No endpints registered. Aborting")

    # First register to one webhook
    api.add_webhook("http://api.webhookinbox.com/i/UTComlHQ/in/")
    time.sleep(2)

    # Then register to another one
    api.add_webhook("http://api.webhookinbox.com/i/SyjKevok/in/")
    api.add_subscription(list(devices)[0].id, BUTTON_RESOURCE)
    while True:
        print("Webhook registered. Listening to button updates for 10 seconds...")

        time.sleep(10)
        break

    api.delete_webhook()
    print("Deregistered and ubsubscribed to all resourced. Exiting.")


if __name__ == '__main__':
    _main()
