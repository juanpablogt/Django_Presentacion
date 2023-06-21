from django.shortcuts import render
from django.http.response import HttpResponse


articles = {
    "home": " 666 Juan Pablo",
    "contact": "Contact Page",
    "about": "About Page",
    "social": "Social Page",
    "projects": "Projects Page",
    "error": "Error Page" 
}

# Create your views here.
def home_view(request,topics):
    return HttpResponse(articles[topics])

def contact_view(request,topics):

    return HttpResponse(articles[topics])

def about_view(request,topics):

    return HttpResponse(articles[topics])

def social_view(request,topics):

    return HttpResponse(articles[topics])

def projects_view(request,topics):

    return HttpResponse(articles[topics])

