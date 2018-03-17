'''
Working with file in RO mode
'''

print("Option 1: just opening file for reading")
print("=======================================")

f = open("show_version.txt")
output = f.read()
f.close()

print(output)
print(type(output))

print("Option 2: commonly used way to open files (via Context Manager)")
print("===============================================================")

with open("show_version.txt") as f:
    output = f.readlines()

print(output)
print(type(output))
