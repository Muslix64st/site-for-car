
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import *
from .models import *
from .utils import *


#_____________________________________________


class CarHome(DataMixin, ListView):
    model = Car
    template_name = 'car/index.html'
    context_object_name = 'posts' # или переделать в index----- for p in object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Главная страница')

        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'car/about.html', {'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'car/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')


def login(request):
    return HttpResponse('<h1>Сюда попали после регистрации</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'car/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))




class ShowPost(DataMixin, DetailView):
    model = Car
    template_name = 'car/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))



class CarCategory(DataMixin, ListView):
    model = Car
    template_name = 'car/index.html'
    context_object_name = 'posts' # или переделать в index----- for p in object_list
    allow_empty = False
    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))




def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Ошибка! запрашиваемая страница отсутвует!!!! <p> pageNotFound</p> </h1>')





# def index(request):
#     posts = Car.objects.all()
#     cats = Category.objects.all()    # это вытаскиваю из car_tags
#     context = {
#             'posts': posts,
#             'title': 'Главная страница',
#             'cat_selected': 0,
#     }
#     return render(request, 'car/index.html', context=context)




# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)  # request.FILES для сохранения фото + изменить в шаблоне addpa
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#             # try:
#             #     Car.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста') #  ошибка отправляется в addpage
#     else:
#         form = AddPostForm()
#     return render(request, 'car/addpage.html', {'form': form,'title': 'Добавление статьи'})


# def show_post(request, post_slug):
#     post = get_object_or_404(Car, slug=post_slug)
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'car/post.html', context=context)


# def show_category(request, cat_slug):  #  cat_id)
#     posts = Car.objects.filter(cat__slug=cat_slug)   #cat_id=cat_id
#     #posts = Car.objects.all()             # это вытаскиваю из car_tags
#     context = {
#             'posts': posts,
#             'title': 'Отображение по рубрикам',
#             'cat_selected': cat_slug,   #cat_id
#     }
#     return render(request, 'car/index.html', context=context)
