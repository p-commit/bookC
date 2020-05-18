from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from utils.transliteration import transliteration_rus_eng


class Category(models.Model):
    """Категории объявлений"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField(
        "url",
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.slug = transliteration_rus_eng(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class AdvertType(models.Model):
    """Тип обьявления"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Period(models.Model):
    """Срок для объявления"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Срок"
        verbose_name_plural = "Сроки"
        ordering = ["id"]


class Advert(models.Model):
    """Объявление"""
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    category = models.ManyToManyField(
        Category, verbose_name="Категория"
    )
    filters = models.ForeignKey(
        AdvertType, verbose_name="Фильтр", on_delete=models.CASCADE
    )
    period = models.ForeignKey(
        Period, verbose_name="Срок", on_delete=models.CASCADE
    )
    subject = models.CharField("Тема", max_length=200)
    text = models.TextField("Объявление", max_length=10000)

    # images = models.ForeignKey(
    #     'gallery.Gallery',
    #     verbose_name="Изображения",
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL
    # )

    price = models.DecimalField(
        "Цена",
        max_digits=8,
        decimal_places=2,
        default=0.00
    )
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    moderation = models.BooleanField("Модерация", default=False)
    slug = models.SlugField(
        "url",
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.slug = ("advert" + transliteration_rus_eng(self.id) + "-" + str(self.user.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("advert_detail", kwargs={"slug": self.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comments(models.Model):
    """Комментарии"""
    name = models.CharField("Имя", max_length=50)
    text = models.TextField("Сообщение", max_length=400)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    advert = models.ForeignKey(Advert, verbose_name="Объявление", on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " | " + str(self.advert)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"
