from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request = request,
                                 username = username,
                                   password = password)
            if user is not None:
                login(request, user)
                return HttpResponse("Auth Succesful")
            else: return HttpResponse("Invalid Data")
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)
