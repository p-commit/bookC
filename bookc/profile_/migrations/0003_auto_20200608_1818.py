# Generated by Django 3.0.5 on 2020-06-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0002_auto_20200608_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]