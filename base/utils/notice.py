from stats.models import Dispatches
from base.models import Staff


def notice(text, staff_from, staff_to:tuple,subject):
    if staff_to[0] == 'todos':
        for person in Staff.objects.all():
            msg = Dispatches(
                text=text,staff_from=staff_from,staff_to=person.username,subject=subject
            )
            msg.save()
    else:
        for person in staff_to:
            msg = Dispatches(
                text=text,staff_from=staff_from,staff_to=person,subject=subject
            )
            msg.save()

