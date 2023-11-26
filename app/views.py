from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import todo
import datetime

# Create your views here.
@login_required(login_url='/log_in')
def todo_list(request):
    value = datetime.datetime.now()
    querysetop = todo.objects.all()
    queryset=querysetop.get(id = 1)
    name=queryset.activity_name
    desc=queryset.activity_desc
    return render(request, 'index.html',{'value':value,'params':name,'desc':desc,'data':querysetop})

def form(request):
    if request.method == 'POST':
        activity_name = request.POST.get('activity_name')
        activity_desc = request.POST.get('activity_desc')
        todo.objects.create(
            activity_name = activity_name,
            activity_desc = activity_desc
        )
        return redirect('/')
    return render(request, 'form.html')

def delete(request, id):
    todo.objects.get(id = id).delete()
    return redirect('/')

def update(request, id):
    queryset = todo.objects.get(id=id)
    if request.method == 'POST':
        activity_name = request.POST.get('activity_name')
        activity_desc = request.POST.get('activity_desc')

        queryset.activity_name = activity_name
        queryset.activity_desc = activity_desc
        queryset.save()
        return redirect('/')
    name=queryset.activity_name
    desc=queryset.activity_desc
    return render(request, 'update.html',{'name':name,'desc':desc})

def sign_up(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists() or user == '':
            messages.info(request,'USER ALREADY EXISTS!')
            return redirect('/sign_up')
        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account successfully created!')
        return redirect('/log_in')
    return render(request, 'sign_up.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request, 'Username does not Exist!')
            return redirect('/log_in')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Wrong Username or Password!')
            return  redirect('/log_in')
        else:
            login(request, user)
            return redirect('/')
    return render(request, 'log_in.html')

def log_out(request):
    logout(request)
    return redirect('/log_in')