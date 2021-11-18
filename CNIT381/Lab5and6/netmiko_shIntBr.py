from netmiko import Netmiko

############################
##Challenge 1a
############################

connection = Netmiko(host='192.168.122.10', port = '22', username='cisco', password='cisco', device_type='cisco_ios')

output = connection.send_command('sh ip int br')

print(output)

print('closing connection')

connection.disconnect()

print('#'*40)