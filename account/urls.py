from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name = 'login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout_view'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name = 'password_change' ),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(), name = "password_change_done"),
    path('register/', views.register, name = 'register'),
    path('', views.dashboard, name = 'board')
]