"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from .views import *

app_name = "main"

urlpatterns = [
    path('articles', ArticlePage.as_view(), name="articles"),
    path('home', Homepage.as_view(), name="homepage"),
    path('about', views.about, name="about"),
    path('courses', views.courses, name="courses"),
    path('resources', views.resources, name="resources"),
    path('projects', views.projects, name="projects"),

]
