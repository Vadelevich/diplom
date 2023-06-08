from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

NULLUBLE = {'blank': True, 'null': True}


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', **NULLUBLE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=4096)


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение')
    count = models.BigIntegerField(verbose_name='количество просмотров')
    date = models.DateField(auto_created=True)
    category = models.ForeignKey('diagnostic.Category', on_delete=models.SET_NULL, **NULLUBLE)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
