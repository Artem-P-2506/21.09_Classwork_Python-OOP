from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

def clickSave():
    data = txtData.get(1.0, END)
    with open(txtPath.get(), 'w') as file:
        file.write(data)

def clickDelete():
    txtData.delete(1.0, END)

def clickOpen():
    path = txtPath.get()
    txtData.delete(1.0, END)
    with open(path, 'r') as file:
        data = str(file.read())
        txtData.insert(1.0, data)



# -=-=-=-=-=-=-=-=-=--=-=-=- MAIN -=-=-=-=-=-=-=-=-=--=-=-=-
if __name__ == "__main__":
    path = "none"
    data = "none"

    window = Tk()
    window.geometry("700x530")
    window.resizable(False, False)
    window.title("БЛОКНОТ")
    window.configure(background="gray")

    label1 = ttk.Label(text="Введите путь к файлу:")
    label1.configure(background="orange")
    label1.place(x=10, y=11)
    txtPath = ttk.Entry()
    txtPath.place(x=136, y=10)
    txtPath.configure(width=91)
    buttonOpen = ttk.Button(text="ОТКРЫТЬ ФАЙЛ", command=clickOpen)
    buttonOpen.place(x=305, y=35)

    label2 = ttk.Label(text="Файл:")
    label2.configure(background="green")
    label2.place(x=20, y=75)
    txtData = scrolledtext.ScrolledText()
    txtData.insert(END, "none")
    txtData.place(x=20, y=96)

    buttonSave = ttk.Button(text="СОХРАНИТЬ", command=clickSave)
    buttonSave.place(x=20, y=491)

    buttonDelete = ttk.Button(text="ОЧИСТИТЬ ВСЕ", command=clickDelete)
    buttonDelete.place(x=585, y=491)

    window.mainloop()