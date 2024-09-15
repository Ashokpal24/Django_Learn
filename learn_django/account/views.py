from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        print(user_obj)
        return redirect('login')
    context = {
        "form": form
    }
    return render(request, "account/register.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "account/login.html", {"error":"Invalid username or password"})
    return render(request, "account/login.html", {})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
