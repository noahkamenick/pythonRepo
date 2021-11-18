from simplecrypt import encrypt, decrypt # encryption
from getpass import getpass
import json
import myParamiko as m

def encrypt_file():
    #---Read in pertinent info from user
    dc_in_filename = input('\nInput filename:   ')
    key = input( 'Encryption key (cisco):   ') # key for encrypt

    #---Read in device credentials from CSV file into list of device credentials
    device_creds_list = m.get_list_from_file(dc_in_filename)


    print('\n-------- device creds---------------------------------')

    print(device_creds_list)

    #---Encrypt the device credentials using ken from user

    encrypted_dc_out_filename = input('\nOutput encrypted filename: ')

    with open(encrypted_dc_out_filename,'wb') as dc_out:
        dc_out.write(encrypt(key, json.dumps(device_creds_list))) #encrypt with key, dump list to file

    print("encrypted the file")

def decrypt_file(file_name):
    print("Enter password to open file")
    key = getpass()
    with open (file_name, 'rb') as dc_in:
        device_creds_in = json.loads(decrypt(key, dc_in.read())) #json to list, then decrypt to json/txt
    print('\n-----confirm: decrypt the file------------------------')
    print(type(device_creds_in))
    print(device_creds_in)
    return device_creds_in # return the list