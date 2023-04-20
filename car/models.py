from django.db import models
from django.urls import reverse


# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_crete = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")


    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_id': self.pk})




class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")



    def __str__(self):
        return self.name

    # def get_absolut_url(self):
    #     return reverse('cat', kwargs={'catt_id': self.pk})