from django.urls import path
from . import views

urlpatterns = [
    path("", views.AdvertsView.as_view()),
]
