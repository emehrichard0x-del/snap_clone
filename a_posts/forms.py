from django.forms import ModelForm
from django import forms
from .models import *   
class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'body' : 'caption ',
            'tags' : 'category'
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'add a caption......', 'class': 'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }


class PostEditForm(ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'body' : 'caption',
            'tags' : "category"
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'add a caption......', 'class': 'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }
