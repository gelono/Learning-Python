import requests

URL = 'https://api.openweathermap.org/data/2.5/weather?'
KEY = '325ff0879cb768986c2ff03b7593da2f'
#city = input('Your city: ')


def get_weather(city: str) -> str:
    """
    The function returns the weather in specified city
    """
    options = {'q': city, 'appid': KEY, 'units': 'metric'}
    response = requests.get(url=URL, params=options)
    r_data = response.json()

    try:
        weather = r_data['weather']
        description = weather[0]['description']
        temp_data = r_data['main']
        t = temp_data['temp']
        pressure = temp_data['pressure']
        return f'temperature is {t}C, pressure is {pressure}, weather is {description}'
    except:
        return r_data['message']


if __name__ == "__main__":
    print(get_weather('kkk'))
