from netmiko import Netmiko
from netmiko import ConnectHandler

########################################
##Challenge 1c
########################################

router = {'device_type': 'cisco_ios', 'host': '192.168.122.10', 'username':'cisco', 'password':'cisco','port':'22', 'secret':'cisco', 'verbose': True}

connection = ConnectHandler(**router)
prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()

connection.config_mode()

pess = connection.send_command('username u1 secret cisco')

print(pess)

output = connection.send_command('do sh run')

print(output)



print('closing connection')

connection.disconnect()

print('#'*40)