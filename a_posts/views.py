from django.shortcuts import render,redirect,get_object_or_404
from .forms import *


from django.contrib import messages



# Create your views here.
def home_views(request, tag=None):

    if tag:
         posts = Post.objects.filter(tags__slug=tag)
         tag = get_object_or_404(Tag, slug=tag)
    else:

        posts = Post.objects.all()


    categories = Tag.objects.all()

    context = {
        'posts' : posts,
        'categories' : categories,
        'tag' : tag
    }

    return render(request, 'a_posts/home.html',context )


def post_create_view(request):
    return render(request, 'a_posts/post_create.html')





"""
def category_view(request,tag):
    posts = Post.objects.filter(tags__slug=tag)
    return render(request, 'a_posts/home.html',{'posts' : posts})
"""




def post_create_view(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect('home')
    return render(request, 'a_posts/post_create.html', {'form' : form})



def post_delete_view(request,pk):

    #post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'post deleted')
        return redirect('home')
    return render(request, 'a_posts/post_delete.html', {'post':post})



def post_edit_view(request, pk):
    #post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post )

    if request.method == "POST":
        form = PostEditForm(request.POST,instance=post )
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated')
            return redirect('home')
    context = {
        'post' : post,
        'form' : form
    }
    return render(request, 'a_posts/post_edit.html',context )



def post_page_view(request, pk):
   # post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=pk)
    return render(request, 'a_posts/post_page.html',{'post':post})