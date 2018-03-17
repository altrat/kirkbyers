'''
Working with data structures
'''

# Defining lists
houston = [
    '10.124.19.248',
    '10.254.110.187',
    '10.197.217.229',
    '10.212.144.37',
    '10.171.137.214',
    '172.29.179.170',
    '172.21.128.90',
    '172.17.246.67',
    '172.25.221.142',
    '10.207.231.115',
    '192.168.193.60',
    '192.168.202.23',
    '192.168.5.204',
    '192.168.99.158',
    '192.168.231.241',
    '192.168.250.21',
    '192.168.143.131'
]

atlanta = [
    '192.168.61.128',
    '192.168.12.228',
    '192.168.64.165',
    '192.168.136.49',
    '192.168.193.60',
    '172.20.30.128',
    '172.19.181.224',
    '172.21.244.79',
    '172.25.58.89',
    '172.30.68.122',
    '10.82.64.55',
    '10.18.2.165',
    '10.232.8.213',
    '10.114.190.180',
    '10.110.0.255',
    '10.103.40.60'
]

chicago = [
    '10.173.164.173',
    '10.180.128.227',
    '10.130.17.92',
    '10.113.153.171',
    '172.20.145.225',
    '172.19.202.126',
    '172.31.197.94',
    '172.20.159.58',
    '172.21.225.224',
    '192.168.61.128',
    '192.168.12.228',
    '192.168.64.165',
    '192.168.136.49',
    '192.168.193.60',
    '192.168.202.23',
    '192.168.5.204',
    '192.168.99.158',
    '192.168.231.241',
    '192.168.250.21',
    '192.168.143.131',
    '192.168.85.82',
    '192.168.24.215',
    '192.168.173.74'
]

# Converting to sets
set_chicago = set(chicago)
set_atlanta = set(atlanta)
set_houston = set(houston)

# Finding duplicates in 2 sites
print("Duplicates between Houston and Atlanta:\n" + "-" * 40)
print(set_houston.intersection(set_atlanta))

# Finding duplicates in 3 sites
print("Duplicates between all sites:\n" + "-" * 40)
print(set_houston.intersection(set_atlanta.intersection(set_chicago)))

# Finding unique values for Chicago
print("Unique IP addresses in Chicago:\n" + "-" * 40)
print(set_chicago.difference(set_atlanta.union(set_houston)))

