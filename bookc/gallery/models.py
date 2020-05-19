from django.db import models
from datetime import datetime
from django.utils import timezone
import random
import os



def get_path_upload_image(file):
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + timezone.now().strftime("%h-%m-%s") + '.' + end_extention
    return os.path.join('photos', '{}', '{}').format(time, file_name)


class Image(models.Model):
    """Фото"""
    name = models.CharField("Имя", max_length=50)
    image = models.ImageField("Фото", upload_to="gallery/")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.image.name = get_path_upload_image(self.image.name)
        self.slug = self.image.name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class ImageSet(models.Model):
    """Галерея"""
    name = models.CharField("Имя", max_length=50)
    photos = models.ManyToManyField(Image, verbose_name="Фотографии")
    slug = models.SlugField("url", max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name  + str(random.randint(1000,9999))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"