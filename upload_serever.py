import os
import socket
import struct
import ssl
from cryptography.fernet import Fernet
HOST="192.168.50.77"
PORT=8200

Save_Folder=r"C:\USERS\Meron\Python"

def recv_exact(sock,size):
    data=b""
    while len(data)<size:
        part=sock.recv(size-len(data))
        if not part:
            raise ConnectionError("connection closed early")
        data+=part
    return data

def recieve_file():

    os.makedirs(Save_Folder,exist_ok=True)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST,PORT))
        server_socket.listen(1)
        
        client_socket ,client_adress=server_socket.accept()
        with client_socket:
            print("connecntto:",client_adress)
            name_length=struct.unpack("!I",recv_exact(client_socket,4))[0]
            file_size=struct.unpack("!Q",recv_exact(client_socket,8))[0]
            file_name=recv_exact(client_socket,name_length).decode("utf-8")

            full_path=os.path.join(Save_Folder,file_name)
            print(f"receiving file:{file_name}")

            recieved=0
            with open(full_path,"wb") as file:
                while recieved<file_size:
                    chunk=client_socket.recv(min(4096,file_size-recieved))
                    if not chunk:
                        break
                    file.write(chunk)
                    recieved+=len(chunk)
            

