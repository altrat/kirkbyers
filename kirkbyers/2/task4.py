'''
Output interpretation
'''

with open('show_ip_interface_brief.txt') as f:
    output = f.readlines()

# Getting an interface
interface = output[7]

interface_details = interface.split()

t = (interface_details[0], interface_details[1])
print(t)
