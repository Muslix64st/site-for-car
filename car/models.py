from django.db import models
from django.urls import reverse


# Create your models here.

#_________________________________________clas car________________________________________________________________
class Car(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_crete = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['title', 'time_crete'] # Сортировка по


#_________________________________________clas Category________________________________________________________________
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'
        ordering = ['id'] # Сортировка по



#_________________________________________end clas Category____________________________________________________________