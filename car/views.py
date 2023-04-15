from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse('<h1>Страница о сайте</h1>')


def categories(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')
def addpage(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')
def show_categories(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')
def about(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')