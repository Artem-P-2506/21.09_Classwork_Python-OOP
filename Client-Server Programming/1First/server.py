import socket

server = socket.socket()
host = socket.gethostname()
port = 4100

server.bind((host, port))
server.listen(5)


print("Server start!")

conn, add = server.accept()
print(f"Server get client:\t{conn}\t|\t{add}!")

msq = "Hello server!"
conn.send(msq.encode())
print("Client get msq from server!")

conn.close()
print("Client close!")

print("Server close!")
server.close()