from django.shortcuts import render,redirect
from .models import Post
from django.contrib import auth, messages

# Create your views here.
def home(request):
    post = Post.objects.first()
    post_reviews = post.ratings.all()
    posts = Post.objects.all()

    print(posts)

def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
