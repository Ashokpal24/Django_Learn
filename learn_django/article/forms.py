from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Article
from tag.models import Tag


class ArticleForm(forms.ModelForm):
    author_name = forms.CharField(
        label="Author",
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'tags',
        ]

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs) -> None:
        user = kwargs.pop('user', None)
        super(ArticleForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['author_name'].initial = user.username
