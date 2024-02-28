import socket
from dataWrapper import *

client = socket.socket()
host = socket.gethostname()
port = 4000
print("Client №1 start!")

client.connect((host, port))
print("Client №1 connect!")

while(True):
    message = client.recv(1024)
    time = str(datetime.now()) # Сохраняем время в момент получения пакета
    if message:
        data = dataWrapper.deserializationFullData(message.decode())
        print(f"Server send:\t{data}")
        jsonData = dataWrapper.serializationData("Package received!", data['UUID'], time)
        client.send(jsonData.encode())
        if str(data['msq']) == "/exit":
            break
    else:
        continue

client.close()
print("Client №1 close!")