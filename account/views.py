from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Wellcom you, You have been login successfully")
            else:
                return HttpResponse("Sorry, your username or passwd is not right")
        else:
            return HttpResponse("Invalid login")
    else:
        login_form = LoginForm()
        return render(request, "account/login.html", {'form': login_form})
