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
## Scenario:
Quickly run script to check for anomalies in the form of incorrect speeds, b0rk3d mtus, wonky duplex settings, high input/output, and errors.

## To Do
- [ ] Add duplex
- [ ] Add errors
- [ ] Format output
 - [ ] Column headers
 - [ ] Multiple interface stats without individual task headers breaking up the output
- [ ] Find better methods of iteration
 - [ ] Handle not knowing the number of interfaces on the switch
 - [ ] Handle not knowing the naming convention of the interfaces (ge-, et-, etc.)
