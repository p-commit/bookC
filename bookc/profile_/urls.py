from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.ProfileView.as_view(), name = "profile"),
    path("register/", views.RegisterView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
]