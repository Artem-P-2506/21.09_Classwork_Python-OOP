from tkinter import *
from tkinter import ttk

def clickRed():
    global window
    global colorRed
    if colorRed + 10 <= 255:
        colorRed += 10
    else:
        print("MAX VALUE OF RED")
    window["background"] = f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}"

def clickGreen():
    global window
    global colorGreen
    if colorGreen + 10 <= 255:
        colorGreen += 10
    else:
        print("MAX VALUE OF GREEN")
    window["background"] = f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}"

def clickBlue():
    global window
    global colorBlue
    if colorBlue + 10 <= 255:
        colorBlue += 10
    else:
        print("MAX VALUE OF BLUE")
    window["background"] = f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}"



# -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=- MAIN -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-
if __name__ == "__main__":
    window = Tk()
    window.geometry("700x500")
    window.resizable(True, True)
    window.title("Hello window!")
    colorRed = 0
    colorGreen = 0
    colorBlue = 0
    window.configure(background=f"#{colorRed:02x}{colorGreen:02x}{colorBlue:02x}")

    button1 = ttk.Button(text="RED", command=clickRed)
    button1.place(x=150, y=200)

    button2 = ttk.Button(text="GREEN", command=clickGreen)
    button2.place(x=300, y=200)

    button3 = ttk.Button(text="BLUE", command=clickBlue)
    button3.place(x=450, y=200)
    window.mainloop()