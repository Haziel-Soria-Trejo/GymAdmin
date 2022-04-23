# De Django
from django.urls import path
# Propios
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_page,name='login-page'),
    path('register',views.register,name='register'),
    path('logout',views.logout_staff,name='logout'),
    path('personal',views.staff_page,name='staff'),
]