from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.core.cache import cache

from .forms import RegistrationUserForm
from .models import Profile


# Create your views here.


class RegistrationUser(CreateView):
    form_class = RegistrationUserForm
    template_name = 'app_user/registration.html'

    def post(self, request, *args, **kwargs):
        profile_form = self.form_class(request.POST)
        if profile_form.is_valid():
            user = profile_form.save()
            password = profile_form.cleaned_data.get('password1')
            first_name = profile_form.cleaned_data.get('first_name')
            last_name = profile_form.cleaned_data.get('last_name')
            Profile.objects.create(
                user=user, first_name=first_name,
                last_name=last_name
            )
            username = profile_form.cleaned_data.get('username')
            authenticate_user = authenticate(username=username, password=password)
            # После регистарации сразу авторизируем пользователя
            login(request, authenticate_user)
            # После регистраиции добавляем пользователя в начальную группу
            return redirect('main')

        else:
            return render(request, 'app_user/registration.html', {'form': self.form_class})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'app_user/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('main')


class ProfileInfo(LoginRequiredMixin, TemplateView):
    template_name = 'app_user/profile.html'


class Balance(UpdateView):
    template_name = 'app_user/balance.html'

    def form_valid(self, form):
        Profile.objects.balance = Profile.objects.balance + form.cleaned_data('balance')
