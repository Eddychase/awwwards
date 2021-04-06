from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    post = Post.objects.first()
    post_reviews = post.ratings.all()
    posts = Post.objects.all()

    print(posts)
