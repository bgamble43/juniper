from jnpr.junos import Device
import creds.creds_gss
import sys


def get_host_and_sn(host):
    with Device(host=host, user=creds.creds_gss.username,
                passwd=creds.creds_gss.password, normalize=True) as dev:
        # Get 'show chassis hardware' info.
        chassis = dev.rpc.get_chassis_inventory()
        # Get 'show version' info.
        # version = dev.rpc.get_software_information()
        # xpath the output to only pull FPC-related info.
        chassis_xpath = \
            chassis.xpath("//chassis-module[starts-with(name,'FPC')]")
        # Drill down a couple levels to the 'software-information' info.
        # version_xpath = version.xpath("//software-information")
        """
        Attempting to iterate over all the info collected in chassis and
        version variables, but having issues.
        So the lines below, when not commented, would get FPC name, S/N,
        description, M/N, hostname and version for each XML key in the
        variable. So when iterating over chassis/chassis_xpath you would get
        values for the first four variables then two empty values for the
        last two variables as those aren't defined in chassis/chassis_xpath.
        e.g.
        [FPC0], [HxxxxxxxxxxL], [EX Switch], [EX4600-40F], [], []
        [FPC1], [HxxxxxxxxxxX], [EX Switch], [EX4600-40F], [], []
        [],[],[],[],[HQ.Bld1.IDF2.Sw01], [18.4R2]
        [],[],[],[],[HQ.Bld1.IDF2.Sw01], [18.4R2]
        [FPC0], [HxxxxxxxxxxD], [EX Switch], [EX3400-24], [], []
        [FPC1], [H9xxxxxxxxxU], [EX Switch], [EX3400-24], [], []
        [],[],[],[],[HQ.Bld2.IDF2.Sw01], [18.4R2]
        [],[],[],[],[HQ.Bld2.IDF2.Sw01], [18.4R2]

        The goal of the script was just to obtain S/Ns, so it's still serving
        its purpose currently, but it'd be nice to fix this up as the
        additional information would be helpful/relevant for customer questions
        once the inventory is obtained.
        """
        for i in chassis_xpath:
            # print(i.xpath("name[starts-with(.,'FPC')]/text()"), end=',')
            print(i.xpath("serial-number/text()"))
            # print(i.xpath("description/text()"), end=',')
            # print(i.xpath("model-number/text()"), end=',')
            # print(i.xpath("host-name/text()"), end=',')
            # print(i.xpath("junos-version/text()"))
            # dump(i)


if __name__ == "__main__":

    with open("ip_addr_file.txt", "r") as f:
        HOSTS = f.read().splitlines()
        # print(HOSTS)

    # sys.stdout = open("output.csv", "w")
    print("S/N")
    for host in HOSTS:
        get_host_and_sn(host)

    # sys.stdout.close()
