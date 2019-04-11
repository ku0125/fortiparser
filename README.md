# fortiparser
Simple FortiGate firewall configuration file parser

It takes filename of FortiGate config file as an argument and it exports all "config firewall" sections with > 0 member count into separate .csv files

© 2019 Martin Schimmer, created in free time, distributed under GPL license, works with Python 2.7 and config files from FortiGate 5.2

Inspired by maaaaz/fgpoliciestocsv, however it's written in generic way so it just exports all sections automagically, including policies, addresses, address groups, services, service groups, etc., all that is needed to actually understand which traffic is affected by which rule
