from datetime import date, datetime
# Buitl-in's
from datetime import datetime
# Mi código
from base.models import Client

#TODO Modificar esta función para aplicar cargos automáticos.
# NOTE se me ocurre añadir un chekc de último recargo a Client 
#
def surcharge(c):
    #if (c.paid_until<datetime.now()):
    #    c.charges = c.charges + 
    pass

def updateClient():
    clients = Client.objects.all()

    for c in clients:
        if c.is_active :
            surcharge(c)