from stats.models import Dispatches
from base.models import Staff
from API.models import preUser
from .get_staff_to import *


def notice(text, staff_from, staff_to: tuple, subject, **kargs):
    if staff_to[0] == 'todos':
        msg = Dispatches(
            text=text, staff_from=staff_from, staff_to='todos', subject=subject
        )
        msg.save()

    else:
        people = save_str(staff_to)

        msg = Dispatches(
            text=text, staff_from=staff_from, staff_to=people, subject=subject
        )
        msg.save()
        if subject == 'registro':
            usr = dict(kargs.items())
            save_user(usr['username'], usr['password'],
                      usr['rank'], msg.id)


def save_user(username, password, rank, id):
    disp = Dispatches.objects.get(pk=id)
    usr = preUser(
        username=username, password=password, rank=rank, disp_id=disp
    )
    print(usr)
    usr.save()
