from django.contrib import admin
from .models import Profile,Post,Comment,Location,Followers,Rating

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('technologies','Comment','Followers')


# Register your models here.
admin.site.register(Profile)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(Followers)
admin.site.register(Rating)

