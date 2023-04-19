from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render



def index(request):
    return HttpResponse('<h1>Страница о сайте</h1>')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Отображение по категориям \n\t\t\t\t\t\t<p>{cat_id}</p></h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Ошибка! запрашиваемая страница отсутвует!!!! <p> pageNotFound</p> </h1>')


# def addpage(request):
#     return HttpResponse('<h1>Отображение по категориям</h1>')
# def show_categories(request):
#     return HttpResponse('<h1>Отображение по категориям</h1>')
# def about(request):
#     return HttpResponse('<h1>Отображение по категориям</h1>')