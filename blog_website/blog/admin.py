from django.contrib import admin
# we're registering our models here so that we can access these on the admi page
from .models import Post, Profile

# registering our models
admin.site.register(Post)
admin.site.register(Profile)


# Register your models here.
