from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
    
    posts = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 5)  # 5 posts par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/home_page.html', {
        'page_obj': page_obj
    })


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'home/posts_details.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            return redirect('home:post_details', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'home/post_form.html', {
    'form': form,
    'title': 'Create Post'
})


@login_required
def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home:post_details', pk=post.pk)

    else:
        form = PostForm(instance=post)

    return render(request, 'home/post_form.html', {
    'form': form,
    'title': 'Edit Post'
})


@login_required
def post_delete(request, pk):
    
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'home/post_delete.html', {'post': post})

"""
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return HttpResponse("Post created successfully")
    return render(request, 'home/post_create.html')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        return HttpResponse("Post updated successfully")

    return render(request, 'home/post_edit.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return HttpResponse("Post deleted successfully")

    return render(request, 'home/post_delete.html', {'post': post})
"""




def about(request):
    return HttpResponse("This is the about page")
