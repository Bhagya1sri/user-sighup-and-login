from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth




def login(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"post.html")

        else:
           messages.info(request,"invalid credential") 

           return redirect("login")

    return render(request,"login.html")

def sighup(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
           if User.objects.filter(username=username).exists:
            messages.info(request,"usernametaken")
            return redirect("sighup")
           elif User.objects.filter(email=email).exists:
            messages.info(request,"emailtaken")
            return redirect("sighup")

           else:   
            user = User.objects.create_user(username=username,password=password1,last_name=last_name,first_name=first_name,email=email)
            user.save
            print("user created")
            return redirect("/")
        else:
            print("password not matched")
            return redirect("sighup")

    return render(request,"sighup.html")

# Create your views here.
