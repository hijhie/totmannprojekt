from flask import jsonify, render_template, redirect, jsonify
import threading
import time
import os

app = Flask(__name__)

timer_seconds = 10
last_reset = time.time()

timer_active = False

def timer_loop():
    global last_reset
    global timer_active

    while True:
        time.sleep(1)

        if timer_active:

            if time.time() - last_reset > timer_seconds:
                os.system("rundll32.exe user32.dll,LockWorkStation")
                timer_active = False

threading.Thread(target=timer_loop, daemon=True).start()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():
    global last_reset
    global timer_active

    last_reset = time.time()
    timer_active = True

    return redirect("/")

@app.route("/reset")
def reset():
    global last_reset

    if timer_active:
        last_reset = time.time()

    return redirect("/")

@app.route("/time")
def get_time():

    if not timer_active:
        return jsonify({"seconds": "Scharf"})

    remaining = int(timer_seconds - (time.time() - last_reset))

    if remaining < 0:
        remaining = 0

    return jsonify({"seconds": remaining})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

print("deaktivirt")
