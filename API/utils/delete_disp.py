from stats.models import Dispatches
from ..models import preUser
from base.models import Staff

def approve(disp_id):
    print('hello')
    usr = preUser.objects.get(disp_id=disp_id)
    
    new_usr = Staff.objects.create(
        username=usr.username,rank=usr.rank
        )
    new_usr.set_password(usr.password)
    new_usr.save()

    delete(disp_id)

def disapprove(disp_id):
    delete(disp_id)

def delete(disp_id):
    usr = preUser.objects.get(disp_id=disp_id)
    usr.delete()
    disp = Dispatches.objects.get(pk=disp_id)
    disp.delete()