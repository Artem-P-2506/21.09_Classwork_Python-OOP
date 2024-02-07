from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import psutil

def selectProcess(e):
    labelProcess["text"] = comboBox.get()

def clickKillProcess():
    for item in psutil.process_iter():
        if item.name() == comboBox.get():
            item.kill()
            print(f"Item '{item.name()}' was killed!")

def clickAddProcess():
    newProcess = psutil.Popen('cmdline')
    programs.append(comboBox.get())
    print(f"Item '{item.name()}' was dublicated!")



programs = []
for item in psutil.process_iter():
    programs.append(item.name())
# -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=- MAIN -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-
if __name__ == "__main__":
    window = Tk()
    window.geometry("300x200")
    window.resizable(False, False)
    window.title("Выпадающий список")
    window.configure(background="gray")

    comboBox = Combobox(values=programs)
    comboBox.configure(width=30)
    comboBox.pack()
    comboBox.bind("<<ComboboxSelected>>", selectProcess)

    labelProcess = ttk.Label()
    labelProcess["width"] = 30
    labelProcess.pack()

    buttonKill = ttk.Button(text="KILL PROCESS", command=clickKillProcess)
    buttonKill.pack()

    buttonAdd = ttk.Button(text="ADD PROCESS", command=clickAddProcess)
    buttonAdd.pack()

    window.mainloop()