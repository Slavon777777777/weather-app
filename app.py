from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "3f2a0969bbc5747a5739dbabd6ca1f35"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            weather = {"error": "City not found"}
        else:
            weather = {
                "city": city,
                "temp": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "wind": round(data["wind"]["speed"] * 3.6, 1),
            }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
