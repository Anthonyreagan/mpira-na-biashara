# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import BlogPost # Import your BlogPost model

def blog_list_view(request):
    """
    Displays a list of all published blog posts.
    """
    # Get all blog posts that are marked as published, ordered by most recent
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    context = {
        'posts': posts,
        'title': 'Our Blog'
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail_view(request, slug):
    """
    Displays the details of a single blog post based on its slug.
    Uses get_object_or_404 to return a 404 error if the post is not found.
    """
    # Retrieve the blog post by its unique slug, and ensure it's published
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    context = {
        'post': post,
        'title': post.title
    }
    return render(request, 'blog/blog_detail.html', context)