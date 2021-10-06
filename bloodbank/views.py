from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from django.contrib import sessions

# Create your views here.

def login(request):
    if request.session.has_key('username'):
        return redirect('table')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            data = Add_member.objects.all()
            return render(request, 'table.html', {'username' : username, 'data' : data})
        
        else:
            messages.error(request, 'Somthing Gone Wrong !!!')
            return redirect('login')


    else:
      return render(request, 'login.html')

def signup(request):
    if request.session.has_key('username'):
        return redirect('table')
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
    if request.session.has_key('username'):
       username =  request.session['username']
       return render(request, 'table.html', {'data' : data, 'username' : username})
    else:
        return redirect('login')


def add_member(request):
    # username = request.session['username']
    if request.session.has_key('username'):
       if request.method == 'POST':
            name = request.POST.get['name']
            age = int(request.POST.get['age'])
            phone_number = int(request.POST.get['phonenumber'])
            blood_group = request.POST.get['bloodgroup']
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

    else:
        return redirect('login')
         

def logout(request):
    del request.session['username']
    # auth.logout(request)
    return redirect('login')

def check(request):
    print(request.POST['username'])
    username = request.POST['username']

    if User.objects.filter(username=username).exists():
           return JsonResponse({'message' : 'User Exist'})

    else:
        return JsonResponse({'message' : ' '})


