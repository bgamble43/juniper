# Get Interface State
Show interface speed, duplex, mtu, input/output rate, and errors
Option to sort interfaces by highest input rate
Option to sort interfaces by highest output rate secondarily

## Versions Used:
```
  ansible 2.8.9
  ...
  python version = 3.7.3 (default, Dec 13 2019, 19:58:14) [Clang 11.0.0 (clang-1100.0.33.17)]
```
```
Name: junos-eznc
Version: 2.4.1
```
## Scenario:
Quickly run script to check for anomalies in the form of incorrect speeds, b0rk3d mtus, wonky duplex settings, high input/output, and errors.

## To Do
- [x] Add duplex
- [x] Add interface description
- [x] Add errors
- [x] Format output
- - [x] Column headers
- - [x] Multiple interface stats without individual task headers breaking up the output
- [x] Handle not knowing the number of interfaces on the switch
- [ ] Handle not knowing the naming convention of the interfaces (ge-, et-, etc.)

## Bugs
- [x]Iterations aren't handling absent nodes properly. Instead of having blank entries for things like description, speed, or duplex, if those values aren't defined or if the interface is down/off and the value is empty (doesn't exist in the XML output) the entry is blank, so when I iterate over that sequentially the values "higher up" in the list end up getting squashed down and thus the output is invalid.

Solution: Used -- | default('') -- to default to no value in the case the value doesn't exist in the XML string, which would've overwise thrown an error.

## Sample Output
```
sudo ansible-playbook gis.yml -i hosts

PLAY [GET INTERFACE STATS] *********************************************************************************************************************************

TASK [GET INTERFACE STATS via RPC] *************************************************************************************************************************
[WARNING]: The value {'interface_name': 'ge-0/0/*', 'extensive': True} (type dict) in a string field was converted to "{'interface_name': 'ge-0/0/*',
'extensive': True}" (type string). If this does not look like what you expect, quote the entire value to ensure it does not change.

ok: [switch1.domain.com]

TASK [DETERMINE LENGTH OF DICTIONARY] **********************************************************************************************************************
ok: [switch1.domain.com]

TASK [LOAD CLEAN OUTPUT VARIABLE] **************************************************************************************************************************
ok: [switch1.domain.com] => (item=0)
ok: [switch1.domain.com] => (item=1)
ok: [switch1.domain.com] => (item=2)
ok: [switch1.domain.com] => (item=3)
ok: [switch1.domain.com] => (item=4)
ok: [switch1.domain.com] => (item=5)
ok: [switch1.domain.com] => (item=6)
ok: [switch1.domain.com] => (item=7)
ok: [switch1.domain.com] => (item=8)
ok: [switch1.domain.com] => (item=9)
ok: [switch1.domain.com] => (item=10)
ok: [switch1.domain.com] => (item=11)

TASK [DISPLAY INTERFACE STATUS WITH COLUMN HEADERS] ********************************************************************************************************
ok: [switch1.domain.com] =>
  msg:
  - 'Interface:     Description:           Admin:   Oper:    Speed:       Duplex:        MTU:     Input(bps):  Output(bps): Input errors:  Output errors:'
  - 'ge-0/0/0       Home Office PC Uplink  up       up       1000 Mbps    full-duplex    1514     2104         2888         0              0              '
  - 'ge-0/0/1       Security Cam           up       up       100 Mbps     full-duplex    1514     0            552          0              0              '
  - 'ge-0/0/2       Access Point       up       up       1000 Mbps    full-duplex    1514     28376        35144        0              0              '
  - 'ge-0/0/3       Printer                down     down                                 1514     0            0            0              0              '
  - 'ge-0/0/4                              up       down                                 1514     0            0            0              0              '
  - 'ge-0/0/5                              up       down                                 1514     0            0            0              0              '
  - 'ge-0/0/6                              up       down                                 1514     0            0            0              0              '
  - 'ge-0/0/7       Wired port             up       down                                 1514     0            0            0              0              '
  - 'ge-0/0/8       Office Phone           up       down                                 1514     0            0            0              0              '
  - 'ge-0/0/9       Access point           up       down                                 1514     0            0            0              0              '
  - 'ge-0/0/10      Lab Server iLo         up       down                                 1514     0            0            0              0              '
  - 'ge-0/0/11      MDF-Sw01               up       up       1000 Mbps    full-duplex    1514     66384        59480        0              0              '
  - ''

PLAY RECAP *************************************************************************************************************************************************
switch1.domain.com         : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
