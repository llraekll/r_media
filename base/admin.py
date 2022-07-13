from django.contrib import admin
from .models import Profile, Post, LikePost, Followers

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Followers)
# Register your models here.
