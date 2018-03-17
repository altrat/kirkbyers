'''
Some description
'''

import re
import pdb

def mac_normalize(mac_string):
    # Defining delimiter
    delimiter = re.search(r"[^\w]", mac_string).group(0)
    print("Found delimiter \'" + delimiter + "\'")
    
    # Finding number of delimiters to take a decision of format of a single byte group
    delimiter_count = 0
    for char in mac_string:
        if char == delimiter:
            delimiter_count += 1

    if delimiter_count == 2:
        normal_group_size = 4
    elif delimiter_count == 5:
        normal_group_size = 2
    else:
        print("MAC address provided has wrong format. Check number of delimiters.")
        return
    
    parts_list = mac_string.split(delimiter)
    byte_list = []

    # Normalizing length of parts of provided MAC address
    parts_list_length = len(parts_list)
    for i in range(parts_list_length):
        if len(parts_list[i]) < normal_group_size:
            parts_list[i] = parts_list[i].zfill(normal_group_size)

    # New MAC string assembly
    if len(parts_list[0]) == 4:
        print("Deviding tuples into bytes")
        for item in parts_list:
            byte_list.append(item[:2])
            byte_list.append(item[2:])
    elif len(parts_list[0]) == 2:
        for item in parts_list:
            byte_list.append(item)
    else:
        print("Something went wrong. Exiting...")
        return
    
    mac_address = ":".join(byte_list).upper()
    print("MAC address is: " + mac_address)

user_input = input("Enter MAC address: ")

# Calling for debugger
pdb.set_trace()

if user_input:
    mac_normalize(user_input)
else:
    print("Error: no MAC address entered. Exiting.")
