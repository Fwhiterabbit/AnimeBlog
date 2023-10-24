from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SearchForm(forms.Form):
    author = forms.CharField(required=False)
    title = forms.CharField(required=False)