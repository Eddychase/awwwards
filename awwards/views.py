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

def search_results(request):
    # check if the input field exists and that ic contains data
    if 'post' in request.GET and request.GET['post']:
        # get the data from the search input field
        explore_posts = Post.all_posts()
        search_term = request.GET.get('post')
        searched_posts = Post.filter_by_search_term(search_term)
        print(search_term)
        caption = f'Search results for {search_term}'

        if len(searched_posts) == 0:
            caption = f'Results for {search_term} Found'
        search_context = {
            'posts': searched_posts,
            'explore_posts': explore_posts,
            'caption': caption,
        }
        return render(request, 'search.html', search_context)
    else:
        explore_posts = Post.all_posts()
        search_context = {
            'explore_posts': explore_posts,
            'caption': 'Matches found for your search!! Discover More Posts'
        }
        return render(request, 'search.html', search_context)
