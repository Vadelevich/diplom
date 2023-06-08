from django.contrib import admin

from blog.models import Comment
from diagnostic.models import Gallery

admin.site.register(Comment)
admin.site.register(Gallery)