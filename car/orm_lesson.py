"""Справочное руководство ORM
выписываем основные команды"""

""" 
Car.objects.all()-------------выбирает все записи из таблицы сортировка такая же как и в классе мета
Car.objects.all()[:5]---------Срез берёт первые 5 записей
Car.objects.all()[3:8]--------Срез с 3 по 8

Car.objects.order_by('pk')----сортировка по PK
Car.objects.order_by('title')-сортировка по имени или можно ставить любое поле из таблицы
Car.objects.all().reverse()---Выведет в обратном порядке
Car.objects.get(pk=2) одна запись у которой PK=2 возвращает ЭКЗЕМПЛЯР


w = Car.objects.get(pk=1) создаём переменную в которой нам доступны все поля что в модели

w.cat
        ссылка на экземпляр класса categoty потому что cat связанна c категорией 
        в которой определён магический метод __str__ который возвращает имя категории а если это так томы можем достучаться 
        к любому полю связанной категории

w.cat.name 
            обращаемся к полю name категории category которая связанна с CAT

c = Category.objects.get(pk=1) читаем первую запись в таблице  

c.car_set.all() через переменную С мы обращаемся в модели car и выбираем все посты связанные с PK=1 yf 
                на примере можно увидеть что выдаст все записи мини автомобили
аналогично можно обратится к этому параметру если в связанной категории указан параметр
related_name='имя параметра' тогда можно обращаться через него c.'имя параметра'.all()

______________________________________  ЛУКАПЫ  ________________________________________________________

car.objects.filter(pk__gt=2) выбирает все записи у которых PK больше или равен 2 возвращает коллекцию queriset
Car.objects.filter(pk__lte=2) выведет все записи у которых PK меньше или равен 2 возвращает коллекцию queriset

Car.objects.filter(title__contains='м') возвращает все записи в заголовках которых встречается буква М 
                                        но можно указать и слово и слог
Car.objects.filter(title__icontains='М') делает всё то же самое только без учёта регистра 
                                        плохо работает или не работает если указан верхний регистр
                                        в SQLite потому что она не поддерживает верхний регистр не ASCI символов
                                        ну а с латинскими происходит регитсронезависимый поиск
Car.objects.filter(pk__in=[2,5,12,14])  позволяет указывать через список выбираемые записи по значениям можно указывать вборку
                                        по любому из доступных полей
                                        
Car.objects.filter(pk__in=[2,5,12,14], is_published=True) вторым и последующим (можно несколько)
                                                          параметром можно указать дополнительное условие, также общее условие 
                                                          будет истино если истино каждое из условий сдесь работает AND
                                                        
Car.objects.filter(cat__in=[2,3]) здесь уже происходит обращение к связанной записи Category и выдаст нам все записи
                                  связанные с выбранными критериями (тоесть ВСЕ записи их может быть много тут можно
                                  задавать второй параметр фильтрации записи)
cats = Category.objects.all()  выбираем все записи и передаём в переменную
Car.objects.filter(cat__in=cats) теперь через фильтр выбираем все связанные записи в модели CAR все связанные записи которые есть
                                 в CATEGORY
                                 
-------------------------------------------------------------------------------------------------------------------------                                 
from django.db.models import Q  импортировать класс Q для работы с логическими операторами

~   логическое НЕ (приоритет 1)
&   логическое И  (приоритет 2)
|   логическое НЕ (приоритет 3)     


Car.objects.filter(pk__lt=5, cat_id=2) выбираем все записи у которых первичный ключ меньше или равен 5  pk__lt=5
                                       и те записи которые принадлежат ко второй категории  cat_id=2

Car.objects.filter(Q(pk__lt=5) | Q(cat_id=2)) выполняется логический оператор ИЛИ 
                                             (Q(pk__lt=5) или Q(cat_id=2))

Car.objects.filter(Q(pk__lt=5) & Q(cat_id=2)) логический оператор И только если 2 условия истины
        тоже самое что  
Car.objects.filter(pk__lt=5, cat_id=2)


Car.objects.filter(~Q(pk__lt=5) & Q(cat_id=2)) тут работаем от обратного выборка происходит всех записей при PK>5 
                                               И cat_id=2

Car.objects.filter(~Q(pk__lt=5) | Q(cat_id=2)) выборка происходит всех записей при PK>5 или (cat_id=2)   
_______________________________________________________________________________________________________________________________

first()
last()


Car.objects.first()   возвратит первую запись в базе данных      
Car.objects.order_by('pk')first()  сперва сортируем по какому то полю потом уже после сортировки берём первую запись
Car.objects.order_by('-pk')first()  сперва сортируем по какому то полю в обратном порядке 
                                    потом уже после сортировки берём первую запись
Car.objects.last() берёт последнюю запись в БД
Car.objects.order_by('pk')last()  сортирует и берёт последнюю запись

___________________________________________________________________________________________________________________________________
latest()
earliest()

Если в таблице присутствуют поля привязанные ко времени создания или обновления!!!!!

Car.objects.latest('time_update') в этом случае выдаст запись которая была добавлена самой первой
Car.objects.earliest('time_update') которая была добавлена самой последней

________________________________________________________________________________________________________________________

get_previous
get_next

plot = Car.objects.get(pk=7) делаем выборку из таблицы по заданному условию (можно по разным полям) 

plot.get_previous_by_time_update() берёт предыдущую запись относительно времени обновления 
plot.get_previous_by_time_create() берёт предыдущую запись относительно времени создания
plot.get_next_by_time_update()     берёт следующую запись относительно времени обновления
plot.get_next_by_time_create()     берёт следующую запись относительно времени создания

plot.get_next_by_time_create(pk=10) получить следующую запись но только такую у которой pk больше 10
                                    можно также прописывать и более сложные условия сортировки или представления
                                    
______________________________________________________________________________________________________________________

exists() - проверка существования записи
count() - получения числа записей

cs = Category.objects.get(pk=2) берём записи из категории РК = 2
cs.car_set.exists() проверяем пустая категория или нет
cs.car_set.count() смотрим сколько записей привязано ко второй категории РК = 2

Car.objects.filer(pk__gt=4).count() выбрать все записи РК=>4 и вывести количество этих записей
                                    
______________________ Обращение к полю модели через атрибут___________________________________________________э

Car.objects.filter(cat__slug='mini-avtomobili') обращаемся через модель CAR и её полю CAT которая связанна с другой
                                                моделью CATEGORY и через неё мы обращаемся к атрибуту slug 
                                                равный тому что указано в ковычках. Результатом будет все объекты CAR
                                                которые связанны с это категорией 
Car.objects.filter(cat__in=[1])  то же самое сто написано выше только тут указали явно что брать 1 категорию

Car.objects.filter(cat__name='маленькие автомобили')  тут тоже самое только обращаемся к name
Car.objects.filter(cat__name__contains='Ы') выбрать все имена из категорий в именах категорий  присутствует буква Ы
+++++++++
Category.objects.filter(car__title__contains='ли') через первичную модель (Category) обращаемся к модели CAR в которой
                                                   выбираем все заголовки title в которых присутствует фрагмент строки ли
                                                   и на выходе мы получим КАТЕГОРИИ

Category.objects.filter(car__title__contains='ли').distinct() тоже самое только нам не вывалит кучу категорий а отобразит
                                                                уникальные записи


____________________________________ Агркгирующие функции ___________________________________________

from django.db.models import *

Car.objects.aggregate(Min('cat_id')) возвращает минимальный ID (то есть мин количество связанных категорий cat_id) 
{'cat_id__min': 1}

Car.objects.aggregate(Max('cat_id')) возвращает сколько всего связанных категорий 
Car.objects.aggregate(Max('pk')) вернёт общее количество записей в категории кар

Car.objects.aggregate(Min('cat_id'), Max('cat_id')) можно сразу вывести и два значения
    {'cat_id__min': 1, 'cat_id__max': 2}
    получаем словарь

Car.objects.aggregate(cat_min=Min('cat_id'), cat_max=Max('cat_id'))
        {'cat_min': 1, 'cat_max': 2}
        получаем словарь с другими ключами
        
        
_____________________________________VALUES______________________

Car.objects.values('title', 'cat_id').get(pk=1)  выбрать запись РК=1 и выбрать только поля указанные в параметрах values        

Car.objects.values('title', 'cat__name').get(pk=1) Взять первое поле и взять у него заголовок и категорию к которой он относится
        {'title': 'Hong Guang Mini EV', 'cat__name': 'Мини-автомобили'}

Car.objects.values('title', 'cat__name') Выбрать все поля title и связанные cat__name выдаст список словарей

можно потом этот словарь и циклом крутить
spoilt = Car.objects.values('title', 'cat__name')
for row in spoilt:
    print(row['title'], row['cat__name'])
       
Aixam Minauto Мини-автомобили
Buddy Electric Мини-автомобили
Daewoo Matiz Маленькие автомобили
Fiat 500 Мини-автомобили
Hong Guang Mini EV Мини-автомобили
Mahindra e2o Мини-автомобили
Peel P50 Мини-автомобили
Peel Trident Мини-автомобили
Renault Twizy Мини-автомобили
Reva G-Wiz Мини-автомобили
Smart ForTwo Мини-автомобили
Toyota Yaris Маленькие автомобили
Volkswagen Polo Маленькие автомобили
Ариана гранд Мини-автомобили
    


_________________________________---Групировка записей агрегирующей функцией---_______________________________

Обязательно проверить чтобы в моделях в классе мета была выключена сортировка (можно просто закоментить)

Car.objects.values('cat_id').annotate(Count('id'))
<QuerySet [{'cat_id': 1, 'id__count': 11}, {'cat_id': 2, 'id__count': 3}]>
                                                на выходе увидим сколько записей принадлежит к каждой категории
                                            
c = Category.objects.annotate(Count('car')) если в качестве параметра укажем имя вторичной модели то получим все рубрики
                                            то есть категории но также получим атрибут  car__count
                                             через который можем видеть количество связанных с ней записей


>>> c[3].car__count  можем обращаться чтобы видеть кол-во связанных с ней записей
11

c = Category.objects.annotate(total=Count('car')).filter(total__gt=0)
                                        выбираем все рубрики с фильтром (количество записей больше нуля
<QuerySet [<Category: Маленькие автомобили>, <Category: Мини-автомобили>]>


________________________________________---F клас---_____________________________________
from django.db.models import F

Искуственный пример. Допустим у нас есть поле в таблице которое хранит кол-во просмотров поста
и нам при каждом просмотре нужно увеличить кол-во просмотров допусти на 1 тогда можно выполнить
следующий запрос........(этот пример отлично подходит и используется в социальных сетях

Car objects.filter(slug='xxxxxx').update(views=F('views')+1) Тут обращаемся к определённому полю по слагу и обновляем значение


___________________________________---Length---________________________________________________

from django.db.models.functions import Length

ps = Car.objects.annotate(len=Length('title')) тут получаем queryset со всеми заголовками но также и ещё одним параметром
                                                который прокрутим в цикле
                                                
for x in ps:
    print(x.title, x.len) 
                                               
Aixam Minauto 13
Buddy Electric 14
Daewoo Matiz 12
Fiat 500 8
Hong Guang Mini EV 18
Mahindra e2o 12
Peel P50 8
Peel Trident 12
Renault Twizy 13
Reva G-Wiz 10
Smart ForTwo 12
Toyota Yaris 12
Volkswagen Polo 15


____________________________________---RAW SQL---__________________________________________

Car.objects.raw('SELECT * FROM car_car')



__________________Обработка данных связанных таблиц
From django.db import connection Импорт модуля
connection.queries просмотр запросов
"""