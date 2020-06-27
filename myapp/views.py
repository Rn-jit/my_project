import os

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from pytube import YouTube
import json
import urllib.request


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
        url = urllib.request.urlopen('https://api.exchangeratesapi.io/latest?base='+From+'&symbols='+To)
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
