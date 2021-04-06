from django.db import models

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
