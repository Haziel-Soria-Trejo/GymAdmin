from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# TODO crear permisos para usuarios.


class Staff(AbstractUser):
    """Esta clase es una modificación del modelo
    usuario normal. Creada para añadir los rangos"""
    username = models.CharField(max_length=200, default="", unique=True)
    RANKS = (
        'CEO', 'segundo al mando',
        'empleado nivel 1', 'empleado nivel 2')
    ranks_readable = tuple(zip(RANKS, RANKS))
    rank = models.CharField(
        max_length=50, choices=ranks_readable, default=RANKS[-1])

    def __str__(self):
        return f'{self.username}--{self.rank}'


class Cluster(models.Model):
    """Agrupar en inventario en grupos."""
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    """Los objetos dentro de las instalaciones."""
    name = models.CharField(max_length=200)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    date_register = models.DateTimeField(auto_now_add=True)
    register_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class InventoryPayments(models.Model):
    """Su propósito es registrar cada cobro de un item."""
    item = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True)
    #quantity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    collected_by = models.ForeignKey(
        Staff, on_delete=models.SET_NULL, null=True)
    total = models.FloatField()

    def __str__(self) -> str:
        return self.item.name


class Client(models.Model):
    """Modela los clientes."""
    # Los tipos de membresía.
    client_type = ('month', 'week', 'visit')
    client_type_readable = tuple(zip(client_type, client_type))

    inscription = models.DateTimeField(auto_now_add=True)
    membership = models.CharField(
        max_length=50, choices=client_type_readable, default=client_type[0])
    name = models.CharField(max_length=100)
    register_by = models.ForeignKey(
        Staff, on_delete=models.SET_NULL, null=True)
    inscription = models.DateTimeField(auto_now_add=True)
    fee = models.FloatField()
    paid_until = models.DateTimeField(auto_now_add=True)
    #pay_in = models.DateTimeField(auto_now=True)
    # NOTE elimine pay_in ya que me pareció poco
    # útil, decidi hacer el cálculo en 'stats' 
    advice = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    charges = models.FloatField(default=0)

    def __str__(self):
        return self.name


class ClientPayments(models.Model):
    """Su propósito es registrar cada cobro de una cuota."""
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    collected_by = models.ForeignKey(
        Staff, on_delete=models.SET_NULL, null=True)
    total = models.FloatField()

    def __str__(self):
        return self.client.name


class Expenses(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    total = models.FloatField()

    def __str__(self):
        return self.name


class Task(models.Model):
    """Usar para la to-do-list-app."""
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    assigned_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, related_name='assigned_by')
    assigned_to = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, related_name='assigned_to')
    duration = models.TimeField()
    importance_level = ((1, 1), (2, 2), (3, 3))
    importance = models.SmallIntegerField(choices=importance_level, default=2)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
