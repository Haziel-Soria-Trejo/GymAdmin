# De django
from django.urls import path
# Propios
from . import views

urlpatterns = [
    path('v1',views.v1,name='v1')
]