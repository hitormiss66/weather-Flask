from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
app.debug = True
api_key = 'd07ee60072584de23c4ef0e2626af8dc'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/weather', methods=['POST', 'GET'])
def weather():
    global weather, temp, city
    if request.method == 'POST':
        city = request.form["city"]
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
        weather = weather_data.json()['weather'][0]['main']
        temp = weather_data.json()['main']['temp']
        return redirect(url_for('result'))
    else:
        'something wrong i guess'

    return render_template('weather.html')

@app.route('/weather/result')
def result():
    return f'{weather} in {city}. Currently {round(temp)}°F'

if __name__ == '__main__':
    app.run()
