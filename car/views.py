from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},

]

def index(request):
    posts = Car.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'
    }
    return render(request, 'car/index.html', context= context)



def categories(request, cat_id): return HttpResponse(f'<h1>Отображение по категориям <p>{cat_id}</p></h1>')
def about(request): return render(request, 'car/about.html', {'menu': menu, 'title': 'О сайте'})

def add_page(request):return HttpResponse('<h1>Отображение по категориям</h1>')


def contact(request):return HttpResponse('<h1>Отображение по категориям</h1>')


def login(request):return HttpResponse('<h1>Отображение по категориям</h1>')


def show_post(request, post_id): return HttpResponse(f'<h1>Отображение {post_id}</h1>')




def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Ошибка! запрашиваемая страница отсутвует!!!! <p> pageNotFound</p> </h1>')
