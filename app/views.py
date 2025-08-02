from django.shortcuts import render
import requests

# Create your views here.
def index(request):

    city=request.GET.get('city', 'Bangalore')  # Default to Bangalore if no city is provided

    api_key = '3bea7a605bfaee022aaf1d356818e986'

    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    print(api_url)

    api=requests.get(api_url).json()

    temperature = api['main']['temp']
    country = api['sys']['country']
    city = api['name']


    return render(request, 'index.html',{
        'temperature': temperature,
        'country': country,
        'city': city
    })
