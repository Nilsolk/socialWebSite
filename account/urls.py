from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name = 'login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout_view'),
    path('', views.dashboard, name = 'board')
]