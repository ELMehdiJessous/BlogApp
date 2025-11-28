from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@login_required
def home(request):
    return render(request, "blog/home.html")


def login_func(request):
    if request.method == 'POST':
        userName = request.POST['username']
        userPassword = request.POST['userpassword']
        
        if not User.objects.filter(username = userName).exists():
            return render(request,"blog/login.html",{'error':'User name not exist !!'})
        
        user = authenticate(username = userName , password = userPassword)
        
        if not user:
            return render(request,"blog/login.html",{'error':'Password incorrect!!'})
        
        auth_login(request, user)
        return redirect("home")
    return render(request, "blog/login.html")

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    context = {'form':form}
    return render(request ,"blog/signup.html",context)

def logout(request):
    auth_logout(request)
    return redirect("login")
        
        