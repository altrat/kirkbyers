'''
Some description
'''

def ssh_conn(ip_addr, username, password, device_type='cisco_ios'):
    '''Printing IP addresses.

    This function prints IP addresses of devices and credentials.'''
    print("IP address: " + ip_addr)
    print("Username: " + username)
    print("Password: " + password)
    print("Device type: " + device_type)

# First call - device type specified
ssh_conn('10.128.77.2', 'admin', 'superpassword', 'arista')

# Second call - device type not specified, default value expected
ssh_conn('10.128.77.2', 'admin', 'superpassword')

# Third call - using dictionary with parameters
dic = {
    'ip_addr': '10.128.77.2',
    'username': 'admin',
    'password': 'superpassword',
    'device_type': 'juniper'
}
ssh_conn(**dic)
