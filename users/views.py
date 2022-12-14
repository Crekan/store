from django.shortcuts import render

from .forms import UserLoginForm


def login(request):
    form = UserLoginForm()

    contex = {
        'form': form,
    }
    return render(request, 'users/login.html', contex)


def registration(request):
    return render(request, 'users/register.html')
