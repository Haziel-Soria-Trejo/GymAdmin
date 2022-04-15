from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,\
     BaseUserManager, PermissionsMixin#Para crear la clase User


# Create your models here.
#TODO crear permisos para usuarios.
class UserManager(BaseUserManager):
    def create_user(self,name,password,):
        user = self.model()
        user.set_password(password)

        return user

    def create_superuser(self,name,password):
        user = self.create_user(name,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        self.aggregate()

        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

class Cluster(models.Model):#El inventario se podrá clasificar en grupos
    name = models.CharField(max_length=200)

class Inventory(models.Model):
    name = models.CharField(max_length=200)
    cluster = models.ForeignKey(Cluster)
    date_register = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
    name = models.CharField(max_length=100)
    register_by = models.ForeignKey(User)
    inscription = models.DateTimeField(auto_now_add=True)
    fee = models.FloatField()
    advice = models.TextField()
    is_active = models.BooleanField(default=True)
    

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    assigned_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    duration = models.DurationField()
    importance = models.SmallIntegerField()