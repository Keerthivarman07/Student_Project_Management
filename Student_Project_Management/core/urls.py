from django.urls import path
from . import views
app_name="core"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_redirect, name="dashboard_redirect"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("faculty/dashboard/", views.faculty_dashboard, name="faculty_dashboard"),
    path("hod/dashboard/", views.hod_dashboard, name="hod_dashboard"),
]
