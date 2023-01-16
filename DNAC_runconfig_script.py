import os
import requests
import json

# Cisco DNA Center API endpoint
dnac_url = "https://your_dnac_ip_or_hostname"

# API token
headers = {'X-Auth-Token': 'your_token'}

# Get list of network devices
devices_endpoint = "/dna/intent/api/v1/network-device"
response = requests.get(dnac_url+devices_endpoint, headers=headers)

# Parse the JSON response
devices = json.loads(response.text)['response']

# Create the folder if it does not exist
folder_name = "Network Devices Running Config"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Iterate through the list of network devices
for device in devices:
    hostname = device['hostname']
    id = device['id']
    # Get running configuration of the device
    config_endpoint = f"/dna/intent/api/v1/network-device/{id}/config"
    config_response = requests.get(dnac_url+config_endpoint, headers=headers)
    config = json.loads(config_response.text)['response']
    # Save the running configuration to a text file
    file_path = os.path.join(folder_name, f"{hostname}.txt")
    with open(file_path, "w") as file:
        file.write(config)
    print(f"Running configuration for {hostname} saved to {file_path}")
