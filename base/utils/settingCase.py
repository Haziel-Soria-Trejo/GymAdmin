from base.utils.notice import notice
from .notice import notice


def changePsw(body, model,user):
    newPsw = body.get('psw1')
    preUser = model.objects.get(username=user)

    preUser.set_password(newPsw)
    preUser.save()


def changeRank(body, user):
    notice(f"El empleado {user}, desea ascender a {body.get('change-rank')}.",
           user, ['CEO', 'segundo al mando'], 'cambio de rango')


def changeCEO(body, model,user):
    oldCEO = model.objects.get(username=user)
    newCEO = model.objects.get(username=body.get('select-staff'))
    newCEO.rank = 'CEO'
    newCEO.save()
    oldCEO.delete()   
       



def delete(body, model,user):
    usr = model.objects.get(username=user)
    usr.delete()


def CASE(body, model, user):
    cases = {
        'change-psw': changePsw,
        'change-rank': changeRank,
        'change-ceo': changeCEO,
        'del-staff': delete,
    }
    for c in cases:
        if c in body:
            if c == 'change-rank':
                changeRank(body, user)
                break
            cases[c](body, model,user)
