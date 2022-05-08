# Built-in's
import json
# De django
from django.http import JsonResponse
# Mi código.
from .utils.delete_disp import approve, disapprove
from base.models import Staff,Client,Cluster
from .utils.modelActions import Actions
# Create your views here.

# TODO: Cambiar el nombre de esta vista.

def v1(req):
    body = json.loads(req.body.decode())
    if req.user.rank in ('CEO', 'segundo al mando'):
        try:
            id = int(body['id'])
            if body['btn'] == 'like':
                approve(id)
            else:
                disapprove(id)
        except:
            return JsonResponse({'status': 'error', 'code': 404})

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
    return JsonResponse({'staud':'ok','code':202,'clusters':cslist})

def setData(req):
    body = json.loads(req.body.decode())
    by = Staff.objects.get(username=req.user.username)
    res = None
    setActions  = Actions(body,by,Staff.objects.get)

    res = setActions.switchSubject()

    if res == 'duplicates':
        return JsonResponse({'status': 'error', 'code': 204, 'message': 'Es necesario ingresar el ID del usuario.'})
    return JsonResponse({'status': 'ok'})
