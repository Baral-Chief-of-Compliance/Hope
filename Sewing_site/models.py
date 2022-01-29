from django.db import models
from datetime import date
from django.urls import reverse


class Post(models.Model):
	photo_of_preview_post = models.ImageField("Изображение заставки статьи", upload_to = 'photo_of_preview_post/' )
	date_of_post = models.DateField("Дата статьи", default = date.today)
	name_of_post = models.CharField("Название статьи", max_length = 64)
	text_of_post = models.TextField("Текст статьи")


	def __str__(self):
		return self.name_of_post

	def get_absolute_url(self):
		return reverse("post-details", kwargs={"pk": self.id})

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"


class MasterClass(models.Model):
	photo_of_preview_master_class = models.ImageField("Изображение заставки мастеркласс", upload_to = 'photo_of_preview_masterclass/')
	date_of_master_class = models.DateField("Дата публикации", default = date.today)
	title_of_master_class = models.CharField("Название мастер класса", max_length = 64)
	text_of_master_class = models.TextField("Текст к изображению")


	def __str__(self):
		return self.title_of_master_class

	def get_absolute_url(self):
		return reverse("master-class-detail", kwargs={"pk": self.id})


	class Meta:
		verbose_name = "Мастер-класс"
		verbose_name_plural = "Мастер-классы"
