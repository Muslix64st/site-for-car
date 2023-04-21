from django import forms
from .models import *

#_________________________________________________________________________
"""Класс создания формы"""
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=250)
    slug = forms.SlugField(max_length=250)
    content = forms.CharField(widget=forms.Textarea(attrs={'color': 60, 'row': 10}))
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
