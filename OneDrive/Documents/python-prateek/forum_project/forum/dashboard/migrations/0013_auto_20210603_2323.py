# Generated by Django 3.1.7 on 2021-06-03 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='users',
        ),
        migrations.DeleteModel(
            name='DisLike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
