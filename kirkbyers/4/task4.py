'''
Some description
'''

import re

# Sample string
show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

match1 = re.search(r"Cisco (?P<model>\S+) .*", show_version)
match2 = re.search(r"with (?P<memory>\S+) .*", show_version)

print(match1.groupdict())
print(match2.groupdict())

