from django.contrib.auth.views import LoginView
from django.shortcuts import render

from users.forms import LoginUserForm, RegisterUserForm


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.changed_data["password"])
            user.save()
            return render(request, "users/register.html")
    else:
        form = RegisterUserForm()
    return render(request, "users/register.html", {"from": form})
