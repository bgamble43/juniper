#!/usr/bin/python3
#
# Query Mist Switch metrics from CLI
#
# To Do: Allow user to enter switch name and pull metrics for that switch based on MAC or Switch ID

import requests
import json
import base64
from base64 import b64encode
import getpass

def main():
    # Username
    u = None
    # Password
    p = None
    # Mist Org ID
    oid = None
    # Mist Site ID
    sid = None
    # Mist Switch ID
    swid = None

    # Get username
    if u == None:
        try:
        	u = input("Username: ")
        except Exception as error:
        	print("An error occured: %s" % str(error))
        else:
        	print("Username stored")
    else:
        print("Using preconfigured username")

    # Get password
    if p == None:
        try:
        	p = getpass.getpass()
        except Exception as error:
        	print("An error occured: %s" % str(error))
        else:
        	print("Password stored")
    else:
        print("Using preconfigured password")

    #Get OrgID
    if oid == None:
        try:
        	oid = input("Org ID: ")
        except Exception as error:
        	print("An error occured: %s" % str(error))
        else:
        	print("Org ID stored")
    else:
        print("Using preconfigured Org ID")

    # Get SiteID
    if sid == None:
        try:
        	sid = input("Site ID: ")
        except Exception as error:
        	print("An error occured: %s" % str(error))
        else:
        	print("Site ID stored")
    else:
        print("Using preconfigured Site ID")

    # Get Switch Name
    if swid == None:
        try:
            swid = input("Switch Name: ")
        except Exception as error:
            print("An error occured: %s" % str(error))
        else:
            print("Switch name stored")
    else:
        print("Using preconfigured Switch name")

    """
    # Get Switch ID
    if swid == None:
        try:
            sid = input("Switch ID: ")
        except Exception as error:
            print("An error occured: %s" % str(error))
        else:
            print("Switch ID stored")
    else:
        print("Using preconfigured Switch ID")
    """
    # Gather switch facts based on entered switch name (swn)
    org_inventory = requests.get('https://api.mist.com/api/v1/orgs/'+oid+'/inventory?mac=c003809f360f', auth=(u, p))
    org_inventory_json = json.loads(org_inventory.text)
    print(org_inventory.text)
    for list_item in org_inventory_json:
        for key, value in list_item.items():
            print (key, value)


    # Gather switch CPU data, swid is switch MAC address
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/cpu', auth=(u, p))
    resultsjson = json.loads(results.text)
    # results = resultsjson['results']
    # print(results)
    # print(results.text)
    # print(" --- ")
    # print(results.json())
    # print(" --- ")
    # print(resultsjson['max_cpu'])
    results_max_cpu = resultsjson['max_cpu']
    results_avg_cpu = resultsjson['avg_cpu']

    # Gather switch memory data, swid is switch MAC address
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/memory', auth=(u, p))
    resultsjson = json.loads(results.text)
    results_max_memory = resultsjson['max_memory']
    results_avg_memory = resultsjson['avg_memory']

    # Gather switch TX/RX data, swid is switch MAC address
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/tx_bytes', auth=(u, p))
    resultsjson = json.loads(results.text)
    results_results_tx_bytes = resultsjson['results']
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/rx_bytes', auth=(u, p))
    resultsjson = json.loads(results.text)
    results_results_rx_bytes = resultsjson['results']
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/port_tx_errors', auth=(u, p))
    resultsjson = json.loads(results.text)
    results_results_port_tx_errors = resultsjson['results']
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/port_rx_errors', auth=(u, p))
    resultsjson = json.loads(results.text)
    results_results_port_rx_errors = resultsjson['results']
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/power_draw', auth=(u, p))
    resultsjson = json.loads(results.text)
    results_max_power_draw = resultsjson['max_power_draw']
    # results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/insights/switch/'+swid+'/power_draw', auth=(u, p))
    # resultsjson = json.loads(results.text)
    results_avg_power_draw = resultsjson['avg_power_draw']

    print("CPU Utilization % [Max / Avg]",results_max_cpu[23],"/",results_avg_cpu[23])
    print("Memory Used     % [Max / Avg]",results_max_memory[23],"/",results_avg_memory[23])
    print("TX Bytes                     ",results_results_tx_bytes[23])
    print("RX Bytes                     ",results_results_rx_bytes[23])
    print("Port TX Errors               ",results_results_port_tx_errors[23])
    print("Port RX Errors               ",results_results_port_rx_errors[23])
    print("Power Draw        [Max / Avg]",results_max_power_draw[23],"/",results_avg_power_draw[23])

if __name__ == "__main__":
    main()
