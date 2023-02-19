from django.db import models


class Room(models.Model):
    """Помещение для категории"""
    title = models.CharField(max_length=255, verbose_name='Нвазние')
    slug = models.SlugField(verbose_name='Ссылка')
    order_index = models.PositiveSmallIntegerField(default=1, verbose_name='Индекс сортировки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'
        ordering = ('order_index',)


class Category(models.Model):
    """Категория товара в магазине"""
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='categories', verbose_name='Помещение')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='childrens',
                               verbose_name='Родительская категория')
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name='Ссылка')
    photo = models.ImageField(upload_to='categories/', verbose_name='Фотография')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    order_index = models.PositiveSmallIntegerField(default=1, verbose_name='Индекс сортировки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order_index',)
