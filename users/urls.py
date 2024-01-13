from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetView
)

from users.views import (
    UserLoginView,
    RegisterUserView,
    logout_view,
    ProfileUserView,
    UserPasswordChangeView,
)

app_name = "users"


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("profile/", ProfileUserView.as_view(), name="profile"),
    path("password-change/", UserPasswordChangeView.as_view(), name="password_change"),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html",
            email_template_name="users/password_reset_email.html",
            success_url = reverse_lazy("users:password_reset_done")
            ),
        name="password_change_done",
    ),
    path(
        "password-reset/",
        PasswordResetView.as_view(template_name="users/password_reset_form.html"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url = reverse_lazy("users:password_reset_done")
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
