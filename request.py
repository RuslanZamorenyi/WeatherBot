import requests

MY_KEY = '5db13c2dafdec432fc7cb0d56ba30025'


def check_weather(city_name):
    location = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_KEY}').json()
    coordinate = location.get('coord')
    lat = coordinate.get('lat')
    lon = coordinate.get('lon')

    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={MY_KEY}').json()

    temperature = round(weather.get('main')['temp'] - 273)
    feels_like = round(weather.get('main')['feels_like'] - 273)
    description = weather.get('weather')[0]['description']

    description = f'temperature {temperature} ℃, feels_like {feels_like} ℃, {description}'
    return description

