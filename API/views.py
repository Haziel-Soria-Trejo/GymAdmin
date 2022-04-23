# Built-in's
import json
# De django
from django.http import JsonResponse
# Mi código.
from stats.models import Dispatches
# Create your views here.

# TODO: Cambiar el nombre de esta vista.
def v1(req):  
    body = json.loads(req.body.decode())

    if req.user.rank in ('CEO','segundo al mando'):
       try:
            if body['btn'] == 'like':
               print('like')
            else:
                print('dislike')
       except:
           return JsonResponse({'status':'error','code':404})

    return JsonResponse({'status':'ok','code':204})