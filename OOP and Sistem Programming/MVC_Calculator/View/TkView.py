from tkinter import Tk, Label, Button, Entry
from MVC_Calculator.Controller.CalculatorController import *
from MVC_Calculator.Model.Calculator import *

class TkView:
    def __init__(self):
        self.__controller = CalculatorController()

        self.__root = Tk()
        self.__root.geometry("500x500")
        self.__root.configure(background="gray")

        self.__labelFirstNumberText = Label(text="Enter first number:")
        self.__labelFirstNumberText.pack()
        self.__firstNumberField = Entry()
        self.__firstNumberField.pack()

        self.__labelSecondNumberText = Label(text="Enter second number:")
        self.__labelSecondNumberText.pack()
        self.__secondNumberField = Entry()
        self.__secondNumberField.pack()

        self.__labelActionText = Label(text="Enter action sign\n( '+' | '-' | '*' | '/' ):")
        self.__labelActionText.pack()
        self.__actionField = Entry()
        self.__actionField.pack()

        self.__addBtn = Button(text="COUNT UP", command=self.btnCountUpClick)
        self.__addBtn.pack()

        self.__labelResultText = Label(text="RESULT:")
        self.__labelResultText.pack()
        self.__labelResultValue = Label(text="-------", background="yellow")
        self.__labelResultValue.pack()

        self.__root.mainloop()

    def btnCountUpClick(self):
        firstNumber = float(self.__firstNumberField.get())
        secondNumber = float(self.__secondNumberField.get())
        action = self.__actionField.get()
        if firstNumber and secondNumber and action:
            try:
                if self.__controller.getSize() > 0:
                    self.__controller.changeValues(0, firstNumber, secondNumber, action)
                else:
                    self.__controller.addCalculator(Calculator(firstNumber, secondNumber, action))
                result = self.__controller.startCountUp(0)
                self.__labelResultValue.config(text=result, background="green")
            except ValueError as e:
                print(f"ValueError: {str(e)}")