# De django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
# Mi código
from .models import Staff
# Create your views here.

@login_required(login_url='login-page')
def home(req):
    context = {'title':'home'}
    return render(req,'base/home.html',context)


def login_page(req):
    post = req.POST
    msg = 'El usuario o la contraseña son incorrectos'
    if 'create_btn' in post:
        pass
    if 'login-btn' in post:
        username = post.get('username')
        password = post.get('password')
        try:
            Staff.objects.get(username=username)
        except:
            messages.error(req, msg)
        user = authenticate(req,username=username,password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req,msg)
    
    context = {'title':'Login'}
    return render(req,'base/login.html',context)

def register(req):
    context = {'title':'Registro'}
    return render(req,'base/register.html',context)

def logout_staff(req):
    logout(req)
    
    return redirect('home')

def profile(req):
    users = Staff.objects.all()
    context = {'title':'Perfil','staff':users}
    return render(req,'base/profile.html',context)