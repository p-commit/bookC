from django.urls import path
from . import views

urlpatterns = [
    path("", views.AdvertsView.as_view()),
    path("comments/<int:pk>/", views.AddComment.as_view(), name="add_comment"),
    path("<slug:slug>/", views.AdvertDetailView.as_view(), name="advert_detail"),
]
