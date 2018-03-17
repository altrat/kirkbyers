'''
Experimenting with lists
'''

print('STAGE 1 - Empty list')
print('====================')
ip_addresses = []
print(ip_addresses)

print('STAGE 2 - Adding a single address')
print('=================================')
ip_addresses.append('192.168.1.1')
print(ip_addresses)

print('STAGE 3 - Adding a list of addresses to the end of the current list')
print('===================================================================')
ip_addresses.extend(['172.16.1.1', '10.128.77.2'])
print(ip_addresses)

print('STAGE 4 - List concatenation')
print('============================')
ip_addresses += ['172.31.255.255', '172.25.16.24']
print(ip_addresses)

print('STAGE 5 - Reading separate items')
print('================================')
print('Reading the FIRST item of the list')
print(ip_addresses[0])
print('Reading the LAST item of the list')
print(ip_addresses[-1])

print('STAGE 6 - Popping list elements')
print('===============================')
print('Pop the FIRST item:')
print(ip_addresses.pop(0))
print('Pop the LAST item:')
print(ip_addresses.pop(-1))

print('STAGE 7 - Modifying list items')
print('==============================')
ip_addresses[0] = '2.2.2.2'
print(ip_addresses)
