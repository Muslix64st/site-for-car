from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import *



def index(request):
    posts = Car.objects.all()
    cats = Category.objects.all()    # это вытаскиваю из car_tags
    context = {
            'posts': posts,
            'title': 'Главная страница',
            'cat_selected': 0,
    }
    return render(request, 'car/index.html', context=context)



def about(request):
    return render(request, 'car/about.html', {'title': 'О сайте'})


def add_page(request):
    return render(request, 'car/addpage.html',  {'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')
def login(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')

#_______________________________________кнопка читать пост___________________________________________
def show_post(request, post_slug):
    post = get_object_or_404(Car, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'car/post.html', context=context)


#_______________________________________ отображение по категориям ___________________________________________

def show_category(request, cat_slug):  #  cat_id)
    posts = Car.objects.filter(cat__slug=cat_slug)   #cat_id=cat_id
    #posts = Car.objects.all()             # это вытаскиваю из car_tags
    context = {
            'posts': posts,
            'title': 'Отображение по рубрикам',
            'cat_selected': cat_slug,   #cat_id
    }
    return render(request, 'car/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Ошибка! запрашиваемая страница отсутвует!!!! <p> pageNotFound</p> </h1>')
