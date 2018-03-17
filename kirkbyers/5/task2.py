'''
Some description
'''

from random import randint

def generate_ip(base='10.10.10.'):
    print("Using base " + base)
    last_octet = randint(0, 256)
    print(base + str(last_octet))

print("Prefix /24 is being used.")
base = input("Enter base (10.10.10.0/24 is used by default):")

print("You entered " + base)

if base:
    generate_ip(base)
else:
    generate_ip()
