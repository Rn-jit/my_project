import os
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from myapp.forms import MadlibForm, Madlib2Form
from pytube import YouTube
import json
import urllib.request

from myapp.models import Madlib, Madlib2


def home(request):
    return render(request, 'home.html')


def youtube(request):
    if request.method == 'POST':
        try:
            Path = os.path.expanduser("~") + "/Downloads/"
            url = request.POST.get('link')
            yt = YouTube(url)
            thumbnail = yt.thumbnail_url
            title = yt.title
            stream = yt.streams.first()
            stream.download(Path)
            messages.info(request, 'Video Downloaded! Please Check Your Download Directory')
            return render(request, 'youtube.html', {'thumbnail': thumbnail, 'title': title})
        except:
            messages.info(request, 'Please Enter Correct URL')
            return redirect('myapp:youtube')
    return render(request, 'youtube.html')


def chat(request):
    return render(request, 'chat.html')


def currency_convert(request):
    context = {}
    url = urllib.request.urlopen('https://api.exchangeratesapi.io/latest')
    document = json.loads(url.read().decode())
    rate = document['rates']
    country = list(rate)
    context['rate'] = rate
    context['country'] = country
    if request.method == 'POST':
        From = request.POST['source_country']
        To = request.POST['destination_country']
        amount = request.POST['amount']
        amount = float(amount)
        url = urllib.request.urlopen('https://api.exchangeratesapi.io/latest?base=' + From + '&symbols=' + To)
        doc = json.loads(url.read().decode())
        rates = doc['rates']
        for key, value in rates.items():
            convert = value * amount
            context['exchange'] = convert
        context['from'] = From
        context['to'] = To
        context['amount'] = amount
        return render(request, 'currency_exchange.html', context)
    else:
        return render(request, 'currency_exchange.html', context)


def weather(request):
    context = {}
    if request.method == 'POST':
        city = request.POST['city']
        city = city.title()
        url = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=74fba27056f2592c94d4686c83d48238&units=metric')
        document = json.loads(url.read().decode())
        weather = document['weather'][0]['main']
        desr = document['weather'][0]['description']
        icon = document['weather'][0]['icon']
        temp = document['main']['temp']
        wind = document['wind']['speed']
        humidity = document['main']['humidity']
        clouds = document['clouds']['all']
        weather_info = {
            'city' : city,
            'date': datetime.now(),
            'weather': weather,
            'desr': desr,
            'icon': icon,
            'temp': temp,
            'wind': wind,
            'humidity': humidity,
            'clouds': clouds,
        }
        context['weather_info'] = weather_info
    return render(request, 'weather.html', context)


def madlibs(request):
    context = {}
    forms = MadlibForm()
    context['forms'] = forms

    if request.method == 'POST':
        forms = MadlibForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            data = Madlib.objects.all().last()
            context['data'] = data
            return render(request, 'madlibs.html', context)

    return render(request, 'madlibs.html', context)


def madlibs2(request):
    context = {}
    form = Madlib2Form()
    context['form'] = form
    if request.method == 'POST':
        form = Madlib2Form(request.POST or None)
        if form.is_valid():
            form.save()
            data = Madlib2.objects.all().last()
            context['data'] = data
            return render(request, 'madlib2.html', context)

    return render(request, 'madlib2.html', context)