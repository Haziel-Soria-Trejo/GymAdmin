# Built-in's
import json
# De django
from django.http import JsonResponse
from django.contrib.auth import authenticate
# Mi código.
from base.models import Staff, Client, Cluster
from stats.models import Activity
from stats.excel.sheet import create
from .utils.delete_disp import approve, disapprove, onlyDelete
from .utils.modelActions import Actions
# Create your views here.

# TODO: Cambiar el nombre de esta vista.


def v1(req):
    body = json.loads(req.body.decode())
    try:
        id = int(body['id'])
        if body['btn'] == 'like':
            approve(id)
        elif body['btn'] == 'check':
            onlyDelete(id)
        else:
            disapprove(id)
    except:
        return JsonResponse({'status': 'error', 'code': 404})

    """if req.user.rank in ('CEO', 'segundo al mando'):
        try:
            id = int(body['id'])
            if body['btn'] == 'like':
                approve(id)
            elif body['btn'] == 'check':
                print('hello')
                onlyDelete(id)
            else:
                disapprove(id)
        except:
            return JsonResponse({'status': 'error', 'code': 404})"""

    return JsonResponse({'status': 'ok', 'code': 204})


def getStaff(req):
    ranks = {
        'CEO': 4,
        'segundo al mando': 3,
        'empleado nivel 1': 2,
        'empleado nivel 2': 1
    }
    user = req.user
    users = list(Staff.objects.values_list('username', 'rank'))
    allowed_users = list(
        filter(lambda i: ranks[user.rank] > ranks[i[1]] or i[0] == user.username, users))

    return JsonResponse({'status': 'ok', 'code': 200, 'users': allowed_users})


def getCluster(req):
    clusters = Cluster.objects.values_list('name')
    cslist = [i[0] for i in clusters]
    return JsonResponse({'staus': 'ok', 'code': 202, 'clusters': cslist})


def setData(req):
    body = json.loads(req.body.decode())
    by = Staff.objects.get(username=req.user.username)
    res = None
    setActions = Actions(body, by, Staff.objects.get)

    res = setActions.switchSubject()

    if res == 'duplicates':
        return JsonResponse({'status': 'error', 'code': 204, 'message': 'Es necesario ingresar el ID del usuario.'})
    return JsonResponse({'status': 'ok','code':200})

def stats(req):
    """
    Filtros posibles:
    staff, --back
    tipo de Acitivity,--back
    periodo, --back
    epacio temporal,--front
    cantidad --back
    """
    acts = Activity.objects.all()
    query = req.GET.get('q')
    if query:
        filters = json.loads(query)
        # ['staff','type','timemax','timemin'] los posibles campos

        acts = acts.filter(
            done_by=filters['staff']) if \
            'staff' in filters and filters['staff'] != '' else acts
        acts = acts.filter(
            name=filters['type']) if \
            'type' in filters and filters['type'] != '' else acts

        if ('timemax' and 'timemin') in filters:
            if (filters['timemax'] and filters['timemin']) != '':
                acts = acts.filter(date__range=[filters['timemin'],filters['timemax']])

    acts = list(acts.values())

    return JsonResponse({'status': 'ok', 'code': 200, 'activity': acts})

def getSheet(req):
    create()
    return JsonResponse({'status': 'ok','code':200})

def verifyPsw(req):
    body = json.loads(req.body.decode())
    username = req.user.username
    psw = body['password']

    user = authenticate(req,username=username,password=psw)
    if user is not None:
        return JsonResponse({'status': 'ok','code':200})
    else :
        return JsonResponse({'status': 'error','code':401})

def changeClient(req):
    try:
        body = json.loads(req.body.decode())
        ID = body['id']
        clt = Client.objects.get(id=ID)
        clt.is_active = (clt.is_active == False)
        
        clt.save()

        return JsonResponse({'status': 'ok','code':200})
        
    except:
        return JsonResponse({'status': 'error','code':404})

