'''
Extracting some data
'''

with open('show_lldp_neighbors_detail.txt') as f:
    lines = f.readlines()

remote_name = ''
remote_port_id = ''

for line in lines:
    if "System Name:" in line:
        temp_list = line.split()
        remote_name = temp_list[-1]
    elif "Port id:" in line:
        temp_list = line.split()
        remote_port_id = temp_list[-1]
    if remote_name and remote_port_id:
        break

print(remote_name, remote_port_id)
