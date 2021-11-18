from netmiko import Netmiko
from netmiko import ConnectHandler

###################################
##Challenge 1b
###################################

router = {'device_type': 'cisco_ios', 'host': '192.168.122.10', 'username':'cisco', 'password':'cisco','port':'22', 'secret':'cisco', 'verbose': True}

connection = ConnectHandler(**router)

connection.enable()

output = connection.send_command('sh run')

print(output)

print('closing connection')

connection.disconnect()

print('#'*40)