import socket
import json
import uuid
from datetime import datetime

client = socket.socket()
host = socket.gethostname()
port = 4111
print("Client №3 start!")

client.connect((host, port))
print("Client №3 connect!")
data = client.recv(1024)
print(f"Server send:\t{data.decode()}")

while True:
    text = input("Enter message: ")
    message ={
        "ID": str(uuid.uuid4()),
        "msq": text,
        "Date": str(datetime.now())
    }

    msqJSON = json.dumps(message)
    client.send(msqJSON.encode())
    if text == "/exit":
        client.close()
        break
print("Client №3 close!")