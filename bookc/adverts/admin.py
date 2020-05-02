from django.contrib import admin
from .models import Category, Period, Advert, AdvertType

admin.site.register(Category)
admin.site.register(Period)
admin.site.register(Advert)
admin.site.register(AdvertType)

