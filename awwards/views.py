from django.shortcuts import render,redirect, get_object_or_404, reverse, get_list_or_404
from .models import Post
from django.core.mail import mail_admins
from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
import datetime

# Create your views here.
def home(request):
    post = Post.objects.first()
    post_reviews = post.ratings.all()
    posts = Post.objects.all()
    judges = list(set([judge.user for judge in post_reviews]))
    print(posts)

    average_usability = Rating.average_usability(post)
    average_design = Rating.average_design(post)
    average_creativity = Rating.average_creativity(post)
    average_content = Rating.average_content(post)
    average_mobile = Rating.average_mobile(post)
    average_rating = Rating.average_rating(post)
    context = {
        'posts': posts,
        'judges': judges,
        'post': post,
        'average_usability_w': stringify_rating(average_usability)[0],     'average_usability_d': stringify_rating(average_usability)[1],
        'average_design_w': stringify_rating(average_design)[0],           'average_design_d': stringify_rating(average_design)[1],
        'average_creativity_w': stringify_rating(average_creativity)[0],   'average_creativity_d': stringify_rating(average_creativity)[1],
        'average_content_w': stringify_rating(average_content)[0],         'average_content_d': stringify_rating(average_content)[1],
        'average_mobile_w': stringify_rating(average_mobile)[0],           'average_mobile_d': stringify_rating(average_mobile)[1],
        'average_rating': average_rating,
    }
    return render(request, 'index.html', context)

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

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('here')
            form.save()
            return redirect('login')

    form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def stringify_rating(rating):
    r = str(rating).split('.')
    x = r[1]
    if len(r[1]) < 2:
        x += '0'

    return [r[0], x]
