# De Django
from django.urls import path
# Propios
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_page,name='login-page'),
]