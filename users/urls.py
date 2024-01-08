from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, register

app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register')
]