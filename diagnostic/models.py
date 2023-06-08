from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from blog.models import NULLUBLE


class Category(models.Model):
    """ Поля:
    - Наименование
    - Описание

    """

    category_name = models.CharField(max_length=250, verbose_name='Наименование', )
    title = models.TextField(verbose_name='Описание', )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Doctor(models.Model):
    name = models.CharField(max_length=20, verbose_name='имя')
    surname = models.CharField(max_length=30, verbose_name='фамилия')
    specialization = models.ForeignKey('diagnostic.Category', on_delete=models.CASCADE, verbose_name='специализация')
    image = models.ImageField(upload_to='./doctors/', verbose_name='фото')
    age = models.IntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(100)],
                              verbose_name='возраст')
    experience = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(40)],
                                     verbose_name='опыт')
    phone = models.CharField(max_length=20, verbose_name='телефон', null=True, blank=True)
    email = models.EmailField(verbose_name='почта', null=True, blank=True)

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Gallery(models.Model):
    img = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey('diagnostic.Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя клиента', **NULLUBLE)
    email = models.EmailField(**NULLUBLE, unique=True)
    phone = models.CharField(max_length=50, **NULLUBLE, unique=True)
    message = models.CharField(max_length=500,**NULLUBLE)

    class Meta:
        verbose_name= 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return {self.email}
