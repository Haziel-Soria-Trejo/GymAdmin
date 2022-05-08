# De django
from django.urls import path
# Propios
from . import views

urlpatterns = [
    path('v1',views.v1,name='v1'),
    path('getstaff',views.getStaff,name='getStaff'),
    path('getcluster',views.getCluster,name='getCluster'),
    path('setdata',views.setData, name='setData'),
]