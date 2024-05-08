from bs4 import BeautifulSoup
import requests
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

request = "диски-ф25"
url = f"https://www.olx.ua/uk/list/q-{request}/"
savedHTML = requests.get(url)
soup = BeautifulSoup(savedHTML.text, "html.parser")

window = Tk()
window.geometry("1720x1210")
window.title("ОЛХ-парсер")

names = []
for name in soup.find_all('h6', class_='css-16v5mdi er34gjf0'):
    names.append(name.text)

prices = []
for price in soup.find_all('p', class_='css-tyui9s er34gjf0'):
    prices.append(price.text)

i = 0
photos = soup.find_all('div', class_='css-gl6djm')
for img in photos:
    if img.find('img'):
        imageURL = img.find('img')['src']
        response = requests.get(imageURL)
        with open(f"picture{i}.png", "wb") as file:
            file.write(response.content)
        i += 1
        if i == 5:
            break

iterator = 0
coordinatesY = (10, 610, 1210, 1810)
for y in coordinatesY:
    coordinatesX = (10, 610, 1210)
    for x in coordinatesX:
        if iterator == 5:
            break
        labelName = ttk.Label(text=names[iterator])
        labelName.configure(font=2)
        labelName.place(x=x, y=y)

        labelPrice = ttk.Label(text=prices[iterator])
        labelPrice.configure(font=1)
        labelPrice.place(x=x, y=y+30)

        canvas = tkinter.Canvas(window, width=500, height=500)
        canvas.place(x=x, y=y+60)
        img = Image.open(f"picture{iterator}.png")
        img = img.resize((500, 500))
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
        canvas.image = photo

        iterator += 1

window.mainloop()