from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from mood.models import Mood
from mood.forms import MoodForm

def index(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    form1 = CityForm()
    form2 = MoodForm()

    # if request.method == 'POST': # only true if form is submitted
    #     form = CityForm(request.POST) # add actual request data to form for processing
    #     form2 = MoodForm(request.POST)
    #     form.save() # will validate and save if validate

    if request.method == 'POST':
        form1 = CityForm(request.POST, prefix='city')
        if form1.is_valid():
            form1.save()
            print("form1 looking nice")
    else:
        form1 = CityForm(prefix='city')
        print("bottom text")

    if request.method == 'POST' and not form1.is_valid():
        form2 = MoodForm(request.POST, prefix='mood')
        form1 = CityForm(prefix='city')
        if form2.is_valid():
            form2.save()
            data = request.POST.copy()
            mood = data.get('mood')
            print("come on set the mood i got candles")

    else:
        form2 = MoodForm(prefix='mood')
        print("mood BROKE")

    weather_data = []
    data = request.POST.copy()
    mood = data.get('mood')

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    print(mood)
    print(city)

    context = {'weather_data' : weather_data, 'form1' : form1, 'form2': form2, 'mood': mood}

    return render(request, 'weather/index.html', context) #returns the index.html template
