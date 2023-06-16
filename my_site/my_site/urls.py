"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse
from . views import home_view
from . views import contact_view
from . views import about_view
from . views import social_view
from . views import projects_view


urlpatterns = [
    path("my_app/", include("my_app.urls")),
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("contact/", contact_view, name="contact"),
    path("about/", about_view, name="about") ,
    path("projects/", social_view , name="projects"),
    path("social/", projects_view, name="social"),
    path("home/", home_view, name="home"),

    ]
