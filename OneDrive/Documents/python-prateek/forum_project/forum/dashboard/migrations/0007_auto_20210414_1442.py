# Generated by Django 3.1.7 on 2021-04-14 09:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210414_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
