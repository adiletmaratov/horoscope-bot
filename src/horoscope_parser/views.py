from django.shortcuts import render


def index(request):
    template = 'horoscopes/index.html'
    return render(request, template)
