"""
URL configuration for allcar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.core.files.storage import handler
from django.urls import path
from .views import *



urlpatterns = [
    path('', index,name="home"),                        #http://127.0.0.1:8000/
    path('about/', about, name="about"),  #http://127.0.0.1:8000/cats/
    path('add_page/', add_page, name="add_page"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('post/<int:post_id>', show_post, name="post"),
    path('cats/<int:cat_id>/', categories, name="categories"),  # http://127.0.0.1:8000/cats/
]

handler404 = pageNotFound