from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, ImageForm
from .models import Image
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    images = Image.objects.all().order_by('-created_at')
    context = {
        'images': images,
    }
    return render(request, 'board.html', context)

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
    image_form = ImageForm(request.POST or None, request.FILES or None)
    if image_form.is_valid():
        new_image = image_form.save(commit=False)
        new_image.author = request.user
        new_image.save()
        return redirect('profile')

    context = {
        'image_form': image_form,
    }
    return render(request, 'profile.html', context)

@login_required
def like_image(request, image_id):
    image = Image.objects.get(id=image_id)
    if request.user in image.likes.all():
        image.likes.remove(request.user)
    else:
        image.likes.add(request.user)
    return redirect('board')

