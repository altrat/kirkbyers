'''
Brief environment availability check
'''

import os

base = "10.10.100."
ip_addresses = []

for i in range(1, 255):
    ip_addresses.append(base + str(i))
    print(str(i-1) + " ---> " + ip_addresses[i-1])

ip_addresses_part = ip_addresses[2:6]
print(ip_addresses_part)

for ip in ip_addresses_part:
    os.system("ping -c 1 -W 1 " + ip)
