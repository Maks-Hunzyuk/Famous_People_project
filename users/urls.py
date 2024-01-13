from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView

from users.views import UserLoginView, RegisterUserView, logout_view, ProfileUserView, UserPasswordChangeView

app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path("password-change/", UserPasswordChangeView.as_view(), name='password_change'),
    path("password-change/done/", PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name='password_change_done')
]
