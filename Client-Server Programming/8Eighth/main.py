import requests
import tkinter
from tkinter import ttk

API_KEY = "cbNr5mtQNlbQo8L1BvNuPvokFG0uJOqnT2NUK7om"
URL = "https://api.nasa.gov/neo/rest/v1/feed"

def clickSearch():
    startDate = enterStartDate.get()
    endDate = enterEndDate.get()
    params = {
        "api_key": API_KEY,
        "start_date": startDate,
        "end_date": endDate
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        print(f"Result:\t{response.status_code}")
        responseJSON = response.json()
        print(f"Data:\t{responseJSON}\n")
    else:
        print("Ошибка при выполнении запроса:", response.status_code)

    print("------------------ RESULT ------------------")
    result = ""
    earth = responseJSON["near_earth_objects"]
    for date, asteroids in earth.items():
        print(f"--------- DATE:\t{date} ---------")
        result += f"\n--------- DATE: {date} ---------\n"
        for asteroid in asteroids:
            print(f"\t{asteroid['name']}")
            result += f"\t{asteroid['name']}\n"

    labelResult['text'] = result


#========================================= GUI =========================================
root = tkinter.Tk()
root.title("NASA API")
root.geometry("330x550")
root.resizable(False, True)

labelStartDate = ttk.Label(text="Введите дату начала:")
labelStartDate.configure(background="orange")
labelStartDate.place(x=10, y=10)

enterStartDate = ttk.Entry()
enterStartDate.place(x=135, y=8)
enterStartDate.configure(width=30)

labelEndDate = ttk.Label(text="Введите  дату  конца:")
labelEndDate.configure(background="orange")
labelEndDate.place(x=10, y=35)

enterEndDate = ttk.Entry()
enterEndDate.place(x=135, y=33)
enterEndDate.configure(width=30)

buttonSearch = ttk.Button(text="ПОКАЗАТЬ РЕЗУЛЬТАТЫ", command=clickSearch)
buttonSearch.place(x=11, y=60)
buttonSearch.configure(width=50)

labelResult = ttk.Label()
labelResult.configure(background="gray")
labelResult.place(x=70, y=95)

root.mainloop()