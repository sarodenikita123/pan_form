from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


def user_login(request):
    template_name = "auth_app/login.html"
    if request.method == "POST":
        un = request.POST["un"]
        pw = request.POST["pw"]
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect("show_url")
        else:
            return HttpResponse("plz enter correct username and password")

    return render(request, template_name)


def user_signup(request):
    template_name = "auth_app/register.html"
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("register successful")
    context = {"form": form}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    return redirect("login_url")


def change_password(request):
    if request.method == 'POST':
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect('login_url')
    return render(request, 'auth_app/cpass.html')
