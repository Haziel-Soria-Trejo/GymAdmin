from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#Mi código
from base.models import Staff
from .models import Activity

# Create your views here.
@login_required(login_url='login-page')
def mainStats(req):
    names = list(Staff.objects.values_list('username'))
    nameList = [i[0] for i in names]

    acts = list(Activity.objects.values_list('name'))
    actList = [i[0] for i in acts]
    actList = set(actList)#Obtener valores únicos.


    context = {'title':'Estadísticas','names':nameList,'acts':actList}

    return render(req,'base/stats.html',context)