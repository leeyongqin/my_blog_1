from django.contrib import admin
from blog.models import Blog, BlogAdmin

admin.site.register(Blog, BlogAdmin)
