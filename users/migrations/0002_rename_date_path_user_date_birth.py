# Generated by Django 5.0 on 2024-01-14 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_path',
            new_name='date_birth',
        ),
    ]
