from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Car
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo',  'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows':10}),
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title



"""Класс создания формы"""
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=250, label='Заголовок')
#     slug = forms.SlugField(max_length=250, label='slug_url')
#     content = forms.CharField(widget=forms.Textarea(attrs={'color': 60, 'row': 10}), label='Статья')
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
