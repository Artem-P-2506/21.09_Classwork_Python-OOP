import socket
import tkinter
from tkinter import ttk
from dataWrapper import *

def usernameRequest():
    request = dataWrapper.serializationData("USERNAME")
    conn.send(request.encode())
    answer = conn.recv(1024).decode()
    data = dataWrapper.deserializationFullData(answer)
    labelAnsver['background'] = "green"
    labelAnsver['text'] = f"Имя учетной записи клиента:\t{data['message']}"
    timeLabel['background'] = "green"
    timeLabel['text'] = f"Время запроса:\t{data['Date']}"

def hostnameRequest():
    request = dataWrapper.serializationData("HOSTNAME")
    conn.send(request.encode())
    answer = conn.recv(1024).decode()
    data = dataWrapper.deserializationFullData(answer)
    labelAnsver['background'] = "green"
    labelAnsver['text'] = f"Сетевое имя клиента:\t{data['message']}"
    timeLabel['background'] = "green"
    timeLabel['text'] = f"Время запроса:\t{data['Date']}"

def osVersionRequest():
    request = dataWrapper.serializationData("OS_VERSION")
    conn.send(request.encode())
    answer = conn.recv(1024).decode()
    data = dataWrapper.deserializationFullData(answer)
    labelAnsver['background'] = "green"
    labelAnsver['text'] = f"Версия ОС клиента:\t{data['message']}"
    timeLabel['background'] = "green"
    timeLabel['text'] = f"Время запроса:\t{data['Date']}"

def diskListRequest():
    request = dataWrapper.serializationData("DISK_LIST")
    conn.send(request.encode())
    answer = conn.recv(1024).decode()
    data = dataWrapper.deserializationFullData(answer)
    labelAnsver['background'] = "green"
    labelAnsver['text'] = f"Список дисков клиента:\t{data['message']}"
    timeLabel['background'] = "green"
    timeLabel['text'] = f"Время запроса:\t{data['Date']}"

#=======================================================================================================================
server = socket.socket()
host = socket.gethostname()
port = 4000
print("Server start!")

server.bind((host, port))
server.listen(5)
conn, addr = server.accept()
print(f"Server get client!")

root = tkinter.Tk()
root.title("Меню")
root.geometry("300x165")
root.resizable(False, False)

label = ttk.Label(background="gray", foreground="white", text="Выберите что нужно получить от клиента:")
label.pack()

btnUsername = ttk.Button(width=25, text="Имя учетной записи", command=usernameRequest)
btnUsername.pack()
btnHostname = ttk.Button(width=25, text="Сетевое имя", command=hostnameRequest)
btnHostname.pack()
btnOsVersion = ttk.Button(width=25, text="Версия ОС", command=osVersionRequest)
btnOsVersion.pack()
btnDiskList = ttk.Button(width=25, text="Список дисков", command=diskListRequest)
btnDiskList.pack()

labelAnsver = ttk.Label(background="red", foreground="white", text="ИНФОРМАЦИЯ ОТСУТСТВУЕТ")
labelAnsver.pack()
timeLabel = ttk.Label(background="red", foreground="white", text="Время запроса: ИНФОРМАЦИЯ ОТСУТСТВУЕТ")
timeLabel.pack()

root.mainloop()