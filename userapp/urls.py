from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('forgot_password/', views.forgot_password,name="forgot_password"),
    path('change_password/', views.change_password,name="change_password"),
    path('home/', views.home,name="home")
]