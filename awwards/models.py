from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    uploaded_by = models.ForeignKey(User, null=True, related_name='posts')
    country = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200, null=True)
    landing_image = models.ImageField(upload_to='site-images/', null=True)
    screenshot_1 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_2 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_3 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_4 = models.ImageField(upload_to='site-images/', null=True)
    description = models.TextField(blank=True)
    site_link = models.CharField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def all_posts(cls):
        all_posts = cls.objects.all()
        return all_posts

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='profile')
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    profile_photo = models.ImageField(upload_to='images/', blank=True,default='dwf_profile.jpg')
    user_name = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=300, null=True)
    company_name = models.CharField(max_length=300, null=True)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=150, null=True)
    facebook = models.CharField(max_length=200, null=True)
    twitter = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)

    @classmethod
    def all_posts(cls):
        all_posts = cls.objects.all()
        return all_posts

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(description__icontains=search_term)

    def get_user_profile(self, post):
        posts = self.objects.filter(uploaded_by=post.uploaded_by)
        return posts

    def get_one_post(self, post_id):
        return self.objects.get(pk=post_id)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', null=True)
    post = models.ForeignKey(Post, related_name='comments', null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    review = models.TextField(null=True, blank=True)

class Location(models.Model):
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    address = models.IntegerField(null=True)

    def __str__(self):
        return self.country

class Followers(models.Model):
    follower = models.ForeignKey(User, related_name='followers', null=True)
    following = models.ForeignKey(User, related_name='following', null=True)
    followed_on = models.DateTimeField(auto_now_add=True)

    def follow_user(self, current_user, user_other):
        self.following = user_other
        self.follower = current_user
        self.save()

    def unfollow_user(self, user):
        fol = self.objects.get(follower=user)
        fol.delete()

    def __str__(self):
        return f'{self.follower.username} is now following {self.following.username}'

class PostLikes(models.Model):
    user = models.ForeignKey(User, related_name='liked_posts', null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, related_name='likes', null=True)

class CommentsLikes(models.Model):
    user = models.ForeignKey(User, related_name='liked_by', null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    comment = models.ForeignKey(Comment, related_name='likes', null=True)

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', null=True)
    post = models.ForeignKey(Post, related_name='ratings', null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    usability = models.FloatField(default=0.00, null=True)
    design = models.FloatField(default=0.00, null=True)
    creativity = models.FloatField(default=0.00, null=True)
    content = models.FloatField(default=0.00, null=True)
    mobile = models.FloatField(default=0.00, null=True)


