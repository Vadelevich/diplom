# Generated by Django 4.2.1 on 2023-06-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='изображение')),
                ('count', models.BigIntegerField(verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
