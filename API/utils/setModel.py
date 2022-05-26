# Built-in's.
from dateutil.relativedelta import relativedelta as rlv
# Mi código.
from base.models import Client, ClientPayments,\
    Inventory, InventoryPayments, Staff, Task, Cluster
from stats.models import Activity, Dispatches


def createAct(name, amount, by):
    act = Activity(
        name=name,
        amount=amount,
        done_by=by
    )
    act.save()


def duplicates(name, id, model):
    obj = None
    if name != '':
        obj = model.objects.filter(name=name)
        if len(obj) > 1:
            return 'duplicates'
        obj = model.objects.get(name=name)
    else:
        obj = model.objects.get(id=int(id))
    return obj
# Funciones a exportar:


def setClient(name, membership, by,  fee, incription,advice,):
    if membership == 'visit':
        createAct('Cobro de visita', fee, by.username)
        return

    client = Client(
        membership=membership,
        name=name,
        register_by=by,
        fee=fee,
        advice=advice,
    )
    client.save()
    createAct('Registro de cliente', incription, by.username)


def setClientPay(name, id, total, by, ):
    # Rangos de tiempo
    client = duplicates(name, id, Client)
    if client == 'duplicates':
        return client
    if client.is_active == False:
        return
        
    fee = client.fee
    charges = client.charges

    # NOTE:
    # Esta funcionalidad no fue utilizada totalmente pero es útil 
    # para cobros fiados.
    if charges <= 0 and fee-total <= 0:  # no se ha pagado y no se adeuda.
        numb = (total - charges)//fee  # obtener el número de pagos hechos.
        rest = (total-charges) % fee
        if client.membership == 'month':
            client.paid_until = client.paid_until + rlv(months=numb)
        elif client.membership == 'week':
            client.paid_until = client.paid_until + rlv(weeks=numb)
            client.is_active = False
        charges = -rest  # deuda negativa => el GYM le debe al cliente.

    elif charges > 0:
        charges -= total
        if charges <= 0:
            numb = (total - charges)//fee  # obtener el número de pagos hechos.
            rest = (total-charges) % fee
            if client.membership == 'month':
                client.paid_until = client.paid_until + rlv(months=numb)
            elif client.membership == 'week':
                client.paid_until = client.paid_until + rlv(weeks=numb)
            charges = -rest  # deuda negativa => el GYM le debe al cliente.
                
    client.charges = charges
    client.save()
    pay = ClientPayments(
        # place=pay,
        client=client,
        collected_by=by,
        total=total,
    )
    pay.save()
    createAct('Cobro de cuotas', total, by.username)


def setTask(name, descr, by, to, duration, importance,):
    task = Task.objects.create(
        name=name,
        description=descr,
        assigned_by=by,
        assigned_to=to,
        duration=duration,
        importance=importance,
    )
    task.save()


def setItemSell(name, id, by, total):
    item = duplicates(name, id, Inventory)
    if item == 'duplicate':
        return item
    pay = InventoryPayments(
        item=item,
        collected_by=by,
        total=total
    )
    pay.save()
    createAct("Cobro de producto", total, by.username)


def deleteTask(id):
    task = Task.objects.get(id=id)
    task.delete()


def addItem(name,by, cluster, price):
    cluster = Cluster.objects.get(name=cluster)
    item = Inventory(name=name, register_by = by, cluster=cluster, price=price)
    item.save()

def addGroup(name):
    cluster = Cluster(name=name)
    cluster.save()

def updateItem(id, name, cluster, price, delete):
    item = Inventory.objects.get(id=int(id))
    if delete==True:
        item.delete()
        return
    item.name = item.name if name == None else name
    print(price)
    item.cluster = item.cluster if cluster == None else Cluster.objects.get(
        name=cluster)
    item.price = item.price if price == None else price

    item.save()


def updateGroup(id, name, delete):
    cluster = Cluster.objects.get(id=int(id))
    if delete==True:
        cluster.delete()
        return

    cluster.name = name

    cluster.save()

def upgradeStaff(name,rank):
    user = Staff.objects.get(username = name)
    user.rank = rank
    user.save()