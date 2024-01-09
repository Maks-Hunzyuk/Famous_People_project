from typing import Any
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from users.forms import LoginUserForm, RegisterUserForm, UserProfileForm


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}
    success_url = reverse_lazy("users:login")


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}


class ProfileUserView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = "users/profile.html"
    extra_context = {"title": "Профиль пользователя"}

    def get_success_url(self) -> str:
        return reverse_lazy("users:profile")

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return self.request.user


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
