# De django.
from django.db import models
# Mi código.
from stats.models import Dispatches
# Create your models here.

class preUser(models.Model):
    username = models.CharField(max_length=200)
    rank = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    disp_id = models.ForeignKey(Dispatches,on_delete=models.CASCADE,default=None)
