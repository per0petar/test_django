# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from .models import Posts
from .forms import PostForm, RawPostForm
# Create your views here.

def view_posts(request):
    posts = Posts.objects.all()  # we can add "[:10]" to show maximum of 10 posts

    context = {
        'posts': posts
    }
    return render(request, 'posts/view_post.html', context)

# def post_create_view(request):
#     my_form = RawPostForm()
#     if request.method == "POST":
#         my_form = RawPostForm(request.POST)
#         if my_form.is_valid():
#             Posts.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, "posts/create_post.html", context)

def post_create_view(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post_instance = form.save(commit=False) # https://stackoverflow.com/questions/53237454/putting-username-of-logged-in-user-as-label-in-django-form-field
            post_instance.author=request.user
            post_instance.save()
            return redirect("posts:view_posts")
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, "posts/create_post.html", context)

def detail_view(request, post_id):
    #post = Posts.objects.get(id=post_id)
    post = get_object_or_404(Posts, id=post_id)
    context = {
        'post': post
    }
    return render(request, "posts/details.html", context)