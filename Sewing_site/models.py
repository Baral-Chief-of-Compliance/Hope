from django.db import models


class Post(models.Model):
	name_of_post = models.CharField("Название статьи", max_length = 64)
	text_of_post = models.TextField("Текст статьи")
	date_of_post = models.DateTimeField("Дата статьи", auto_now_add = True, null = True)


	def __str__(self):
		return self.name_of_post


	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"


class PostImage(models.Model):
	title = models.CharField("Заголовок", max_length=100)
	post = models.ForeignKey(Post, verbose_name = "Статья", on_delete = models.CASCADE)
	image_for_post = models.ImageField(upload_to = 'photo_for_post/')


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = "Изображение"
		verbose_name_plural = "Изображения"