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
