from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages



def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid(): #clean yapmadık ama zaten clean yapılıyor. biz aşağıda override yaptık...
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None: 
            messages.info(request, "Login failed")
            return render(request, "login.html", context)
        messages.success(request, "Login successful")
        login(request,user)
        return redirect("index")
    return render(request, "login.html", context)  #isvalid değilse- get request olduysa veya post'ta sorun olduysa.



def logoutUser(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("index")




def register(request):
    form = RegisterForm(request.POST or None)  #GET request olduğunda bişey yapmıyor
    if form.is_valid():  #valid değilse de boş formla dönüyor
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username= username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.info(request, "Successfully registered new user")
        return redirect("index")
    context = { 
        "form" : form 
    }
    return render(request, "register.html", context)



    #if request.method == "POST":
      # form = RegisterForm(request.POST)
      #  if form.is_valid():
     #       username = form.cleaned_data.get("username")
    # #       password = form.cleaned_data.get("password")
     #       newUser = User(username= username)
    #        newUser.set_password(password)
     #       newUser.save()
    #        login(request, newUser)
      #      return redirect("index")
     #   context = { 
    #        "form" : form 
    #    }
    #    return render(request, "register.html", context)
    #else:
     #   form = RegisterForm()
      #  context = { 
       #     "form" : form 
       # }
      #  return render(request, "register.html", context)"""






