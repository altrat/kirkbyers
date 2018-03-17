'''
RegExp practice
'''

import re

with open("show_version.txt") as f:
    output = f.read()

os_version = re.search(r".*, Version (\S+),", output).group(1)
serial = re.search(r".* board ID (\S+)", output).group(1)
reg_value = re.search(r".* register is (\S+)", output).group(1)

print("OS Version: " + os_version)
print("Serial Number: " + serial)
print("Config Register: " + reg_value)
