from django.forms import ModelForm
from django import forms
from .models import *   
class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'body' : 'caption ',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'add a caption......', 'class': 'font1 text-4xl'},)
        }


class PostEditForm(ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'body' : 'aption',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'add a caption......', 'class': 'font1 text-4xl'},)
        }
