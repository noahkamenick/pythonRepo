import requests
import json
import requests
import sys
from argparse import ArgumentParser
from collections import OrderedDict
from requests import exceptions
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


# shutdown_int('Loopback100') # since I import this file to the next challenge

def get_cpu():
    url = url_base + "/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/five-seconds"

    # This statement performs a GET on the specified URL

    response = requests.get(url,
                            auth=(USER,PASS),
                            headers=headers,
                            verify=False
                            )
    # Return JSON as text
    # print(url)
    return response.json()['Cisco-IOS-XE-process-cpu-oper:five-seconds']

print('CPU Usage:', get_cpu())

# Retrieve memory on device

def get_mem():

    url = url_base + "/data/Cisco-IOS-XE-memory-oper:memory-statistics/memory-statistic=Processor"

    # Perform a GET statement on the URL

    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

    data = response.json()["Cisco-IOS-XE-memory-oper:memory-statistic"]
    # return json as text

    print("Name: ", data["name"])
    used, free = 0,0

    try:
        used = int(data["used-memory"])
        free = int(data["free-memory"])
        total = int(data["total-memory"])
    except KeyError:
        print("Json Error")
    print()

    #return the json as text

    tot = 2130017008/1000000 # Calc in MB

    return (used/(used+free)) * 100, (free/(used+free)) * 100, str(tot)


# print("PercentFree/PercentUsed/TotalMemoryInMegabytes", get_mem())

def get_int_state():
    url = url_base + "/data/ietf-interfaces:interfaces-state/interface=Loopback1"

    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

    interInfo = response.json()["ietf-interfaces:interface"]
    interStats = interInfo["statistics"]

    int_state = f"""
    
    {interInfo["name"]} Interface State
    -----------------------

    Speed: {interInfo["speed"]}
    MAC Address: {interInfo["phys-address"]}
    Discontinuity Time: {interStats["discontinuity-time"]}
    In-Octets: {interStats["in-octets"]}
    In-Unicast-Packets: {interStats["in-unicast-pkts"]}
    In-Broadcast-Packets: {interStats["in-broadcast-pkts"]}
    In-Multicast-Packets: {interStats["in-multicast-pkts"]}
    Out-Octets: {interStats["out-octets"]}
    Out-Unicast-Packets: {interStats["out-unicast-pkts"]}

    """

    return int_state

print(get_int_state())