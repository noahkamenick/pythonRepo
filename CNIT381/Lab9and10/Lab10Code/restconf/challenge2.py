import json
import requests
import sys
from argparse import ArgumentParser
from collections import OrderedDict
from requests.api import head
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Router connection
HOST = '192.168.56.102'
PORT = '443'
USER = 'cisco'
PASS = 'cisco123!'

# Management Int
# Specified to ensure the script doesn't change the IP of the interface specified for management
MANAGEMENT_INTERFACE = "GigabitEthernet1"

# Base URL for RESTCONF Calls
url_base = "https://{h}/restconf".format(h=HOST)

# Identify yang+json as the data formats
headers = {'Content-Type':'application/yang-data+json',
           'Accept':'application/yang-data+json'}

# get_interfaces() to retrieve a list of interfaces on a device

def get_interfaces():
    url = url_base + "/data/ietf-interfaces:interfaces"

    # Perform a GET request on a specific URL
    response = requests.get(url, auth=(USER,PASS), headers=headers, verify=False)

    # Return the json as text
    print(url)
    return response.json()["ietf-interfaces:interfaces"]["interface"]

# print(json.dumps(get_interfaces(), indent=4, sort_keys=True)) # Run function and PrettyPrint JSON

def shutdown_int(interface):
    # RESTCONF URL for specific interface
    url = url_base + "/data/ietf-interfaces:interfaces/interface={i}".format(i=interface)

    type = 'iana-if-type:ethernetCsmacd'
    if 'Loopback' in interface:
        type = 'iana-if-type:softwareLoopback'
    
    # Create the data payload to disable the interface
    # Need to use OrderedDicts to maintain the order of elements

    data = OrderedDict([('ietf-interfaces:interface', 
                OrderedDict([
                        ('name', interface),
                        ('type', type),
                        ('enabled', False) # shutdown int
                  ])
                )])
    # Use PUT to update data
    response = requests.put(url, auth=(USER, PASS), headers=headers, verify=False, json=data)

    print(url)

    print(response.text)


# shutdown_int('Loopback1')
 