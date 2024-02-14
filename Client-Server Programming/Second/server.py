import socket
import threading
import json

def connectToClient(clients, clientID):
    conn, addr = clients[clientID - 1]
    print(f"Server get client №{clientID}:\t{conn}\t|\t{addr}!")
    msq = f"Hello client №{clientID}!"
    conn.send(msq.encode())

    while True:
        data = conn.recv(1024)
        if not data:
            continue
        message = json.loads(data.decode())
        print(f"Client {clientID} send:\t{message}")
        if message['msq'] == "/exit":
            conn.close()
            print(f"Client №{clientID} close!")
            break



if __name__ == "__main__":
    server = socket.socket()
    host = socket.gethostname()
    port = 4111
    print("Server start!")

    server.bind((host, port))
    server.listen(5)

    clients = []
    clientID = 0
    while True:
        conn, addr = server.accept()
        clientID += 1
        clients.append((conn, addr))
        threading.Thread(target=connectToClient, args=(clients, clientID)).start()
        if len(clients) == 10:
            break

    server.close()
    print("\nServer close!")