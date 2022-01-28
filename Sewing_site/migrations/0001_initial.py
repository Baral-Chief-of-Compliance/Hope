# Generated by Django 3.2.3 on 2022-01-27 11:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_of_preview_post', models.ImageField(upload_to='photo_of_preview_post/', verbose_name='Изображение заставки статьи')),
                ('date_of_post', models.DateTimeField(default=datetime.date.today, verbose_name='Дата статьи')),
                ('name_of_post', models.CharField(max_length=64, verbose_name='Название статьи')),
                ('text_of_post', models.TextField(verbose_name='Текст статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_for_post', models.ImageField(upload_to='photo_for_post/', verbose_name='Изображение к статье')),
                ('title', models.CharField(max_length=100, verbose_name='Подпись к изображению')),
                ('text_of_image', models.TextField(verbose_name='Текст к изображению')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sewing_site.post', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
