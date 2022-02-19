from django.shortcuts import render
from django.http import HttpResponse
from .models import Games
from .filters import Filters


def home(request):
    games = Games.objects.all()[20:24]
    context = {
        'games': games,
    }
    return render(request, 'index.html', context)


def games(request, cat=None):
    if cat:
        if cat == "*":
            games = Games.objects.filter().order_by('title')
        elif cat == "pc":
            games = Games.objects.filter(console="pc").order_by('title')
        elif cat == "ps":
            games1 = Games.objects.filter(console="ps3").order_by('title')
            games2 = Games.objects.filter(console="ps4").order_by('title')
            games = games1 | games2
        elif cat == "xbox":
            games = Games.objects.filter(console="xbox").order_by('title')
        else:
            pass
    context = {
        'games': games
    }

    return render(request, 'store.html', context)


def game(request, id):
    game = Games.objects.get(id=id)
    dict = {'game': game}
    return render(request, 'game.html', dict)
