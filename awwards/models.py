from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    uploaded_by = models.ForeignKey(User, null=True, related_name='posts')
    country = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200, null=True)

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
