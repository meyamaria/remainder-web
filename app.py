# Save as app.py in your project folder
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

user_data = []
water_data = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", user_data=user_data)

@app.route("/set_notifications", methods=["POST"])
def set_notifications():
    name = request.form["name"]
    sleep_hours = request.form["sleep_hours"]
    hour = request.form["hour"]
    minute = request.form["minute"]
    ampm = request.form["ampm"]
    sleep_time = f"{hour}:{minute.zfill(2)} {ampm}"
    # Example calculation for wake time
    wake_time = "..."
    user_data.append({
        "name": name,
        "sleep_time": sleep_time,
        "wake_time": wake_time,
        "sleep_hours": sleep_hours
    })
    return redirect("/")

@app.route("/drink_water", methods=["GET"])
def drink_water():
    return render_template("drink_water.html", water_data=water_data)

@app.route("/set_water_notification", methods=["POST"])
def set_water_notification():
    name = request.form["name"]
    hour = request.form["hour"]
    minute = request.form["minute"]
    ampm = request.form["ampm"]
    water_time = f"{hour}:{minute.zfill(2)} {ampm}"
    water_data.append({
        "name": name,
        "water_time": water_time
    })
    return redirect("/drink_water")

if __name__ == "__main__":
    app.run(debug=True)