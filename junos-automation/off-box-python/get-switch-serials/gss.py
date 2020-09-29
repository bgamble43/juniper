import os
from jnpr.junos import Device
from jnpr.junos.exception import *
import creds.creds_gss


def connect_to_host(host):
    """
    Connect to Device from IP file and issue two commands:
        show chassis hardware
        show version
    """
    # Connect to device using contextual whatevertheheck
    try:
        # auto_probe tries NETCONF port for 5 seconds before timing out
        with Device(host=host, user=creds.creds_gss.username,
                    passwd=creds.creds_gss.password, auto_probe=5,
                    normalize=True) as dev:
            # Get 'show chassis hardware' info.
            chassis = dev.rpc.get_chassis_inventory()
            # Get 'show version' info.
            version = dev.rpc.get_software_information()
        # Return these two variables to Main
        return chassis, version
    # If a connection can't be made let the terminal know.
    except (ProbeError, ConnectError):
        print(host+": Device timeout.")


def get_host_info(chassis, version):
    """
    Load data into variables using xpath run on the 'chassis' and 'version'
    variables that were set in the 'connect_to_host' function
    So far all platforms tested storm the data we want at the same path in the
    'show version' output
    """
    #
    # ====== Load host-name, model number and JunOS version ======
    #
    # set to host-name value of element at this path
    list_of_device_name = version.xpath("//host-name/text()")
    # set to model number value of element at this path
    list_of_mn = version.xpath("//product-model/text()")
    # set to version value of element at this path
    list_of_version = version.xpath("//junos-version/text()")

    #
    # ====== Load serial number ======
    #
    # --- Tested against: Physical EX, vQFX ---
    #
    # Virtual-chassis-capable devices have a multi-routing-engine-item
    # element
    # If multi-routing-engine-item exists, start populating lists
    if version.xpath("//multi-routing-engine-item"):
        # Determine how many switches are in stacik if any.
        length = len(version.xpath("//multi-routing-engine-item"))
        # Physical EX in an active VC used this path for serial number
        if chassis.xpath("//chassis-module[starts-with(name,\
                                   'FPC')]/serial-number/text()"):
            # set to serial number of element at this path
            list_of_sn = chassis.xpath("//chassis-module[starts-with(name,\
                                       'FPC')]/serial-number/text()")
        # vQFX not in an active VC used this path for serial number
        else:
            # set to serial number of element at this path
            list_of_sn = chassis.xpath("//chassis/serial-number/text()")
        return list_of_device_name, list_of_mn, list_of_version,\
            list_of_sn, length
    #
    # --- Tested against: vMX ---
    #
    # Check to see if the product-model is a vMX instance
    # The path to serial number is at the chassis level and not the
    # chassis-module.
    # And we can't just check for the existence of a S/N to determine
    # if we're checking the right path as some elements have 'BUILTIN' for
    # the serial number
    elif version.xpath("//software-information/product-model[contains(.,'mx')]\
                       /text()"):
        # since length was not set at the beginning of this function as there
        # is no multi-routing-engine-item value, manually set to 1 so that
        # value is returned to Main and loop indexes are processed properly
        length = 1
        # set to serial-number value of element at this path
        # Physical SFX used this path for serial number
        list_of_sn = chassis.xpath("//chassis/serial-number/text()")
        return list_of_device_name, list_of_mn, list_of_version,\
            list_of_sn, length
    #
    # --- Tested against: Physical SRX ---
    #
    # If multi-routing-engine-item doesn't exist and not a vMX then load
    # single item lists
    # The path to the serial number is different on devices that don't support
    # virtual chassis
    else:
        # since length was not set at the beginning of this function as there
        # is no multi-routing-engine-item value, manually set to 1 so that
        # value is returned to Main and loop indexes are processed properly
        length = 1
        # set to serial-number value of element at this path
        # Physical SFX used this path for serial number
        list_of_sn = chassis.xpath("//chassis-module[starts-with(name,\
                                'Routing Engine')]/serial-number/text()")
        return list_of_device_name, list_of_mn, list_of_version,\
            list_of_sn, length


def print_host_info(list_of_device_name, list_of_mn, list_of_version,
                    list_of_sn, length, host):
    """
    Print host info to terminal
    Receive several variables from main via 'get_host_info' function.
    This data will be a list, either with one element in the event of a
    device that doesn't support VC, or a device that does support VC but is
    standalone; or it will be a list with several items in the event of an
    active VC.
    """
    # 'length' is passed from main, and is set to the number of
    # 'multi-routing-engine-item' values that occur in the output of the
    # 'show version' RPC. If the RPC doesn't have any 'multi-routing-engine-
    # item values, then this would be zero, so we set it to 1 manually in the
    # 'get_host_info' function if need be.
    for i in range(length):
        # print IP address of current host iteration, end w/ command instead of
        # newline
        print(host, end=",")
        # print device hostname
        try:
            print(list_of_device_name[i], end=",")
        # handle empty hostname exception
        except IndexError:
            print("NONE", end=",")
        # print device model number
        print(list_of_mn[i], end=",")
        # print device JunOS version
        print(list_of_version[i], end=",")
        # print device serial number
        print(list_of_sn[i])


def write_host_info_csv(list_of_device_name, list_of_mn, list_of_version,
                        list_of_sn, length, host):
    """
    Write host info to file
    Receive several variables from main via 'get_host_info' function.
    This data will be a list, either with one element in the event of a
    device that doesn't support VC, or a device that does support VC but is
    standalone, or it will be a list with several items in the event of an
    active VC.
    """
    # 'length' is passed from main, and is set to the number of
    # 'multi-routing-engine-item' values that occur in the output of the
    # 'show version' RPC. If the RPC doesn't have any 'multi-routing-engine-
    # item values, then this would be zero, so we set it to 1 manually in the
    # 'get_host_info' function if need be.
    for i in range(length):
        # write IP address of current host iteration to host_info.csv
        output.writelines(host)
        # separate lines written with comma
        output.writelines(",")
        # write device hostname to file
        try:
            output.writelines(list_of_device_name[i])
        # handle empty host name exception
        except IndexError:
            output.writelines("NONE")
        output.writelines(",")
        # write device model number to file
        output.writelines(list_of_mn[i])
        output.writelines(",")
        # write device JunOS version to file
        output.writelines(list_of_version[i])
        output.writelines(",")
        # write device serial number to file
        output.writelines(list_of_sn[i])
        # write newline so iterations are written to separate lines in csv
        output.writelines("\n")


if __name__ == "__main__":
    output_file = "output/host_info.csv"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Open/create 'host_info.csv' for writing.
    output = open(output_file, "w")

    # Open file for reading containing list of IPs to query
    with open("input/ip_addr_file.txt", "r") as f:
        # Read each line of file into separate list item
        HOSTS = f.read().splitlines()
    # Print header
    print("IP Address,Name,Model,Version,S/N")
    # Write header to file
    output.writelines("IP Address,Name,Model,Version,S/N\n")
    # For each IP in file do this:
    for host in HOSTS:
        # Connect to host and get 'show chassis hardware' and 'show version'
        # info
        try:
            version, chassis = connect_to_host(host)
        # Lazy way to handle not being able to connect to device.
        # When that happens no data is sent back to 'main' resulting in
        # 'TypeError: cannot unpack non-iterable NoneType object'.
        # So I just excepted it until I can figure a better way to handle this.
        except (TypeError):
            continue
        # Pass 'version' and 'chassis' to function and load values into lists.
        # Return device name, model number, version and serial number to main.
        # Return length of 'multi-routing-engine-item' so we can iterate over
        # list in 'print_host_info' and 'write_host_info' functions.
        list_of_device_name, list_of_mn, list_of_version, list_of_sn, length =\
            get_host_info(version, chassis)
        # Print output to the terminal
        print_host_info(list_of_device_name, list_of_mn, list_of_version,
                        list_of_sn, length, host)
        # Write output to file
        write_host_info_csv(list_of_device_name, list_of_mn, list_of_version,
                            list_of_sn, length, host)

    output.close()
