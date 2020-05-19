# Generated by Django 3.0.5 on 2020-05-19 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20200519_1436'),
        ('adverts', '0004_comments_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.ImageSet', verbose_name='Изображения'),
        ),
    ]