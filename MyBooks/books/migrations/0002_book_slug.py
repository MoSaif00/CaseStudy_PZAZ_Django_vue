# Generated by Django 4.1.2 on 2022-10-20 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='new slug', max_length=200, unique=True),
        ),
    ]
