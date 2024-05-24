from ncclient import manager

# Fill in the device IP and credentials
nexus = manager.connect(host='', port=830, username='', password='',
                        allow_agent=False,
                        look_for_keys=False,
                        hostkey_verify=False,
                        unknown_host_cb=True)

for capability in nexus.server_capabilities:
    print(capability)
