import requests
import json

# ISE API endpoint
url = "https://yourise.com:9060/ers/config/networkdevice"

# ISE API token
api_token = "your_api_token"

# List of network devices to add
devices = [
    {
        "name": "device1",
        "description": "Test Device 1",
        "ipAddress": "10.10.10.1"
    },
    {
        "name": "device2",
        "description": "Test Device 2",
        "ipAddress": "10.10.10.2"
    }
]

# Create a session for authentication
session = requests.Session()
headers = {'Authorization': "Bearer "+api_token}

# Function to add a device to ISE
def add_device(device):
    response = session.post(url, json=device,headers=headers)
    if response.status_code == 201:
        print(f"Successfully added {device['name']} to ISE.")
    else:
        print(f"Failed to add {device['name']} to ISE. Error code: {response.status_code}")

# Add each device to ISE
for device in devices:
    add_device(device)

# Close the session
session.close()
