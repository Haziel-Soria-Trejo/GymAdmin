from django.db import models

# Create your models here.
# TODO:
# Crear una forma de realizar encuestas
# Las urls
# NO se han hecho las migraciones 
class Transactions(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)