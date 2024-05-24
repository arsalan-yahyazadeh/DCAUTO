from ncclient import manager
import sys
from lxml import etree
from rich import print

# Fill in the device IP and credentials
device = {
    "address": "",
    "netconf_port": 830,
    "username": "",
    "password": ""
}


def main():
    remove_loopback = """
    <config>
      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <intf-items>
          <lb-items>
            <LbRtdIf-list operation="delete">
              <id>lo10</id>
            </LbRtdIf-list>
          </lb-items>
        </intf-items>
      </System>
    </config>"""

    with manager.connect(host=device["address"],
                         port=device["netconf_port"],
                         username=device["username"],
                         password=device["password"],
                         hostkey_verify=False) as m:

        # create vlan with edit_config
        netconf_response = m.edit_config(
            target="running", config=remove_loopback)

        print(netconf_response)


main()
