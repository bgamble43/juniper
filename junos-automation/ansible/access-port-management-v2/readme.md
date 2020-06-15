# Access Port Manager
Ansible script to change VLANs on access ports.

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
-- possibility of the above situations will result in stanza'd config file where we delete config that doesn't exist in current active config. e.g. if "poe" is set to "no" in host_vars file then we'll delete the poe config, but if that config didn't exist in the first place it'll toss an error. We'll handle this with a specific "ignore_warning" argument.

## Automation Steps [High-level]:
1) Create host_vars files for switches where VLANs need to be reconfigured
-- host_vars contains:
-- ports on each switch where VLANs need to be reconfigured
-- new VLAN or VLANs to be configured
-- -- If multiple VLANs defined, configure as trunk port
-- -- If single VLAN defined, configure as access port
-- -- Set native vlan id, if provided
-- voice_vlan if any
-- poe power required or notify
-- native vlan id
-- description
2) Using host_vars, iterate over j2 templates to do the following:
-- add interface to [protocols rstp], edge, no-root-port
-- if poe port add interface to [poe] and [protocols lldp, lldp-med]
-- if voice_vlan defined then add appropriate [switch-option] config, assured forwarding (not EF?)
-- set native vlan id
-- set interface description
3) Commit Confirm, notify the commit handler
4) [handler] Commit

## To do
- [x] Add voice vlan configuration
  - [x] voice vlan
  - [x] switch-options
  - [x] forwarding-class
  - [x] lldp-med

## Note
This was a second attempt at the Access Port Manager script using only stanza'd config. I found the "delete" option so I didn't have to use "set" commands. Thanks to the "Day One: Automating JunOS with Ansible, 2nd Edition" book.
