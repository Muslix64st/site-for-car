from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *



urlpatterns = [
    path('', CarHome.as_view(), name="home"),
    path('about/', about, name="about"),
    path('add_page/', AddPage.as_view(), name="add_page"),
    path('contact/', ContactFormView.as_view(), name="contact"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),  # RegisterUser.as_view
    path('post/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>/', CarCategory.as_view(), name="category"),
]

handler404 = pageNotFound