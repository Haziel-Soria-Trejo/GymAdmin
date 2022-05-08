from django.db import models
from django.utils import timezone

# Create your models here.
# TODO:
# Las urls
# NO se han hecho las migraciones 
class Activity(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)
    # NOTE: Se pudo haber hecho importando Staff (tal vez)
    # pero lo considere más facil así.
    # TODO:
    # Posiblemente sea necesario cambiar el campo para
    # que apunte a Staff.
    done_by = models.CharField(max_length=200)

class Dispatches(models.Model):
    text = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    # NOTE Mismo dilema que en done_by.
    staff_from = models.CharField(max_length=200)
    staff_to  = models.CharField(max_length=200,default='todos')
    subject = models.CharField(max_length=100,default='mensaje')