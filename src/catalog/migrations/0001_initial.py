# Generated by Django 4.1.7 on 2023-02-19 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Нвазние')),
                ('slug', models.SlugField(verbose_name='Ссылка')),
                ('order_index', models.PositiveSmallIntegerField(default=1, verbose_name='Индекс сортировки')),
            ],
            options={
                'verbose_name': 'Помещение',
                'verbose_name_plural': 'Помещения',
                'ordering': ('order_index',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Ссылка')),
                ('photo', models.ImageField(upload_to='categories/', verbose_name='Фотография')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('order_index', models.PositiveSmallIntegerField(default=1, verbose_name='Индекс сортировки')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childes', to='catalog.category', verbose_name='Родительская категория')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='catalog.room', verbose_name='Помещение')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('order_index',),
            },
        ),
    ]
