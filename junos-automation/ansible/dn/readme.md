# DNS and NTP
Ansible script to set DNS and NTP servers.

## Versions Used:
```
  ansible 2.8.9
  ...
  python version = 3.7.3 (default, Dec 13 2019, 19:58:14) [Clang 11.0.0 (clang-1100.0.33.17)]
```
## Scenario:
Update DNS and NTP servers on group of devices.

## Automation Steps [High-level]:
Create config directories.
Create config stanzas.
Concatenate config stanzas.
Apply config stanzas.
Print diff.
Remove config directories.

## To do
Could probably consolidate into a single stanza since both config elements
exist within the system hierarchy.

## Note