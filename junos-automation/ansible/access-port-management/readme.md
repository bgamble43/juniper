## Versions Used:
```
  ansible 2.8.9
  ...
  python version = 3.7.3 (default, Dec 13 2019, 19:58:14) [Clang 11.0.0 (clang-1100.0.33.17)]
```
## Scenario:
- VLAN on switch needs changed
- either the config is blank (default vlan)
- or the config is wrong, intentionally inactive/unconfigured vlan
- or the config has changed, new device installed (was previously an IP phone, but is now a security camera)
-- this could also have a few options
-- previously trunk port, remains trunk port after change
-- previously trunk port, becomes access port after change
-- previously access port, remains access port after change
-- previously access port, becomes trunk port after change

## Automation Steps [High-level]:
1) Input switches where VLANs need to be reconfigured
2) Input ports on each switch where VLANs need to be reconfigured
3) Input new VLAN or VLANs
   If multiple VLANs defined, configure as trunk port
   If single VLAN defined, configure as access port
   Set native vlan id, if provided
4) Add interface to [protocols rstp]
5) Add interface to [poe]
4) Input port description
5) Commit Confirm
6) Commit

## To do
- [ ] Add voice vlan configuration
  - [ ] voice vlan
  - [ ] switch-options
  - [ ] forwarding-class
  - [ ] lldp-med
