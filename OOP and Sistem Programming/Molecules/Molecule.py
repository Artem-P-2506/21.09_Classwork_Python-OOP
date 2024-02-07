class Molecule:
    def __init__(self,name, *atoms):
        self._name = name
        self.atoms = atoms

    def getName(self):
        return self._name

    def setName(self, newName):
        self._name = newName

    def __iter__(self, numberOfAtom):
        if not (len(self.atoms) < numberOfAtom):
            return self.atoms[numberOfAtom]
        else:
            return -1

    def print(self):
        print(f"Имя молекулы:\t{self._name}")
        iterator = 1
        for item in self.atoms:
            print(f"--------Атом №{iterator}--------")
            print(item)
            iterator += 1