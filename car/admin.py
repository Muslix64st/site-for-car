from django.contrib import admin
from .models import *

"""класс для отображения в админке дополнительных полей
все нужные поля перечисляются в классе, 
его нужно обязательно зарегистрировать вторым параметром"""

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_crete', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',) # Список полей доступных для редактирования в админке
    list_filter = ('is_published', 'time_crete')  # Фильтрация по полям (фильтр добавляется сбоку)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)



"""Регистрация приложений 
для отображения в админке сайта """
admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)