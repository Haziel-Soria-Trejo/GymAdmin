from django.contrib import admin
# Aqui están los modelos
from .models import *

# Register your models here.
admin.site.register(Staff)
admin.site.register(Cluster)
admin.site.register(Inventory)
admin.site.register(Client)
admin.site.register(Task)
admin.site.register(InventoryPayments)
admin.site.register(ClientPayments)
admin.site.register(Expenses)
