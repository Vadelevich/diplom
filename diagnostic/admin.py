from django.contrib import admin

from blog.models import Blog
from diagnostic.models import Category, Doctor

admin.site.register(Category)
admin.site.register(Doctor)
admin.site.register(Blog)
