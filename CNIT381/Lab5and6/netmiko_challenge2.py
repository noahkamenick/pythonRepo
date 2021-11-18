from netmiko import ConnectHandler

router = {'device_type': 'cisco_ios', 'host': '192.168.122.10', 'username':'cisco', 'password':'cisco','port':'22', 'secret':'cisco', 'verbose': True}
connection = ConnectHandler(**router)
prompt = connection.find_prompt()

if '>' in prompt:

    connection.enable()   

if not connection.check_config_mode():

    connection.config_mode()

output = connection.send_config_set('int lo0', 'exit')

connection.exit_config_mode() 

print('Closing connection')

connection.disconnect()

print('#'*40)