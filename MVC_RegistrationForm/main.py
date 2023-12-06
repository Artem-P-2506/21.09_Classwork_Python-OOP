from MVC_RegistrationForm.View.TkView import *
from MVC_RegistrationForm.View.TkAdministrationForm import *
from tkinter import *

def btnRegistrationFormClick():
    root.destroy()
    TkView()

def btnAdministratorWindowClick():
    root.destroy()
    TkAdministratorView()

# while(True):
#     choise = int(input("'1' - ФОРМА РЕГИСТРАЦИИ    |   '2' - ОКНО АДМИНИСТРАТОРА: "))
#     if choise == 1:
#         tkView = TkView()
#         break
#     elif choise == 2:
#         tkAdministratorView = TkAdministratorView()
#         break
#     else:
#         print("НЕВЕРНЫЙ ВЫБОР")

root = Tk()
root.geometry("200x60")
root.title("CHOISE")
root.configure(background="black")

registrationFormButton = Button(text="ФОРМА РЕГИСТРАЦИИ", background="blue", foreground="white", width=25, command=btnRegistrationFormClick)
registrationFormButton.pack()

administratorFormButton = Button(text="ОКНО АДМИНИСТРАТОРА", background="blue", foreground="white", width=25, command=btnAdministratorWindowClick)
administratorFormButton.pack()

root.mainloop()