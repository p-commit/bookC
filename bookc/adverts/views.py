from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import redirect

from .models import Advert
from .forms import CommentForm


class AdvertsView(ListView):
    '''Список обьявлений'''
    model = Advert
    queryset = Advert.objects.filter(moderation=True)


class AdvertDetailView(DetailView):
    """Объявление"""
    model = Advert
    queryset = Advert.objects.filter(moderation=True)
    slug_field = "slug"


class AddComment(View):
    """Комментарии"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        advert = Advert.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.advert = advert
            form.save()
        return redirect(advert.get_absolute_url())
