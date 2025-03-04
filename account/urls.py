from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='board'),
    path('profile/', views.profile, name="profile"), 
    path('like/<int:image_id>/', views.like_image, name='like_image'),
    path('delete_item/<int:image_id>/', views.delete_item, name ='delete_item'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]