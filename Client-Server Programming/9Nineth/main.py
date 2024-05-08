from bs4 import BeautifulSoup
import requests
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

url = "https://sinoptik.ua/"
savedHTML = requests.get(url)
soup = BeautifulSoup(savedHTML.text, "html.parser")

window = Tk()
window.geometry("250x300")
window.title("ПОГОДА")

label1 = ttk.Label(text=soup.find('p', class_='today-time').text)
label1.place(x=20, y=10)

canvas1 = tkinter.Canvas(window, width=200, height=200)
canvas1.place(x=0, y=30)
img = Image.open(f"temp.png")
img = img.resize((80, 140))
photo = ImageTk.PhotoImage(img)
canvas1.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas1.image = photo

canvas2 = tkinter.Canvas(window, width=200, height=200)
canvas2.place(x=70, y=30)
imageURL = "https://sinst.fwdcdn.com/img/weatherImg/b/d000.jpg"
response = requests.get(imageURL)
if response.status_code == 200:
    with open("picture1.png", "wb") as file:
        file.write(response.content)
img = Image.open("picture1.png")
img = img.resize((150, 140))
photo = ImageTk.PhotoImage(img)
canvas2.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas2.image = photo

label2 = ttk.Label(text=soup.find('p', class_='today-temp').text)
label2.place(x=100, y=150)

label3 = ttk.Label(text=soup.find('div', class_='infoDaylight').text)
label3.place(x=20, y=180)

label4 = ttk.Label(text=soup.find('p', class_='infoHistory').text)
label4.place(x=20, y=240)

label5 = ttk.Label(text=soup.find('p', class_='infoHistoryval').text)
label5.place(x=40, y=260)

window.mainloop()