from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts2 = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts2})

def post_detail(request, pk):
    post3 = Post.objects.get(pk=pk)
    return render(request, 'blog/post_examp.html', {'post': post3})
