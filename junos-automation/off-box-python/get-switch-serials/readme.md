# Get Switch Serials
Get switch name, serial number, model number, description and JunOS version from
list of switches fed via text document.

ip_addr_file.txt is a list of IPs of switches that you want to pull data from.
One IP per line.

Creds are stored in /creds/creds_gss.py in this format:
```
# -------------------------------------------------------------
#  USERNAME TO ACCESS SWITCH
# -------------------------------------------------------------
username = "python"
# -------------------------------------------------------------
#  PASSWORD TO ACCESS SWITCH
# -------------------------------------------------------------
password = "PytH0n!"
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

- [ ] Test against virtual chassis

## Bugs

## Sample Output
```
python3 gss.py
['172.16.1.1', '172.16.1.2', '172.16.1.3', '172.16.1.4']
```

## Sample CSV
```
Name,Module,Serial,Model,Description,Version
IDF-Sw01,FPC 0,HA0123456789,EX2300-C-12P,EX2300-C-12P,19.4R1-S1.2
IDF-Sw02,FPC 0,HA1234567890,EX2300-C-12P,EX2300-C-12P,19.4R1-S1.2
IDF-Sw03,FPC 0,HA2345678901,EX2300-C-12P,EX2300-C-12P,19.4R1-S1.2
IDF-Sw04,FPC 0,HA3456789012,EX2300-C-12P,EX2300-C-12P,19.4R1-S1.2
```
## Current Debugging Output
```
S/N
['HxxxxxxxxxxA']
['HxxxxxxxxxxB']
['HxxxxxxxxxxC']
['HxxxxxxxxxxD']
```
