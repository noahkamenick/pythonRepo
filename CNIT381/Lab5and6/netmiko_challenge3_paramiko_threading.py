from netmiko import ConnectHandler
import encrypt_dev_info as edi
import myParamiko as m
import time
import threading

start = time.time() # Start timing execution

def config_ospf(router):
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

encrypte_file = input('Enter encrypted files: ')
routers = edi.decrypt_file(encrypte_file)

threads = list()

for router in routers:
    th = threading.Thread(target=config_ospf, args=(router,))
    threads.append(th)
    

for th in threads:
    th.start()


for th in threads:
    th.join()

end = time.time()

print(f'Total execution time:{end-start}')