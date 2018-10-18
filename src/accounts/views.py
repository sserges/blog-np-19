from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.shortcuts import render

from .forms import UserLoginForm


def login_view(request):
    title = 'Login'
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'form.html', context)


def register_view(request):
    pass


def logout_view(request):
    pass