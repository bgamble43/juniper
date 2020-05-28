#!/usr/bin/python3
#
# Query Mist Site SLEs from CLI

import requests
import json
import base64
from base64 import b64encode
import getpass

def main():
    #
    #
    # username = 'XXXXXXXXXX'
    # password = 'XXXXXXXXXX'
    oid = None
    sid = None


    #GET /api/v1/sites/:site_id/insights/client/:mac/:metric
    #/api/v1/const/insight_metrics     insights/client/dc080f39945f/
    #/api/v1/sites/'+site+'/alarms/search
    #
    #GET /api/v1/sites/:site_id/alarms/search
    #GET /api/v1/sites/:site_id/alarms/count

    # Get username
    try:
    	u = input("Username: ")
    except Exception as error:
    	print("An error occured: %s" % str(error))
    else:
    	print("Username stored")

    # Get password
    try:
    	p = getpass.getpass()
    except Exception as error:
    	print("An error occured: %s" % str(error))
    else:
    	print("Password stored")

    #Get OrgID
    if oid == None:
        try:
        	oid = input("Org ID: ")
        except Exception as error:
        	print("An error occured: %s" % str(error))
        else:
        	print("Org ID stored")
    else:
        print("Using pre-configured Org ID")

    # Get SiteID
    if sid == None:
        try:
        	sid = input("Site ID: ")
        except Exception as error:
        	print("An error occured: %s" % str(error))
        else:
        	print("Site ID stored")
    else:
        print("Using pre-configured Site ID")

    # Display alarms count
    results = requests.get('https://api.mist.com/api/v1/sites/'+sid+'/alarms/count', auth=(u, p))

    alarms = json.loads(results.text)
    print("Alarms Active:" ,alarms["total"])

    # Wireless SLEs
    # Gather wireless SLE data
    results = requests.get('https://api.mist.com/api/v1/orgs/'+oid+'/insights/sites-sle', auth=(u, p))
    resultsjson = json.loads(results.text)
    results = resultsjson['results']

    # Print wireless SLE data
    print ("==============    WIRELESS  SLE      ==============")

    #print(json.dumps(resultsjson, indent=4, sort_keys=True))

    if results[0]:
        print("AP Availability       ",results[0]['ap-availability'])
        print("Capacity              ",results[0]['capacity'])
        print("Coverage              ",results[0]['coverage'])
        print("Roaming               ",results[0]['roaming'])
        print("Successful Connect    ",results[0]['successful-connect'])
        print("Throughput            ",results[0]['throughput'])
        print("Time to Connect       ",results[0]['time-to-connect'])

    # Gather wired metrics data
    results = requests.get('https://api.mist.com/api/v1/orgs/'+oid+'/insights/sites-wa-metrics', auth=(u, p))
    resultsjson = json.loads(results.text)
    results = resultsjson['results']

    # Print wired metrics data
    print ("=========     WIRED ASSURANCE METRICS     =========")

    if results[0]:
        print("Switch/AP Affinity    ",results[0]['switch_ap_affinity'])
        print("Total AP Count        ",results[0]['total_ap_count'])
        print("Total Power Draw      ",results[0]['total_power'])
        print("PoE Compliance        ",results[0]['poe_compliance'])
        print("Total Switch Count    ",results[0]['total_switch_count'])
        print("Version Compliance    ",results[0]['version_compliance'])
        print("Inactive Wired VLANs  ",results[0]['inactive_wired_vlans'])

    results = requests.get('https://api.mist.com/api/v1/orgs/'+oid+'/insights/sites-sle', auth=(u, p))
    resultsjson = json.loads(results.text)
    results = resultsjson['results']

    # Gather wireless SLE data
    print("==============     OTHER INFO      =================")

    #print(json.dumps(resultsjson, indent=4, sort_keys=True))

    # Print other info not specifically related to a wireless SLE
    if results[0]:
        print("Registered APs        ",results[0]['num_aps'])
        print("Client Count          ",results[0]['num_clients'])

if __name__ == "__main__":
    main()
