from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(max_length=30)

    class Meta:
        model=Post
        fields=('post',)
