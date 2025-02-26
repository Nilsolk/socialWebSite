from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required

# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             user = authenticate(request = request,
#                                  username = username,
#                                    password = password)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponse("Auth Succesful")
#             else: return HttpResponse("Invalid Data")
#     else:
#         form = LoginForm()
#     context = {'form': form}
#     return render(request, 'login.html', context)


@login_required
def dashboard(request):
    return render(request, 'board.html')


def register(request):
    if request.method == "POST":
        user_form  = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(
                user_form.cleaned_data['password']
            )
            user.save()
            return render(request, 'registration/register_done.html', {'new_user': user})

    else:
        user_form = RegistrationForm()
    return render(request, 'registration/register.html', context = {'register_form': user_form})


@login_required
def profile(request):
    return render(request, "profile.html")
