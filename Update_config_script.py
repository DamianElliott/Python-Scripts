import requests
import json

# Cisco DNA Center API endpoint
dnac_url = "https://your_dnac_ip_or_hostname"

# API token
headers = {'X-Auth-Token': 'your_token', 'Content-Type': 'application/json'}

# List of network devices to modify the configuration
devices = ["device1", "device2", "device3"]

# Configuration to be applied
config = """
interface GigabitEthernet0/0
 no shut
"""

# Iterate through the list of network devices
for device in devices:
    # Get the device ID
    device_endpoint = f"/dna/intent/api/v1/network-device/ip-address/{device}"
    device_response = requests.get(dnac_url+device_endpoint, headers=headers)
    device_id = json.loads(device_response.text)['response']['id']

    # Modify the device configuration
    config_endpoint = f"/dna/intent/api/v1/network-device/{device_id}/config"
    config_data = {
        "commands": config
    }
    config_response = requests.put(dnac_url+config_endpoint, headers=headers, json=config_data)

    # Check if the configuration was applied successfully
    if config_response.status_code == 200:
        print(f"Configuration applied on {device} successfully")
        # Get the running configuration
        running_config_endpoint = f"/dna/intent/api/v1/network-device/{device_id}/config"
        running_config_response = requests.get(dnac_url+running_config_endpoint, headers=headers)
        running_config = json.loads(running_config_response.text)['response']
        # Compare the running configuration to the desired configuration
        if config.strip() == running_config.strip():
            print(f"Desired configuration was applied correctly on {device}")
        else:
            print(f"Desired configuration was not applied correctly on {device}")
    else:
        print(f"Error applying configuration on {device}: {config_response.text}")

