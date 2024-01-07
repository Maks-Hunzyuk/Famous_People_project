from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import LoginUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
                                username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('people:home'))
    else:
        form = LoginUserForm()
    context = {'form': form}
    return render(request, 'users/login.html',context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
