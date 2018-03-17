'''
Some practice with dictionaries
'''

from time import sleep

device1 = {
    'ip_addr':'172.24.1.1',
    'vendor':'cisco',
    'username':'user',
    'password':'superpassword',
    'platform':'ios'
}

bgp_fields = {
    'bgp_as':'25106',
    'peer_as':'60330',
    'peer_ip':'192.168.1.1'
}

device1.update(bgp_fields)

print("\n\nPrinting keys of the dictionary:")
print("-" * 50)
sleep(2)
for key in device1.keys():
    print(key)

print("\n\nPrinting keys and values of the dictionary:")
print("-" * 50)
sleep(2)
for key, value in device1.items():
    print(key + ':', value)
