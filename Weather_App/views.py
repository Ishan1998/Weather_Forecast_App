from django.shortcuts import render, redirect
import requests


def updateWeather(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
        w_dataset = requests.get(url).json()

        data = {
            "name" : str(w_dataset['name']),
            "country": str(w_dataset['sys']['country']),
            "temp": str(w_dataset['main']['temp']) + ' °C',
            "feels_like": str(w_dataset['main']['feels_like']),
            "temp_min": str(w_dataset['main']['temp_min']),
            "temp_max": str(w_dataset['main']['temp_max']),
            "pressure": str(w_dataset['main']['pressure']),
            "humidity": str(w_dataset['main']['humidity']),
            'main': str(w_dataset['weather'][0]['main']),
            'description': str(w_dataset['weather'][0]['description']),
            'icon': w_dataset['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "Weather.html",data)
        