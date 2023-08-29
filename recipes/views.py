# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('home 2')


def contacto(request):
    return HttpResponse('contacto 2')


def sobre(request):
    return HttpResponse('sobre')
