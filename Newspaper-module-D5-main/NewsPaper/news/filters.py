from django import forms
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author
import django_filters


class PostFilter(django_filters.FilterSet):
   dateCreation = django_filters.DateFilter(
           field_name='dateCreation',
           label='Дата создания позже чем',
           lookup_expr='gte',
           widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'}),
           input_formats=['%d-%m-%Y', '%d-%m','%m', '%d', '%m-%Y', '%Y-%m-%d', '%Y-%m', '%m-%d', '%d.%m.%Y']
       )
   title = CharFilter(field_name='title', label='Заголовок', lookup_expr='icontains')
   author = ModelChoiceFilter(field_name='author', label='Автор', lookup_expr='in', queryset=Author.objects.all())

   class Meta:
        model = Post
        fields = ['dateCreation', 'title', 'author']