from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method =='POST':                   
        first_name= request.POST['fname']                 
        
        username= request.POST['username']
       
        password1= request.POST['password1']             
        password2= request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                
                return redirect('home')
            
            else:    
                user=User.objects.create_user(username=username, first_name=first_name, password=password1)
                user.save()
                
                return redirect("login")
        else:
           
            return redirect('home')
       
    

    else:
        return render(request, 'home.html')    



def front(request):
    return render(request, 'front.html') 


def login(request):
    if request.method =='POST':
        username= request.POST['username'] 
        password= request.POST['password']
        user = auth.authenticate(username=username, password=password)  
        
        
        if user is not None:
            auth.login(request, user)
            return redirect("start")
        else:
            
            return redirect("login")
    else:
     return render(request, 'login.html') 


@login_required

def videocall(request):
    return render(request, 'videocall.html', {'name':request.user.username})


@login_required
def start(request):
    return render(request, 'start.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def join(request):
    if request.method == 'POST':
        roomID=request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'join.html')
     