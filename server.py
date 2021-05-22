import socket
import threading
from cryptography.fernet import Fernet
ip=input("enter your ip adress, type local to use the local host")
if ip=="local":
    host = '127.0.0.1'
else:
    host=ip
port = 1235
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSock.bind((host, port))
serverSock.listen()
f = Fernet("Sp1MImGD6ddlsmq3di0SimVsvP92TA1Gvo9MGWFTIoo=")


clients=[]

def sendOut(message):
    for clientsocket in clients:
        clientsocket.send(message)
def messagePrep(clientsocket):
    while True:
        try:
            message=clientsocket.recv(2048)
            sendOut(message)
        except:
            clients.remove(clientsocket)
            clientsocket.close()
            print(f"{clientsocket} has left.")
            break


def receiveMessages():
    while True:
        clientsocket, address = serverSock.accept()
        print(f"a connection from {address}has been established")
        clients.append(clientsocket)
        print(f"{address} has joined!")
        serverThread = threading.Thread(target=messagePrep, args=(clientsocket,))
        serverThread.start()
receiveMessages()
