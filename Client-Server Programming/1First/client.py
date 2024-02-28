import socket

client = socket.socket()
host = socket.gethostname()
port = 4100
print("Client start!")

client.connect((host, port))
print("Client connect!")
data = client.recv(1024)
print(f"Server send:\t{data.decode()}")

client.close()
print("Client close!")