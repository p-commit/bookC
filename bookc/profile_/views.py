from django.views.generic.edit import FormView
from django.views.generic.base import View,TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from .forms import RegisterForm


class ProfileView(TemplateView):
    """Профиль"""
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['data'] = Profile.objects.all()
        return context


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


@receiver(post_save, sender=User)
def new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")