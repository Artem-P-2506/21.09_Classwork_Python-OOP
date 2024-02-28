import socket
import threading
from dataWrapper import *

TEST_DATA = ("1-first data packet", "2-second data packet", "3-third data packet", "4-fourth data packet", "5-fifth data packet")

def sendPacketTCP(conn, data):
    conn.send(dataWrapper.serializationData(data).encode())
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
        for data in TEST_DATA:
            sendPacketTCP(conn, data)
        sendPacketTCP(conn, "/exit")
        conn.close()
        print(f"Client №{clientID} close!")

# =============================================== SERVER ===============================================
server = socket.socket()
host = socket.gethostname()
port = 4000
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