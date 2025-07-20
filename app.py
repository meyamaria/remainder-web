from flask import Flask, render_template, request, redirect
from datetime import datetime, timedelta

app = Flask(__name__)
user_data = []
water_data = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", user_data=user_data)

@app.route("/set_notifications", methods=["POST"])
def set_notifications():
    name = request.form["name"]
    sleep_hours = int(request.form["sleep_hours"])
    hour = int(request.form["hour"])
    minute = int(request.form["minute"])
    ampm = request.form["ampm"]

    # Convert 12-hour to 24-hour format
    if ampm == 'PM' and hour != 12:
        hour += 12
    elif ampm == 'AM' and hour == 12:
        hour = 0

    now = datetime.now()
    sleep_time_obj = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if sleep_time_obj < now:
        sleep_time_obj += timedelta(days=1)

    wake_time_obj = sleep_time_obj + timedelta(hours=sleep_hours)

    sleep_time_str = sleep_time_obj.strftime("%I:%M %p")
    wake_time_str = wake_time_obj.strftime("%I:%M %p")

    user_data.append({
        "name": name,
        "sleep_time": sleep_time_str,
        "wake_time": wake_time_str,
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
