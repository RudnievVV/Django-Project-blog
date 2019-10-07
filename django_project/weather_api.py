import requests, time, os

while True:
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Kiev&units=metric&APPID=ace95de816c519aeb2ef9f0bec1a0b42')
    r.raise_for_status()

    os.chdir(".\\blog\\templates\\blog")
    with open('weather.html', 'w') as weather:
        weather.write(f"""
<p>City: {r.json().get("name")}</p>
<p>Weather Description: <img src="http://openweathermap.org/img/wn/{r.json().get("weather")[0].get("icon")}@2x.png" height="30" width="30"> -- {r.json().get("weather")[0].get("main")} -- {r.json().get("weather")[0].get("description")}</p>
<p>Temprature: {r.json().get("main").get("temp")} Celsius</p>""")

    time.sleep(180)
