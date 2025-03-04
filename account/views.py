from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User 
from .forms import RegistrationForm, ImageForm, ProfileEditForm
from .models import Image
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    images = Image.objects.all().order_by('-created_at') 
    users = User.objects.exclude(id=request.user.id)

    context = {
        'images': images,
        'users': users, 
    }
    return render(request, 'board.html', context)


def delete_item(request, image_id):
    image = get_object_or_404(Image, pk = image_id).delete()
    return redirect('profile')

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

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_posts = Image.objects.filter(author=user).order_by('-created_at')  # Все посты пользователя
    
    context = {
        'profile_user': user, 
        'user_posts': user_posts, 
    }
    return render(request, 'user_profile.html', context)