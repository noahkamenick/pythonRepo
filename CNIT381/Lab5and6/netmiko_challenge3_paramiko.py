from netmiko import ConnectHandler
import myParamiko as m

routers = m.get_list_from_file('routers.txt')

for router in routers:
    
    connection = ConnectHandler(**router)
    
    prompt = connection.find_prompt()    

    if '>' in prompt:
    
        connection.enable()  
    
    if not connection.check_config_mode():
        
        connection.config_mode() 
    
    print('Sending commands from file...')

    output = connection.send_config_from_file(router['host']+'_ospf.txt') # read commands from multiple file

    print(output)

    print('Closing connection')

    connection.disconnect()

    print('#'*40)