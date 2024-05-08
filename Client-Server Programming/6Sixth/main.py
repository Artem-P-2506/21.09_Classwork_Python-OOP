import requests
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

key = "42972882-0f77eec6bd9a961c014b42386"

def clickSearch():
    req = enterReq.get()
    res = requests.get(f"https://pixabay.com/api/?key={key}&q={req}&image_type=photo&per_page=6")
    print(f"Status:\t{res.status_code}")
    resJSON = res.json()
    print(resJSON)

    i = 0
    for obj in resJSON['hits']:
        i += 1
        image = requests.get(obj['largeImageURL'])
        with open(f"picture{i}.png", "wb") as file:
            file.write(image.content)

    print("--- DOWNLOAD COMPLETE !!!")
    label.configure(background="green")

def clickShow():
    label.configure(background="red")
    for i, canvas in enumerate([canvas1, canvas2, canvas3, canvas4, canvas5, canvas6], start=1):
        img = Image.open(f"picture{i}.png")
        img = img.resize((300, 300))
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
        canvas.image = photo

#========================================= GUI =========================================
root = tkinter.Tk()
root.title("Pixabay")
root.geometry("1000x720")
root.resizable(False, False)

label = ttk.Label(text="Введите запрос для поиска:")
label.configure(background="orange")
label.place(x=10, y=10)

enterReq = ttk.Entry()
enterReq.place(x=166, y=8)
enterReq.configure(width=100)

buttonSearch = ttk.Button(text="SEARCH", command=clickSearch)
buttonSearch.place(x=772, y=6)
buttonSearch.configure(width=35)

canvas1 = tkinter.Canvas(root, width=300, height=300)
canvas1.place(x=25, y=70)
canvas2 = tkinter.Canvas(root, width=300, height=300)
canvas2.place(x=350, y=70)
canvas3 = tkinter.Canvas(root, width=300, height=300)
canvas3.place(x=675, y=70)
canvas4 = tkinter.Canvas(root, width=300, height=300)
canvas4.place(x=25, y=395)
canvas5 = tkinter.Canvas(root, width=300, height=300)
canvas5.place(x=350, y=395)
canvas6 = tkinter.Canvas(root, width=300, height=300)
canvas6.place(x=675, y=395)

buttonShow = ttk.Button(text="SHOW PICTURES", command=clickShow)
buttonShow.place(x=9, y=35)
buttonShow.configure(width=162)

root.mainloop()