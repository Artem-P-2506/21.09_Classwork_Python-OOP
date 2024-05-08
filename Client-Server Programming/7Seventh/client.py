import socket
import winreg
import psutil
from dataWrapper import *

def getUsername():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName")
        computerName, _ = winreg.QueryValueEx(key, "ComputerName")
        winreg.CloseKey(key)
        return computerName
    except Exception as e:
        print(f"Ошибка при получении имени компьютера: {e}")
        return None

def getHostname():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters")
        hostname, _ = winreg.QueryValueEx(key, "Hostname")
        winreg.CloseKey(key)
        return hostname
    except Exception as e:
        print(f"Ошибка при получении сетевого имени компьютера: {e}")
        return None

def getOSVersion():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        OSVersion, _ = winreg.QueryValueEx(key, "ProductName")
        winreg.CloseKey(key)
        return OSVersion
    except Exception as e:
        print(f"Ошибка при получении версии операционной системы: {e}")
        return None

def getDiskList():
    try:
        disks = []
        partitions = psutil.disk_partitions(all=True)
        for partition in partitions:
            disks.append(partition.device)
        return disks
    except Exception as e:
        print(f"Ошибка при получении списка дисков: {e}")
        return None

#=======================================================================================================================
client = socket.socket()
host = socket.gethostname()
port = 4000
print("Client №1 start!")

client.connect((host, port))
print("Client №1 connect!")

while(True):
    request = dataWrapper.deserializationFullData(client.recv(1024).decode())
    if request['message'] == "USERNAME":
        username = getUsername()
        if username:
            answer = dataWrapper.serializationData(username)
            client.send(answer.encode())
    elif request['message'] == "HOSTNAME":
        hostname = getHostname()
        if hostname:
            answer = dataWrapper.serializationData(hostname)
            client.send(answer.encode())
    elif request['message'] == "OS_VERSION":
        osVersion = getOSVersion()
        if osVersion:
            answer = dataWrapper.serializationData(osVersion)
            client.send(answer.encode())
    elif request['message'] == "DISK_LIST":
        diskList = getDiskList()
        if diskList:
            answer = dataWrapper.serializationData(diskList)
            client.send(answer.encode())
    else:
        print("ОШИБКА! Некоректный запрос!")

client.close()
print("Client №1 close!")