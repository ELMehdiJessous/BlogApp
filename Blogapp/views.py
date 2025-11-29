from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
# Create your views here.

@login_required
def home(request):
    postform = PostForm()
    context = {'postform':postform}
    return render(request, "blog/home.html" ,context)


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

@login_required
def logout(request):
    auth_logout(request)
    return redirect("login")
        
@login_required
def change_name(request):
    if request.method == "POST":
        newname = request.POST.get('newname','').strip()
        if newname:
            user = request.user
            user.username = newname
            user.save()
        return redirect("home")
    return render(request, "blog/home.html")


@login_required
def create_post(request):
    if request.method == "POST":
        x = PostForm(request.POST)
        if x.is_valid():
            y = x.save(commit=False)
            y.user = request.user
            y.save()
        return redirect("home")
            

@login_required
def profile(request):
    pass