from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    if request.method == "POST":
        city = request.form.get("city", "Chennai")  # safe default
        if api_key:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    weather = response.json()
                else:
                    weather = {"error": "City not found"}
            except Exception as e:
                weather = {"error": str(e)}
        else:
            weather = {"error": "API key not set"}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
