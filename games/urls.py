from django.urls import path
from django.conf.urls import url
from . import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('games/<str:cat>', v.games, name="games"),
    path('game/<int:id>', v.game, name="game"),
    #url(r'^findGame', v.findGame, name='findGame'),
    # path('new/',v.new)
]
