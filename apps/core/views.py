from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from apps.jobs.models import Job


def index_page(request):
    jobs = Job.objects.all()[1:4]
    return render(request, 'core/index.html', {'jobs': jobs})


@login_required
def job_dashboard(request):
    jobs = Job.objects.all()
    if request.user.is_authenticated:
        return render(request, 'core/dashboard.html', {'jobs': jobs})
    else:
        return redirect('login_page')


def register_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        user = User.objects.create_user(
            username=username, password=password1, first_name=first_name,
            last_name=last_name, email=email
        )
        user.save()
        login(request, user)
        return redirect('job_dashboard')
    else:
        return render(request, 'core/register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password"]
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('job_dashboard')
        else:
            return redirect('/')
    return render(request, 'core/login.html')


def logout_dash(request):
    logout(request)
    return redirect('index_page')
