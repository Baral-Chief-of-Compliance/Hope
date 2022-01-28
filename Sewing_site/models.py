from django.db import models
from datetime import date

class Post(models.Model):
	photo_of_preview_post = models.ImageField("Изображение заставки статьи", upload_to = 'photo_of_preview_post/' )
	date_of_post = models.DateField("Дата статьи", default = date.today)
	name_of_post = models.CharField("Название статьи", max_length = 64)
	text_of_post = models.TextField("Текст статьи")


	def __str__(self):
		return self.name_of_post


	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"


class PostImage(models.Model):
	post = models.ForeignKey(Post, verbose_name = "Статья", on_delete = models.CASCADE)
	image_for_post = models.ImageField("Изображение к статье", upload_to = 'photo_for_post/')
	title = models.CharField("Подпись к изображению", max_length=100, blank=True)
	text_of_image = models.TextField("Текст к изображению", blank = True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = "Изображение"
		verbose_name_plural = "Изображения"
