'''
Output interpretation
'''

with open('show_ip_bgp_summary.txt') as f:
    output = f.readlines()

first_line = output[-2]
last_line = output[-1]

print(first_line)
print(last_line)

first_list = first_line.split()
as1 = first_list[2]
second_list = last_line.split()
peer2 = second_list[0]

print(as1)
print(peer2)
