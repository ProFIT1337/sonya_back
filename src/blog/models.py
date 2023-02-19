from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name='Ссылка')
    photo = models.ImageField(upload_to='blog/', verbose_name='Заглавное изображение')
    date = models.DateField(verbose_name='Дата публикации')
    description = models.TextField(verbose_name='Короткое описание')
    full_text = RichTextUploadingField(verbose_name='Полный текст')
    full_text_mobile = RichTextUploadingField(verbose_name='Полный текст для мобилок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('date', )