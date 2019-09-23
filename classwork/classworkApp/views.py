from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")

def music(request):
    return HttpResponse('Welcome to the music page! Go to one of the following routes: kendricklamar,jcole,or tankandthebangas')

def kendricklamar(request):
    return HttpResponse('Kendrick Lamar is an American rapper from Compton,CA. His music is a reflection of himself and his childhood residence.')
def jcole(request):
    return HttpResponse('Jermaine Cole aka J. Cole is from Fayetteville,NC. He is the founder of the music label, Dreamville. ')
def tankandthebangas(request):
    return HttpResponse('Tank and The Bangas are a soul/funk band from New Orleans. They were 1st discovered on NPR tiny Desk.')