from django.views.generic import ListView

from .models import Advert


class AdvertsView(ListView):
    '''Список обьявлений'''
    model = Advert
    queryset = Advert.objects.filter(moderation = True)


