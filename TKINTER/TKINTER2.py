from tkinter import *
from tkinter import ttk

def clickSave():
    with open("information.txt", 'w') as file:
        file.write(f"{txt1.get()} {txt2.get()} {txt3.get()}, {txt4.get()}")

def clickDelete():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)


# -=-=-=-=-=-=-=-=-=--=-=-=- MAIN -=-=-=-=-=-=-=-=-=--=-=-=-
if __name__ == "__main__":
    window = Tk()
    window.geometry("290x200")
    window.resizable(False, False)
    window.title("Форма анкетирования")
    window.configure(background="orange")

    label1 = ttk.Label(text="Введите имя:")
    label1.configure(background="orange")
    label1.place(x=15, y=15)
    txt1 = ttk.Entry()
    txt1.place(x=150, y =15)

    label2 = ttk.Label(text="Введите фамилию:")
    label2.configure(background="orange")
    label2.place(x=15, y=45)
    txt2 = ttk.Entry()
    txt2.place(x=150, y =45)

    label3 = ttk.Label(text="Введите отчество:")
    label3.configure(background="orange")
    label3.place(x=15, y=75)
    txt3 = ttk.Entry()
    txt3.place(x=150, y=75)

    label4 = ttk.Label(text="Введите Ваш возраст:")
    label4.configure(background="orange")
    label4.place(x=15, y=115)
    txt4 = ttk.Entry()
    txt4.place(x=150, y =115)

    buttonDelete = ttk.Button(text="ОЧИСТИТЬ ВСЕ", command=clickDelete)
    buttonDelete.place(x=15, y=160)

    buttonSave = ttk.Button(text="ЗАПИСАТЬ", command=clickSave)
    buttonSave.place(x=200, y=160)

    window.mainloop()