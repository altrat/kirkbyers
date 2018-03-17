'''
Working with FOR loops and netsted IF conditions
'''

with open("show_arp.txt") as f:
    output = f.readlines()

conditions = 2
condition_count = 0

for string in output:
    if not "Internet" in string:
        continue
    temp_list = string.split()
    ip_addr = temp_list[1]
    mac_addr = temp_list[3]
    if ip_addr == '10.220.88.1':
        print("Default gateway IP/MAC:")
        condition_count += 1
        print(ip_addr, mac_addr)
    elif ip_addr == '10.220.88.30':
        print("Arista3 IP/MAC is:")
        condition_count += 1
        print(ip_addr, mac_addr)

    if condition_count == conditions: break
