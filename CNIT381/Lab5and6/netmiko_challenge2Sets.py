from netmiko import ConnectHandler

router = {'device_type': 'cisco_ios', 'host': '192.168.122.10', 'username':'cisco', 'password':'cisco','port':'22', 'secret':'cisco', 'verbose': True}
connection = ConnectHandler(**router)
prompt = connection.find_prompt()

cmd = '''int lo 0
ip add 1.1.1.1 255.255.255.255
exit
username cisco1 secret cisco
'''

if '>' in prompt:

    connection.enable()   

if not connection.check_config_mode():

    connection.config_mode()

connection.send_config_set(cmd.split('\n'))

connection.exit_config_mode() 

print('Closing connection')

connection.disconnect()

print('#'*40)