from jnpr.junos import Device
from myTables.chassisTables import ShowChassisHardwareTable
from myTables.versionTables import ShowVersionTable
import creds.creds_gss
import sys

# HOSTS = open("ip_addr_file.txt", "r")
# HOST_ADDRESSES = [HOSTS.readlines()]
# HOST_ADDRESSES = HOST_ADDRESSES.split(",")


def get_host_and_sn(host):
    with Device(host=host, user=creds.creds_gss.username, passwd=creds.creds_gss.password) as dev:
        host_chassis_hw = ShowChassisHardwareTable(dev)
        # print(host_chassis_hw)
        host_version_name = ShowVersionTable(dev)
        # print(host_version_name)
        host_chassis_hw.get()
        host_version_name.get()

        for name in host_version_name:
            print("{}".format(name.hostname), end=',')
            for entry in host_chassis_hw:
                print("{},{},{},{}".format(entry.fpc_name, entry.fpc_sn, entry.fpc_mn, entry.fpc_desc), end=',')
            print("{}".format(name.version))


if __name__ == "__main__":

    with open("ip_addr_file.txt", "r") as f:
        HOSTS = f.read().splitlines()
        print(HOSTS)

    sys.stdout = open("output.csv", "w")
    print("Name,Module,Serial,Model,Description,Version")
    for host in HOSTS:
        get_host_and_sn(host)
    sys.stdout.close()
