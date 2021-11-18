from netmiko import ConnectHandler
import myParamiko as m

router = {'device_type': 'cisco_ios', 'host': '192.168.122.10', 'username':'cisco', 'password':'cisco','port':'22', 'secret':'cisco', 'verbose': True}
connection = ConnectHandler(**router)
prompt = connection.find_prompt()

if '>' in prompt:

    connection.enable()   

print('Sending commands from file...')

output = connection.send_config_from_file('192.168.122.10_ospf.txt') # read commands from file

print(output)

print('Closing connection')

connection.disconnect()

print('#'*40)