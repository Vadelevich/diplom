# Generated by Django 4.2.1 on 2023-05-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0002_alter_doctor_options_doctor_age_doctor_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(upload_to='./doctors/', verbose_name='фото'),
        ),
    ]
