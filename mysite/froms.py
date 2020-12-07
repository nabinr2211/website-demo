from django import forms
from mysite.models import *


class AddPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
