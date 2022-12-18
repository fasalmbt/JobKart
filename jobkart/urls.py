"""jobkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from apps.core.views import index_page, register_page, login_page, logout_dash, job_dashboard, login
from apps.jobs.views import job_details, add_job, apply_job, applied_jobs, recieved_apps,view_applied_job

urlpatterns = [
    path('', index_page, name='index_page'),
    path('register/', register_page, name='register_page'),
    path('login/', LoginView.as_view(template_name='core/login.html'),
         name='login_page'),
    path('logout/', logout_dash, name='logout'),
    path('dashboard/', job_dashboard, name='job_dashboard'),
    path('admin/', admin.site.urls),

    path('job_details/<int:job_id>/', job_details, name='job_details'),
    path('jobs/add/', add_job, name='add_job'),
    path('apply_job/<int:job_id>/', apply_job, name='apply_job'),
    path('applied_jobs/', applied_jobs, name='applied_jobs'),
    path('recieved_apps/', recieved_apps, name='recieved_apps'),
    path('view_applied_job/<int:job_id>/', view_applied_job, name='view_applied_job')

]


