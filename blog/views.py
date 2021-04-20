from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm


def home(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = CommentForm()

    context = {
        'posts':Post.objects.all(),
        'form': form
    }
    return render(request, "blog/home.html", context)


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, "blog/form_input.html", context)