# Generated by Django 5.0 on 2024-01-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_uploadfile_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
