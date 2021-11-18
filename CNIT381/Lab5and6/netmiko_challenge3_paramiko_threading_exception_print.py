from netmiko import ConnectHandler, Netmiko
from netmiko import ssh_exception
from netmiko.ssh_exception import NetMikoTimeoutException, NetmikoTimeoutException
from paramiko.ssh_exception import NoValidConnectionsError, SSHException
from netmiko.ssh_exception import AuthenticationException
import encrypt_dev_info as edi
import myParamiko as m
import alert_popup as ap
import time
import threading

start = time.time() # Start timing execution

def config_ospf(router):
    
    try:
        connection = ConnectHandler(**router)
    except (AuthenticationException):
        print('Auth Failure', router['host'], 'CNIT-381-LAB')
        return
    except (NetmikoTimeoutException):
        print('Timeout to device', router['host'], 'CNIT-381-LAB')
        return
    except (SSHException):
        print('SSH Issue. Are you sure SSH is enabled?', router['host'], 'CNIT-381-LAB')
        return
    except(NoValidConnectionsError):
        print('NoValid', router['host'], 'CNIT-381-LAB')
        return
    except Exception as unknown_error:
        print('Unknown Failure', str(unknown_error), '')
        return
    
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