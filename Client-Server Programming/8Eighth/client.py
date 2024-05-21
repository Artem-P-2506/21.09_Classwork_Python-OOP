import socket
import tkinter
from tkinter import ttk
import json

def clickSearch():
    startDate = enterStartDate.get()
    endDate = enterEndDate.get()
    params = {
        "start_date": startDate,
        "end_date": endDate
    }

    request = json.dumps(params)
    client.send(request.encode())
    answer = client.recv(4096).decode()
    data = json.loads(answer)
    labelResult['text'] = data
    root.update()


#==================================== GUI ====================================
client = socket.socket()
host = socket.gethostname()
port = 4000
print("Client №1 start!")

client.connect((host, port))
print("Client №1 connect!")

root = tkinter.Tk()
root.title("NASA API")
root.geometry("330x550")
root.resizable(False, True)

labelStartDate = ttk.Label(text="Введите дату начала:")
labelStartDate.configure(background="orange")
labelStartDate.place(x=10, y=10)

enterStartDate = ttk.Entry()
enterStartDate.place(x=135, y=8)
enterStartDate.configure(width=30)

labelEndDate = ttk.Label(text="Введите  дату  конца:")
labelEndDate.configure(background="orange")
labelEndDate.place(x=10, y=35)

enterEndDate = ttk.Entry()
enterEndDate.place(x=135, y=33)
enterEndDate.configure(width=30)

buttonSearch = ttk.Button(text="ПОКАЗАТЬ РЕЗУЛЬТАТЫ", command=clickSearch)
buttonSearch.place(x=11, y=60)
buttonSearch.configure(width=50)

labelResult = ttk.Label()
labelResult.configure(background="gray")
labelResult.place(x=70, y=95)

root.mainloop()
client.close()
print("Client №1 close!")