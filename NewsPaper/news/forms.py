from django import forms
from django.forms import ModelForm
from .models import Post, Author, Category


# Создаём модельную форму
class PostForm(ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Автор")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория")
    title = forms.CharField(label="Заголовок", max_length=128)
    text = forms.CharField(label="Текст", widget=forms.Textarea)

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'text')
