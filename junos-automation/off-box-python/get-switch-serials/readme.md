# Get Switch Serials (Not really just switches though)
Get switch name, serial number, model number, description and JunOS version from
list of switches, firewalls and routers fed via text document.

ip_addr_file.txt is a list of IPs of switches that you want to pull data from.
One IP per line.

Creds are stored in /creds/creds_gss.py in this format:
```
# -------------------------------------------------------------
#  USERNAME TO ACCESS SWITCH
# -------------------------------------------------------------
username = "python"
# -------------------------------------------------------------
#  PASSWORD TO ACCESS SWITCH or PRIVATE KEY FILE
# -------------------------------------------------------------
password = "YippyKaiYay"
```

## Versions Used:
```
python3 --version
Python 3.7.3

pip3 list | grep junos-eznc
junos-eznc            2.4.1
```

## Scenario:
Run script against list of IPs from text file to generate simple inventory and populate CSV

## To Do

- [x] Test against physical EX virtual chassis
- [x] Test against vQFX
- [x] Test against physical SRX
- [x] Test against vMX
- [ ] Test against physical MX
- [ ] Test against physical QFX in VC
- [ ] Test against physical QFX standalone
- [ ] Test against vSRX

## Bugs
I think the Try/Except for connecting to devices could be handled better in
function 'connect_to_host'

## Sample Terminal Output
```
IP Address,Name,Model,Version,S/N
172.16.2.11,MDF-VC01,ex2300-c-12p,19.4R1-S1.2,H__________2
172.16.2.11,MDF-VC01,ex2300-c-12p,19.4R1-S1.2,H__________5
172.16.2.12,MDF-FW01,srx320,20.2R1-S2.1,C__________4
172.16.2.244: Device timeout.
172.16.2.201,NONE,vqfx-10000,18.4R1.8,6_________4
172.16.2.202,NONE,vqfx-10000,18.4R1.8,2_________0
172.16.2.203,NONE,vqfx-10000,18.4R1.8,6_________4
172.16.2.204,NONE,vqfx-10000,18.4R1.8,6_________7
172.16.2.206,LAB-vMX,vmx,19.4R1.10,V__________D
```

## Sample CSV (Identical to terminal output)
```
IP Address,Name,Model,Version,S/N
172.16.2.11,MDF-VC01,ex2300-c-12p,19.4R1-S1.2,H__________2
172.16.2.11,MDF-VC01,ex2300-c-12p,19.4R1-S1.2,H__________5
172.16.2.12,MDF-FW01,srx320,20.2R1-S2.1,C__________4
172.16.2.244: Device timeout.
172.16.2.201,NONE,vqfx-10000,18.4R1.8,6_________4
172.16.2.202,NONE,vqfx-10000,18.4R1.8,2_________0
172.16.2.203,NONE,vqfx-10000,18.4R1.8,6_________4
172.16.2.204,NONE,vqfx-10000,18.4R1.8,6_________7
172.16.2.206,LAB-vMX,vmx,19.4R1.10,V__________D
```
