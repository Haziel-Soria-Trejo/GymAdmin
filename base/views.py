# Bult-in
from datetime import datetime 
# De django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
# Mi código
from .models import Cluster, Inventory, Staff,Task, Client
from stats.models import Activity, Dispatches
from .utils.notice import notice
from .utils.get_staff_to import decode_str
# Me parecio más fácil importarlo que
# hacer sus propias views (tal vez como API).

# Create your views here.


@login_required(login_url='login-page')
def home(req):
    tasks = Task.objects.all()
    context = {'title': 'home','tasks':tasks}
    return render(req, 'base/home.html', context)


def login_page(req):
    post = req.POST
    msg = 'El usuario o la contraseña son incorrectos'
    if 'create-btn' in post:
        pass
    if 'login-btn' in post:
        username = post.get('username')
        password = post.get('password')
        try:
            Staff.objects.get(username=username)
        except:
            messages.error(req, msg)
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, msg)

    context = {'title': 'Login'}
    return render(req, 'base/login.html', context)


def register(req):
    post = req.POST
    if 'create-btn' in post:
        username = post.get('username')
        password = post.get('password')
        ps_rep = post.get('password-repeat')
        rank = post.get('ranks')

        if Staff.objects.filter(username=username).exists():
            messages.error(req,'Su usuario ya existe.')
            return redirect('register')
        if password != ps_rep:
            messages.error(req,"Las contraseñas no coinciden.")
            return redirect('register')

        msg = f"""
        Se ha hecho una soliditud de empleo por parte de {username}
        para el cargo de {rank}.
        """
        notice(
            msg,'registro',['CEO','segundo al mando'],
            subject='registro',username=username,password=password,rank=rank) 

        return redirect('login-page')       
        
    context = {'title': 'Registro'}
    return render(req, 'base/register.html', context)


def logout_staff(req):
    logout(req)

    return redirect('home')

@login_required(login_url='login-page')
def staff_page(req):
    users = Staff.objects.all()

    now = str(datetime.now())
    morning = f"{now.split(' ')[0]} 00:00:00"
    activity = Activity.objects.filter(date__range=[morning,now])

    tasks = Task.objects.all()
    dispatches = Dispatches.objects.all()
    
    context = {'title': 'Perfil', 'staff': users,
    'activity':activity, 'tasks':tasks, 'dispatches':dispatches,}
    return render(req, 'base/staff.html', context)

@login_required(login_url='login-page')
def clients(req):
    q = req.GET.get('q') if req.GET.get('q') != None else ''
    
    clients = Client.objects.filter(Q(name__icontains=q))

    context = {'title':'Clientes', 'clients':clients}
    return render(req,'base/clients.html',context)

@login_required(login_url='login-page')
def invetory(req):
    q = req.GET.get('q') if req.GET.get('q') != None else ''
    
    items = Inventory.objects.filter(
        Q(name__icontains=q ) | Q(cluster__name__icontains=q))
    clusters = Cluster.objects.filter(
        Q(name__icontains=q)
    )

    context = {'title':'Inventario', 'items':items,'clusters':clusters}
    return render(req,'base/inventory.html',context)