# Generated by Django 3.0.5 on 2020-05-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='url'),
        ),
    ]
