import re
import json
import os

PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
class RegistrationFormController:
    def __init__(self):
        self.__forms = []

    def addForm(self, formOBJ):
        self.__forms.append(formOBJ)

    def deleteForm(self, index):
        if self.getSize() != 0 and index < self.getSize() and index >= 0:
            self.__forms.pop(index)

    def getForm(self, index):
        if self.getSize() == 0 or index >= self.getSize() or index < 0:
            return None
        else:
            return self.__forms[index]

    def getSize(self):
        return len(self.__forms)

    def emailValidation(self, email):
        return re.match(PATTERN, email)

    def getInformation(self, formIndex):
        return str(self.__forms[formIndex])

    def dumpInfoToJSON(self, formIndex):
        name = "json.txt"
        information = self.getInformation(formIndex)
        flag = "a" if os.path.exists(name) else "w"
        with open(name, flag) as file:
            file.write(f"{json.dumps(information)}\n")
            print("=== DUMP - SUCCESS ===\n")