from MVC_RegistrationForm.Controller.RegistrationFormController import *
from tkinter import *

class TkAdministratorView:
    def __init__(self):
        self.__controller = RegistrationFormController()

        self.__root = Tk()
        self.__root.geometry("700x450")
        self.__root.title("ADMINISTRATOR FORM")
        self.__root.configure(background="black")

        self.__emailLabel = Label(text="REGISTRATIONS:")
        self.__emailLabel.pack()

        self.__dataField = Text(background="darkgreen", foreground="white")
        self.__dataField.pack()

        self.__addBtn = Button(text="SHOW INFORMATION", background="brown", foreground="white", command=self.btnShowClick)
        self.__addBtn.pack()

        self.__root.mainloop()

    def btnShowClick(self):
        name = "json.txt"
        with open(name, 'r') as file:
            data = file.read()
        self.__dataField.delete(1.0, END)
        self.__dataField.insert(1.0, data)