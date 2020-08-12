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
