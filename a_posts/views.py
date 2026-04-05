from django.shortcuts import render,redirect
from .models import *

from django.forms import ModelForm
from django import forms

from django.contrib import messages



# Create your views here.
def home_views(request):
     posts = Post.objects.all()
     return render(request, 'a_posts/home.html',{'posts' : posts})


def post_create_view(request):
    return render(request, 'a_posts/post_create.html')



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


def post_create_view(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'a_posts/post_create.html', {'form' : form})



def post_delete_view(request,pk):

    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'post deleted')
        return redirect('home')
    return render(request, 'a_posts/post_delete.html', {'post':post})



def post_edit_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'a_posts/post_edit.html',{'post': post})