# Generated by Django 5.0 on 2024-01-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ('-time_create',)},
        ),
        migrations.AddField(
            model_name='people',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='people',
            index=models.Index(fields=['-time_create'], name='people_peop_time_cr_be868e_idx'),
        ),
    ]
