import requests
import json
import time

# DNA Center API endpoint
url = "https://yourdnacenter.com/dna/system/api/v1/network-device"

# API token
api_token = "your_api_token"

# List of network devices to add
devices = [
    {
        "hostname": "device1",
        "ipAddress": "10.10.10.1",
        "snmpVersion": "v2c",
        "snmpCommunity": "public",
        "cliTransport": "ssh",
        "authenticationType": "ISE",
        "authPort": "9080",
        "iseIpAddress": "10.20.30.40",
        "iseUsername": "admin",
        "isePassword": "password"
    },
    {
        "hostname": "device2",
        "ipAddress": "10.10.10.2",
        "snmpVersion": "v2c",
        "snmpCommunity": "public",
        "cliTransport": "ssh",
        "authenticationType": "ISE",
        "authPort": "9080",
        "iseIpAddress": "10.20.30.40",
        "iseUsername": "admin",
        "isePassword": "password"
    }
]

# Create a session for authentication
session = requests.Session()
headers = {'X-Auth-Token': api_token}

# Function to add a device to DNA Center
def add_device(device):
    response = session.post(url, json=device, headers=headers)
    if response.status_code == 201:
        print(f"Successfully added {device['hostname']} to DNA Center.")
        response_data = json.loads(response.text)
        task_id = response_data['response']['taskId']
        return task_id
    else:
        print(f"Failed to add {device['hostname']} to DNA Center. Error code: {response.status_code}")
        return None

# Function to check the status of a device addition using the task id
def check_status(task_id):
    status_url = f"https://yourdnacenter.com/dna/system/api/v1/task/{task_id}"
    status_response = session.get(status_url, headers=headers)
    status_data = json.loads(status_response.text)
    status = status_data['response']['isError']
    return status

# Function to cancel a device addition process using the task id
def cancel_task(task_id):
    cancel_url = f"https://yourdnacenter.com/dna/system/api/v1/task/{task_id}/cancel"
    cancel_response = session.post(cancel_url, headers=headers)

# Add each device to DNA Center and check the status
for device in devices:
    task_id = add_device(device)
    if task_id:
        time.sleep(5) # wait for 5 seconds before checking the status
        status = check_status(task_id)
    if status:
        print(f"Adding {device['hostname']} failed.")
    else:
        print(f"{device['hostname']} added successfully.")
else:
    print(f"Failed to add {device['hostname']} to DNA Center.")
    
session.close()