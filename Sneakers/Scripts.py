import os

def writeCharacteristicsToFile(sneakersOBJ):
    with open("file.txt", 'w') as file:
        file.write(sneakersOBJ.showCharacteristics())

def readCharacteristicsFromFile(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            temp = file.read().split("\t")
            for i in range(len(temp)):
                if i % 2 == 0:
                    temp[i].pop()
        return temp
    else:
        print("Invalid path!")