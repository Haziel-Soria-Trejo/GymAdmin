from django.urls import path
#Mi código.
from . import views


urlpatterns = [
    path('estadisticas',views.mainStats,name='stats')
]