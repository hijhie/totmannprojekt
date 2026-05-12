from flask import Flask, render_template, redirect, jsonify
import time

app = Flask(__name__)

timer_seconds = 6600
last_reset = time.time()

timer_active = False
armed = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():
    global last_reset
    global timer_active
    global armed

    last_reset = time.time()
    timer_active = True
    armed = False

    return redirect("/")

@app.route("/reset")
def reset():
    global last_reset
    global armed

    last_reset = time.time()
    armed = False

    return redirect("/")

@app.route("/time")
def get_time():

    global armed

    if not timer_active:
        return jsonify({
            "seconds": "Nicht gestartet",
            "armed": False
        })

    remaining = int(timer_seconds - (time.time() - last_reset))

    if remaining <= 0:
        armed = True
        remaining = 0

    return jsonify({
        "seconds": remaining,
        "armed": armed
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
