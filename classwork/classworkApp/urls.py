from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('music/', views.music),
    path('kendricklamar/', views.kendricklamar),
    path('jcole/', views.jcole),
    path('tankandthebangas', views.tankandthebangas)

]