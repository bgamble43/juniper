#!/usr/bin/python3
#
# Populate Utility MIB w/ "show interface <int> extensive" output

'''
JunOS Config Prerequisites
set event-options generate-event FIVE_MINUTES time-interval 300
set event-options policy UTILITY_MIB_SCRIPT events FIVE_MINUTES
set event-options policy UTILITY_MIB_SCRIPT then event-script utility_mib.py
set event-options event-script file utility_mib.py python-script-user escript

Other Prerequisites
Copy file to switch using 'escript' user for auth.
e.g. scp ./utility_mib.py escript@127.127.127.127:/var/db/scripts/event/

This results in escript being the owner and allows execution of the script for that user by default
-rw-r--r--  1 escript wheel      1670 Mar 30 11:37 utility_mib.py
'''

from jnpr.junos import Device
from lxml import etree
import jcs

def main():
    dev = Device()
    dev.open()

    # Load extensive details of interface in question
    results = dev.rpc.get_interface_information(extensive="", interface_name="ge-0/0/2")

    # Pull output-bytes and input-bytes from results variable and load into new variables
    filtered_results_out = results.findtext(".//traffic-statistics/output-bytes")
    filtered_results_in = results.findtext(".//traffic-statistics/input-bytes")

    # Set jnxUtilIntegerValue.111.117.116.112.117.116.45.98.121.116.101.115 to filtered_results_out
    dev.rpc.request_snmp_utility_mib_set(object_type="integer", instance="output-bytes", object_value="%s" % filtered_results_out)

    # Set jnxUtilIntegerValue.105.110.112.117.116.45.98.121.116.101.115 to filtered_results_in
    dev.rpc.request_snmp_utility_mib_set(object_type="integer", instance="input-bytes", object_value="%s" % filtered_results_in)
    dev.close()

if __name__ == "__main__":
    main()
