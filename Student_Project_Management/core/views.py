from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User

def home(request):
    return redirect(reverse("core:login"))

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("core:dashboard_redirect"))
    return render(request, "auth/login.html")



@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse("core:login"))


@login_required
def dashboard_redirect(request):
    user: User = request.user
    if user.user_type == User.UserType.STUDENT:
        return redirect(reverse("core:student_dashboard"))
    if user.user_type == User.UserType.HOD:
        return redirect(reverse("core:hod_dashboard"))
    # default: faculty
    return redirect(reverse("core:faculty_dashboard"))


@login_required
def student_dashboard(request):
    user: User = request.user
    if user.user_type == User.UserType.STUDENT:
        return render(request, "dashboards/student_dashboard.html")
    else:
        return redirect(reverse("core:dashboard_redirect"))

@login_required
def faculty_dashboard(request):
    user: User = request.user
    if user.user_type == User.UserType.FACULTY:
        return render(request, "dashboards/faculty_dashboard.html")
    else:
        return redirect(reverse("core:dashboard_redirect"))

@login_required
def hod_dashboard(request):
    user: User = request.user
    if user.user_type == User.UserType.HOD:
        return render(request, "dashboards/hod_dashboard.html")
    else:
        return redirect(reverse("core:dashboard_redirect"))