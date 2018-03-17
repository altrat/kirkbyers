'''
RegExp: Excercise 2
'''

import re

with open("show_ipv6_intf.txt") as f:
    lines = f.readlines()

l = []
candidate = ''

for line in lines:
    candidate = re.search(r"[0-9a-f\:]{10,}\/\d+", line)
    if candidate:
        l.append(candidate.group(0))

print(l)
