import requests
import time
import os

URL = "https://totmannprojekt-4.onrender.com"

while True:

    try:
        response = requests.get(URL)
        data = response.json()

        print(data)

        if data["seconds"] == 0:
            os.system("rundll32.exe user32.dll,LockWorkStation")

        time.sleep(5)

    except Exception as e:
        print("Fehler:", e)
        time.sleep(5)