import requests

res = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
data = res.json()
print(f"Response: {data}")

print("Выбирите валюту для отображения текущего курса:")
i = 0
for ccy in data:
    i += 1
    print(f"\t{ccy['ccy']} - {i}")

userChoise = int(input("Введите номер нужной валюты: "))
if userChoise == 1:
    for i in data:
        if i['ccy'] == "EUR":
            print(f"\tВалюта: {i['ccy']}\n\t\tПродажа: {i['sale']}\n\t\tПокупка: {i['buy']}")
            amountGRN = input("Введите сумму для обмена (в гривнах): ")
            if amountGRN.isdigit():
                print(f"\tКоличество {i['ccy']} после обмена {amountGRN} UAH составит: {float(amountGRN) / float(i['sale'])} ({i['ccy']})")
            else:
                print("Некоректный ввод!")
        else:
            continue
elif userChoise == 2:
    for i in data:
        if i['ccy'] == "USD":
            print(f"\tВалюта: {i['ccy']}\n\t\tПродажа: {i['sale']}\n\t\tПокупка: {i['buy']}")
            amountGRN = input("Введите количество гривен: ")
            if amountGRN.isdigit():
                print(f"\tКоличество {i['ccy']} после обмена {amountGRN} UAH составит: {float(amountGRN) / float(i['sale'])} ({i['ccy']})")
            else:
                print("Некоректный ввод!")

        else:
            continue
else:
    print("Некоректный ввод!")