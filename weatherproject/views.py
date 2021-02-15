from pyowm import OWM
from pyowm.utils.config import get_default_config
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	config_dict = get_default_config()
	config_dict['language'] = 'ru'
	owm  =  OWM ( '31ae8e85189cd152c46bc5ed6d5ee01d', config_dict)

	city = request.GET['city_user']

	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	w = observation.weather

	temp = w.temperature('celsius')["temp"]
	windSpeed = w.wind()["speed"]
	windDeg = w.wind()["deg"]
	humidity = w.humidity
	windDegTop = windDeg(humidity)

	return render(request, 'home.html', {'temp':temp})