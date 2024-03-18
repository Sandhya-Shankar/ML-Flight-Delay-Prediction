import datetime as dt 
import requests

def get_weather(city_name):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": 'f6346ce895c84998a9a151805232107',
        "q": city_name,
        "days": 1,  # Request 7-day forecast
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
call = get_weather('London')
def get_values():
    i = time
    mini_info = data['forecast']['forecastday'][0]['hour'][i]

    windspeedkmph = mini_info['wind_kph']
    winddirDegree = mini_info['wind_degree']
    precipMM = mini_info['precip_mm']
    visibility = mini_info['vis_km']
    pressure = mini_info['pressure_mb']
    DewPointF =  mini_info['dewpoint_f']
    cloudcover = mini_info['cloud']
    WindGustKmph = mini_info['gust_kph']
    tempF = mini_info['temp_f']
    WindChillF = mini_info['windchill_f']
    humidity = mini_info['humidity']
    time = str(i)+'00'
    
    return ''
