#!/usr/bin/python3
#
# Populate Utility MIB w/ "show interface <int> extensive" output

from jnpr.junos import Device
from lxml import etree
import jcs

if __name__ == "__main__":
    with Device() as dev:
        # Load extensive details of interface in question
        results = dev.rpc.get_interface_information(extensive="", interface_name="ge-0/0/2")
        # Pull output-bytes and input-bytes from results variable and load into new variables
        filtered_results_out = results.findtext(".//traffic-statistics/output-bytes")
        filtered_results_in = results.findtext(".//traffic-statistics/input-bytes")
        # Print output-bytes to session
        '''
        would like the following output to be one line
        '''
        jcs.output("Output Bytes:", filtered_results_out)
        # Set jnxUtilIntegerValue.111.117.116.112.117.116.45.98.121.116.101.115 to filtered_results_out
        dev.rpc.request_snmp_utility_mib_set(object_type="integer", instance="output-bytes", object_value="%s" % filtered_results_out)
        # Print input-bytes to session
        '''
        would like the following output to be one line
        '''
        jcs.output("Input Bytes:", filtered_results_in)
        # Set jnxUtilIntegerValue.105.110.112.117.116.45.98.121.116.101.115 to filtered_results_in
        dev.rpc.request_snmp_utility_mib_set(object_type="integer", instance="input-bytes", object_value="%s" % filtered_results_in)
        print("*** End of Script ***")
