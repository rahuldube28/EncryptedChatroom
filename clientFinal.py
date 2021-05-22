import threading
import socket
from cryptography.fernet import Fernet
ip=input("enter the host's ip adress, type local if you are using the local host")
if ip=="local":
    host = '127.0.0.1'
else:
    host=ip
port = 1235
key=input("enter the encryption key:")
f = Fernet(key)
username=input("Please enter your username")
print("type 'bye' to leave.")
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host,port))

def recieve():
    while True:
            msg=clientSocket.recv(2048)
            decodedMsg=f.decrypt(msg)
            output = str(decodedMsg, 'utf-8')
            print(output)

def encryptSend():
    while True:
        text=input()
        message=(f"{username}: {text}")
        if text=="bye":
            print("byeeeee")
            byeTesMessage=bytes(f"{username} has left.", 'utf-8')
            byeToken = f.encrypt(byeTesMessage)
            clientSocket.sendall(byeToken)
            clientSocket.close()
            break
        else:
            bytesMessage=bytes(message, 'utf-8')
            token = f.encrypt(bytesMessage)
            clientSocket.sendall(token)

recieveThread=threading.Thread(target=recieve)
recieveThread.start()
encryptSendThread=threading.Thread(target=encryptSend)
encryptSendThread.start()
