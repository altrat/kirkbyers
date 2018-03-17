'''
Manipulating with CLI outputs
'''

with open('show_vlan.txt') as f:
    text = f.readlines()

# Cleaning up header
text.pop(0)
text.pop(0)

vlans = []

for string in text:
    if string[0] == ' ': continue
    temp_list = string.split()
    vlan_id = temp_list[0]
    vlan_name = temp_list[1]
    temp_tuple = (vlan_id, vlan_name)
    vlans.append(temp_tuple)

print(vlans)
