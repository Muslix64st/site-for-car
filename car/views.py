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
    cats = Category.objects.all()
    context = {
            'posts': posts,
            'cats': cats,
            'menu': menu,
            'title': 'Главная страница',
            'cat_selected': 0,
    }
    return render(request, 'car/index.html', context=context)



def about(request):
    return render(request, 'car/about.html', {'menu': menu, 'title': 'О сайте'})
def add_page(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')
def contact(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')
def login(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')
def show_post(request, post_id):
    return HttpResponse(f'<h1>Отображение {post_id}</h1>')


def show_category(request, cat_id):
    posts = Car.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {
            'posts': posts,
            'cats': cats,
            'menu': menu,
            'title': 'Отображение по рубрикам',
            'cat_selected': cat_id,
    }
    return render(request, 'car/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Ошибка! запрашиваемая страница отсутвует!!!! <p> pageNotFound</p> </h1>')
