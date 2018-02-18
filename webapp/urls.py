from django.urls import path

from . import views, bot

urlpatterns = [
    path('msg', bot.processMessage, name='sendMessage'),
    path('', views.index, name='index'),
]
