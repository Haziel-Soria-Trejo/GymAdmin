# Built-in's
import json
# De django
from django.http import JsonResponse
# Mi código.
from .utils.delete_disp import approve, disapprove
from base.models import Staff
from .utils.setModel import setClient, setClientPay, \
    setClientPay, setTask, setItemSell
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


def setData(req):
    body = json.loads(req.body.decode())
    subject = body['subject']
    by = Staff.objects.get(username=req.user.username)
    res = None

    if subject == 'setClient':
        setClient(
            body['name'], body['membership'],
            by, body['fee'], body['advice'],body['paid_until'])

    elif subject == 'setClientPay':
        res = setClientPay(body['name'], body['id'],
                     float(body['total']), by, 
                    )

    elif subject == 'setTask':
        setTask(body['name'], body['descr'],
                by, Staff.objects.get(username=body['to']),
                body['duration'], int(body['importance']))

    elif subject == 'setItemSell':
        res = setItemSell(body['name'], body['id'],
                          by, body['total'])

    if res == 'duplicates':
        return JsonResponse({'status': 'error', 'code': 204,'message':'Es necesario ingresar el ID del usuario.'})

    return JsonResponse({'status': 'ok', 'code': 404,'message':'Ha ocurrido un error.'})
