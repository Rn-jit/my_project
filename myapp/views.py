import os

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from pytube import YouTube


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







# if request.method == 'POST':
#     #     url = request.POST.get('link')
#     #     yt = YouTube(url)
#     #     context['title'] = yt.title
#     #     context['thumbnail'] = yt.thumbnail_url
#     #     context['stream'] = yt.streams.filter(progressive=True).all()