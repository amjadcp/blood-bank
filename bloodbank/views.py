from django.contrib import auth
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            data = Add_member.objects.all()
            return render(request, 'table.html', {'username' : username, 'data' : data})
        
        else:
            messages.error(request, 'Somthing Gone Wrong !!!')
            return redirect('login')


    else:
      return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
       username = request.POST['username']
       password1 = request.POST['password1']
       password2 = request.POST['password2']

       if User.objects.filter(username=username).exists():
           messages.info(request, 'User already exist')
           return redirect('signup')
       else:
           if password1 == password2:
               user = User.objects.create_user(username=username, password=password1)
               user.save()
               messages.info(request, 'Successfully Created')
               return redirect('signup')

           else:
               messages.info(request, 'Please check password')
               return redirect('signup')
               
    else:
       return render(request, 'signup.html')


def table(request):
    data = Add_member.objects.all()
    return render(request, 'table.html', {'data' : data})

def add_member(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST['age'])
        phone_number = int(request.POST['phonenumber'])
        blood_group = request.POST['bloodgroup']
        Add_member.objects.create(
            name=name,
            age=age,
            phone_number=phone_number,
            blood_group=blood_group
        )
        data = Add_member.objects.all()
        for element in data:
           print(element.id)
        return redirect('table')
    else:
       return render(request, 'add_member.html')

def logout(request):
    auth.logout(request)
    return redirect('login')