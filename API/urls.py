# De django
from django.urls import path
# Propios
from . import views

urlpatterns = [
    path('v1',views.v1,name='v1'),
    path('getstaff',views.getStaff,name='getStaff'),
    path('getcluster',views.getCluster,name='getCluster'),
    path('setdata',views.setData, name='setData'),
    path('active-client',views.changeClient,name='updateClient'),
    path('stats',views.stats),
    path('sheet',views.getSheet),
    path('verify-psw',views.verifyPsw,name='verifyPsw'),
]