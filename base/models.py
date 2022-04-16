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
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    """Los objetos dentro de las instalaciones."""
    name = models.CharField(max_length=200)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    date_register = models.DateTimeField(auto_now_add=True)
    register_by = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    """Modela los clientes."""
    name = models.CharField(max_length=100)
    register_by = models.ForeignKey(
        Staff, on_delete=models.SET_NULL, null=True)
    inscription = models.DateTimeField(auto_now_add=True)
    fee = models.FloatField()
    advice = models.TextField(default='')
    is_active = models.BooleanField(default=True)

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
    importance_level = ((1,1),(2,2),(3,3))
    importance = models.SmallIntegerField(choices=importance_level,default=2)

    def __str__(self):
        return self.name
