# Generated by Django 4.1.7 on 2023-02-19 13:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='full_text_mobile',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Полный текст для мобилок'),
            preserve_default=False,
        ),
    ]