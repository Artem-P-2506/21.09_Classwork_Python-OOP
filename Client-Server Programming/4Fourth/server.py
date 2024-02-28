import socket
import threading
import os
from dataWrapper import *

def sendPacketTCP(conn, data, type="message"):
    conn.send(dataWrapper.serializationData(data, typeOfData=type).encode())
    dataFromClient = dataWrapper.deserializationFullData(conn.recv(1024).decode())
    print(f"Client {clientID} send:\t{dataFromClient}")
    if not str(dataFromClient['msq']) == "Package received!":
        sendPacketTCP(conn, data)
    else:
        return True

def connectToClientTCP(clients, clientID):
    conn, addr = clients[clientID - 1]
    print(f"Server get client №{clientID}:\t{conn}\t|\t{addr}!")

    conn.send(dataWrapper.serializationData(f"Hello client №{clientID}!").encode())
    dataFromClient = dataWrapper.deserializationFullData(conn.recv(1024).decode())
    print(f"Client {clientID} send:\t{dataFromClient}")

    if str(dataFromClient['msq']) == "Package received!":
        while(True):
            while(True):
                pathToFile = input("Enter the path to sending file: ")
                if os.path.exists(pathToFile) or pathToFile == "/exit":
                    break
                else:
                    print("ERROR: Wrong path!")
                    continue
            if not pathToFile == "/exit":
                with open(pathToFile, 'r') as file:
                    data = file.read()
                sendPacketTCP(conn, data, type="file")
                print(f"File {pathToFile} was successfully sent!")
            else:
                sendPacketTCP(conn, "/exit")
                conn.close()
                print(f"Client №{clientID} close!")

# =============================================== SERVER ===============================================
server = socket.socket()
host = socket.gethostname()
port = 4005
print("Server start!")

server.bind((host, port))
server.listen(5)

clients = []
clientID = 0
while True:
    conn, addr = server.accept()
    clientID += 1
    clients.append((conn, addr))
    threading.Thread(target=connectToClientTCP, args=(clients, clientID)).start()
    if len(clients) == 10:
        break

server.close()
print("\nServer close!")