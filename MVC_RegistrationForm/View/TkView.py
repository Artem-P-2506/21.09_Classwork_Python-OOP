from MVC_RegistrationForm.Model.RegistrationForm import *
from MVC_RegistrationForm.Controller.RegistrationFormController import *
from tkinter import Tk, Label, Button, Entry

class TkView:
    def __init__(self):
        self.__controller = RegistrationFormController()

        self.__root = Tk()
        self.__root.geometry("300x250")
        self.__root.title("REGISTRATION FORM")
        self.__root.configure(background="black")

        self.__emailLabel = Label(text="Enter your email:", width=20)
        self.__emailLabel.pack()
        self.__emailField = Entry(width=40)
        self.__emailField.pack()

        self.__loginLabel = Label(text="Enter your login:", width=20)
        self.__loginLabel.pack()
        self.__loginField = Entry(width=35)
        self.__loginField.pack()

        self.__passwordLabel = Label(text="Enter your password:", width=20)
        self.__passwordLabel.pack()
        self.__passwordField = Entry(width=30)
        self.__passwordField.pack()

        self.__repeatPasswordLabel = Label(text="Repeat your password:", width=20)
        self.__repeatPasswordLabel.pack()
        self.__repeatPasswordField = Entry(width=30)
        self.__repeatPasswordField.pack()

        self.__addBtn = Button(text="ENTER", background="brown", command=self.btnEnterClick)
        self.__addBtn.pack()

        self.__resultLable = Label(text="RESULT: -------", background="yellow")
        self.__resultLable.pack()

        self.__root.mainloop()

    def btnEnterClick(self):
        email = self.__emailField.get()
        login = self.__loginField.get()
        password = self.__passwordField.get()
        repeatPassword = self.__repeatPasswordField.get()

        if email and login and password and repeatPassword:
            if self.__controller.emailValidation(email):
                if password == repeatPassword:
                    self.__controller.addForm(RegistrationForm(email, login, password))
                    self.__resultLable.config(text="RESULT: SUCCESS", background="green")
                    print(self.__controller.getInformation(self.__controller.getSize() - 1))
                    self.__controller.dumpInfoToJSON(self.__controller.getSize() - 1)
                else:
                    self.__resultLable.config(text="RESULT: ERROR - PASSWORDS DO NOT MATCH", background="red")
            else:
                self.__resultLable.config(text="RESULT: ERROR - INVALID EMAIL", background="red")
        else:
            self.__resultLable.config(text="RESULT: ERROR - FIELD/S IS EMPTY", background="red")