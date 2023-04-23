from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *



#_____________________________________________



class CarHome(ListView):
    model = Car
    template_name = 'car/index.html'
    context_object_name = 'posts' # или переделать в index----- for p in object_list
    extra_context = {'title': 'Главная страница',
                     'cat_selected': 0}  # через этот параметр только неизменяемые данные передавать

    def get_queryset(self):
        return Car.objects.filter(is_published=True)

    """следующая функция для передачи динамического контекста. В ней мы обращаемся к классу ListView чтобы не 
     затереть данные введённые выше (там уже 2 контекста есть). Функцию использовать не буду потому что
     я передал меню через пользовательские теги. В функции берём уже сформированный словарь через параметр kwargs
      распаковываем и добавляем меню(которое я убрал) """

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = menu
    #     return context



#_____________________________________________

def about(request):
    return render(request, 'car/about.html', {'title': 'О сайте'})

#_____________________________________________

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'car/addpage.html'
    extra_context = {'title': 'Добавление статьи'}
    #success_url = reverse_lazy('home') # перенаправление после добавления если отсутствует get_absolute_url

#_____________________________________________

def contact(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')

#_____________________________________________

def login(request):
    return HttpResponse('<h1>Отображение по категориям</h1>')

#_______________________________________кнопка читать пост___________________________________________

class ShowPost(DetailView):
    model = Car
    template_name = 'car/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    extra_context = {'title': 'Статья'}

#_______________________________________ отображение по категориям ___________________________________________

class CarCategory(ListView):
    model = Car
    template_name = 'car/index.html'
    context_object_name = 'posts' # или переделать в index----- for p in object_list
    allow_empty = False
    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)  # №15   15минута
        context['cat_selected'] = context['posts'][0].cat_id
        return context

#_____________________________________________

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Ошибка! запрашиваемая страница отсутвует!!!! <p> pageNotFound</p> </h1>')

#_________________________________________________функции______________________________________________


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
