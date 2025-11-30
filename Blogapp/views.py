from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as auth_login, logout as auth_logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

@login_required
def home(request):
    postform = PostForm()
    posts = Post.objects.all().order_by('-created')
    context = {'postform':postform,'posts':posts}
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
        newpassword = request.POST.get('newpassword','').strip()
        user = request.user
        if newname:
            if User.objects.filter(username = newname):
                posts = Post.objects.filter(user = request.user)
                context = {'error':"user name exist",'posts':posts}
                return render(request, "blog/profile.html",context)
            else:
                user.username = newname
            
            
        if newpassword:
            user.set_password(newpassword)
            update_session_auth_hash(request,user)

        user.save()    
        return redirect("profile")
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
    user = request.user
    posts = Post.objects.filter(user = user)
    context = {'posts':posts}
    return render(request, "Blog/profile.html",context)

@login_required
def delete_task(request,pk):
    if request.method == "POST":
        post = get_object_or_404(Post,id = pk,user = request.user)
        post.delete()
        return redirect("profile")
    return render(request,"blog/profile.html")
