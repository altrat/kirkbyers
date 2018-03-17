'''
File read/write operations, using pprint (Pretty Print) function
'''

from pprint import pprint

with open('show_arp.txt') as f:
    output = f.readlines()

# Removing the header and last newstring
output.pop(0)
output.pop(-1)

output.sort()

pprint(output)
print()
# Removing incomplete ARP entries
output.pop(-1)

pprint(output)

print()
print('Creating a new string')
print()
newstring = "\n".join(output)
print(newstring)

# Writing changes to a new file
with open('arp_entries.txt', mode='w') as newfile:
    newfile.write(newstring)
