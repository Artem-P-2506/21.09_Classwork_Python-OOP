import socket
import requests
import json

API_KEY = "cXRKzZO0C7RS7jBHsJjlF7ZwbwVgwvGNh1Mg1pCs"# !Если риложение работает не коректно - НУЖНО ОНОВИТЬ КЛЮЧ
URL = "https://api.nasa.gov/neo/rest/v1/feed"

def sendAsteroidData(data):
    startDate = data['start_date']
    endDate = data['end_date']
    params = {
        "api_key": API_KEY,
        "start_date": startDate,
        "end_date": endDate
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        responseJSON = response.json()
    else:
        responseJSON = {"error": f"Ошибка при выполнении запроса: {response.status_code}"}

    result = ""
    if "near_earth_objects" in responseJSON:
        earth = responseJSON["near_earth_objects"]
        for date, asteroids in earth.items():
            result += f"\n--------- DATE: {date} ---------\n"
            for asteroid in asteroids:
                result += f"\t{asteroid['name']}\n"
    else:
        result = responseJSON.get("error", "Неизвестная ошибка")
    return result

server = socket.socket()
host = socket.gethostname()
port = 4000
print("Server start!")

server.bind((host, port))
server.listen(5)
conn, addr = server.accept()
while True:
    answer = conn.recv(4096).decode()
    data = json.loads(answer)
    result = sendAsteroidData(data)
    # ПРИ ИСПОЛЬЗОВАНИИ JSON В ОБРАТНОЙ ОТПРАВКЕ ДАННЫХ МОГУТ РАНДОМНО ВОЗНИКАТЬ ОШИБКИ "ВНУТРИ" JSON-БИБЛИОТЕКИ
    response = json.dumps(result)
    conn.send(response.encode())

server.close()
print("\nServer close!")