# Generated by Django 3.1.7 on 2021-04-17 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_dislike_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
