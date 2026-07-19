from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)

API_KEY = os.getenv("a2c89d49f756c57270b4d334a836fee3")

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                weather = response.json()
            else:
                weather = {"error": "City not found"}
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
