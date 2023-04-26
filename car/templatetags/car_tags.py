# from django import template
# from car.models import *
#
#
# """Создаём экземпляр класса template.Library()
# через который происходит регистрация собственных шаблонных тегов"""
# register = template.Library()
#
#
# #_______________________________________________ Sidebar слева (Категории)______________________________________
#
# """Функция для работы тега
#  Декоратор используется для связи функции с тегом"""
# # @register.simple_tag(name="get_cats") # указываем имя в декораторе через которое будем обращаться к функции
# # def get_category(filter=None):
# #     if not filter:
# #         return Category.objects.all()
# #     else:
# #         return Category.objects.filter(pk=filter)
# #
#
# """Включающий тег который возвращает фрагмент HTML  страницы
# вс1 что возвращает функция отправляется в list_categories
# если переданы данные по сортировке то выполнится второе условие
# если нет нет то просто вернётся переменная cats"""
# # @register.inclusion_tag('car/list_categories.html')
# # def show_categories(sort=None, cat_selected=0):
# #     if not sort:
# #         cats = Category.objects.all()
# #     else:
# #         cats = Category.objects.order_by(sort)
# #
# #     return {'cats': cats, 'cat_selected': cat_selected}
#
# #______________________________________________end Sidebar слева_____________________________________
#
# #_____________________________________________menu сверху____________________________________________
#
# # @register.inclusion_tag('car/list_menu.html') # указываем имя в декораторе через которое будем обращаться к функции
# # def show_menu():
# #     menu = [
# #         {'title': 'О сайте', 'url_name': 'about'},
# #         {'title': 'добавить статью', 'url_name': 'add_page'},
# #         {'title': 'Обратная связь', 'url_name': 'contact'},
# #         {'title': 'Войти', 'url_name': 'login'}
# #     ]
# #
# #     return {'menu': menu}
#
