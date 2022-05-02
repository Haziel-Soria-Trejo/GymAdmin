from base.models import Client, ClientPayments,\
     Inventory, InventoryPayments, Task

def duplicates(name,id,model):
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
def setClient(name, membership, by,  fee, advice,paid_until):
    client = Client(
        membership=membership,
        name=name,
        register_by=by,
        fee=fee,
        advice=advice,
        paid_until=paid_until,
    )
    client.save()

def setClientPay(name, id, total,  by, ):
    client = duplicates(name,id,Client)
    if client == 'duplicates':
        return client
    pay = ClientPayments(
        #place=pay,
        client=client,
        collected_by=by,
        total=total,
    )
    pay.save()
    #ClientPayments.objects.create(place=pay)

def setTask(name, descr, by, to, duration, importance,):
    task = Task.objects.create(
        name=name,
        description=descr,
        assigned_by = by,
        assigned_to = to,
        duration = duration,
        importance = importance,
    )
    task.save()


def setItemSell(name,id,by,total):    
    item = duplicates(name,id,Inventory)
    if item == 'duplicate':
        return item
    pay = InventoryPayments(
        item=item,
        collected_by = by,
        total = total
    )
    pay.save()
