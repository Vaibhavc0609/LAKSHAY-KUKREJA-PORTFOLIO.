from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost

def home(request):
    return render(request, 'pages/index.html')

def podcasts(request):
    return render(request, 'pages/podcasts.html')

def Blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'pages/blog.html', {'posts': posts})

def collaborate(request):
    return render(request, 'pages/collaborate.html')

@login_required
def blog_create(request):
    if not request.user.is_staff:
        return redirect('blog')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        BlogPost.objects.create(title=title, content=content, image=image)
        return redirect('blog')
    return redirect('blog')

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'pages/blog_detail.html', {'post': post})
@login_required
def blog_delete(request, pk):
    if not request.user.is_staff:
        return redirect('blog')
    post = BlogPost.objects.get(pk=pk)
    post.delete()
    return redirect('blog')